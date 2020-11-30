# dumps, dump, loads, load

data = {
    'name' : 'Gopinath Jayakumar',
    'value': 'nothing',
    'exp'  : '10+',
    'hobbies': ('always eating', 'always sleeping'),
    'is_nothing': True
}

import json

# dumps -> convert python to json
print(type(data))

j = json.dumps(data)
print(j)

# dump  -> write the json file
with open('datajson.json', 'w') as file:
    json.dump(j, file, indent=4)