import json

def read_file(path):
    file = open(path, 'r')
    data = file.read()
    file.close()
    return data

def read_json(path):
    return json.loads(read_file(path))
