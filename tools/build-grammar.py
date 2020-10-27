"""Convert the YAML source grammar to JSON.

VS Code only supports JSON-based grammars, which is why the source YAML
grammar must be converted into its JSON equivalent before using the
extension.

This script takes care of this, as well as variable insertion, i.e.
converting the string ``${{ var }}`` into the string stored under the
``variables.var`` key of the YAML source file.

This script requires PyYAML: ``https://github.com/yaml/pyyaml``

For usage instructions, call this script with the `-h` flag set.

"""

import argparse
import io
import json
import re
from typing import Any, Dict, Tuple

import yaml

__author__ = 'leonhard-s'
__version__ = '0.1.0'

# RegEx pattern used to match replacable expressions
_PATTERN = re.compile('(\\${{ ?(\\w+?) ?}})')


def convert_yaml(source: str, target: str, replace: bool = True) -> None:
    """Convert the given YAML source file into its JSON equivalent.

    If the ``replace`` flag is set, this will additionally extract any
    keys stored under the top-level ``variables`` key of the YAML file.

    These keys will not be included in the resulting JSON file, but may
    be used to replace placeholders within other keys.

    The syntax for these placeholders is the same as for GitHub
    actions:

        ${{example1}}
        ${{ example2 }}

    Placeholders that do not match any provided key will not be
    modified.

    Args:
        source (str): The input YAML file to process.
        target (str): The output JSON file to generate.
        replace (bool, optional): Whether to replace placeholders with
            matching keys from the ``variables`` key. Defaults to True.

    """
    # Read the source YAML
    with open(source) as in_file:
        data: Dict[str, Any] = yaml.load(  # type: ignore
            in_file, Loader=yaml.SafeLoader)

    # Extract the variables key, if enabled
    expressions: Dict[str, str] = {}
    if replace:
        expressions = data.pop('variables', expressions)
        # Double up the escapes in the dict values
        for key, value in expressions.items():
            expressions[key] = value.replace('\\', '\\\\')

    # Write the JSON data to a virtual file
    buffer = io.StringIO()
    json.dump(data, buffer, indent=4)
    buffer.seek(0)

    # Write the output JSON file, replacing any expressions
    expression: Tuple[str, str]
    with open(target, 'w') as out_file:
        for line in buffer:
            if replace:
                # Iterate over all replacable expressions
                for expression in _PATTERN.findall(line):
                    placeholder, key = expression
                    try:
                        line = line.replace(placeholder, expressions[key])
                    except KeyError:
                        pass
            out_file.write(line)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='the YAML file to convert')
    parser.add_argument('output', help='the path of the generated JSON file')
    parser.add_argument('--noreplace', action='store_true',
                        help='disable expression replacement')
    args = parser.parse_args()

    convert_yaml(args.file, args.output, replace=not args.noreplace)
