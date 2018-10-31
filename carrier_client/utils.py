import json
import jsonschema
from os.path import join, dirname

json_schemas = {}

def load_json_schema(schema):
    filename = "{}.json".format(schema)
    relative_path = join('schemas', filename)
    absolute_path = join(dirname(__file__), relative_path)

    with open(absolute_path) as schema_file:
        json_schemas[schema] = json.loads(schema_file.read())

load_json_schema('message')

def validate_payload(payload):
    return jsonschema.validate(payload, json_schemas['message'], format_checker=jsonschema.FormatChecker())