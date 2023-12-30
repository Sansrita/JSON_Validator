import json
from jsonschema import validate
from jsonschema.exceptions import ValidationError

with open('person-schema.json') as f:
    document= json.load(f)

try:
    validate(instance=document, schema=json)
    print("Validation sucedded!")
except ValidationError as e:
    print("Validation falied!")
    print(f"Error message: {e.message}")