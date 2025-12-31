import json
a = {"Name":"Venkat","Age":22}

b = json.dumps(a)
with open('data.json','r') as file:
    data = json.load(file)
print(json.dumps(data,indent=2))
