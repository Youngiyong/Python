import json

with open('./data/temp.json', 'r', encoding='utf-8') as f:
    data = f.read()
    print(data)
    print(type(data)) # str

    print('='*50)

    items = json.loads(data)
    print(items)
    print(type(items))

    for item in items:
        print(item, items[item].get('No'), items[item]['Job'] )

    for item in items:  # 딕셔너리는 키를갖고온다
        print(item, items[item]['No'], items[item]['Job'])

    for item, values in items.items():
        for i, v in values.items():
            print(i, v)