__author__ = 'padewitte'
import json

json_string = '{"first_name": "Guido", "last_name":"Rossum"}'
parsed_json = json.loads(json_string)
print(parsed_json['first_name'])
d = {
    'first_name': 'Guido',
    'titles': ['BDFL', 'Developer'],
}
print(json.dumps(d, sort_keys=True, indent=4))