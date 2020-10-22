import json

with open('source_file_2.json', 'r') as json_file:
    data = json.load(json_file)

data_sorted = sorted(data, key=lambda k: k['priority'])

# managers
list_managers = []
for data in data_sorted:
    for item in data['managers']:
        if item not in list_managers:
            list_managers.append(item)

dict_managers = {}
for i in list_managers:
    list_projects = []
    for data in data_sorted:
        if i in data['managers']:
            list_projects.append(data['name'])
    dict_managers[i] = list_projects

with open('managers.json', 'w') as managers_file:
    json.dump(dict_managers, managers_file, indent=4)


# watchers
list_watchers = []
for data in data_sorted:
    for item in data['watchers']:
        if item not in list_watchers:
            list_watchers.append(item)

dict_watchers = {}
for i in list_watchers:
    list_projects = []
    for data in data_sorted:
        if i in data['watchers']:
            list_projects.append(data['name'])
    dict_watchers[i] = list_projects

with open('watchers.json', 'w') as watchers_file:
    json.dump(dict_watchers, watchers_file, indent=4)
