import json


path = 'info.json'

with open(path, 'r', encoding='utf8') as file:
    json_str = file.read()
    dictData = json.loads(json_str)
    print(dictData)
    print(dictData['hobbies'])
    lst_hob = dictData['hobbies']
    print(lst_hob)
    print(len(lst_hob))

