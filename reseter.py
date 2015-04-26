import json

with open('dict_storage.json') as dict_storage:
    idol_list = json.loads(dict_storage.read())

for i in idol_list:
    idol_list[i] = [0, 0, 0]

with open('dict_storage.json', 'w') as karm:
    json.dump(idol_list, karm)