import json

# loads -> convert json to python
py = json.loads('{"name" : "GN", "active" : false, "value" : null}')
print(py)

with open('datajson.json', 'r') as file:
    j_value = json.load(file)       # read the data from json
    j_to_p = json.loads(j_value)    # convert json to python
print(j_to_p)