'''
    sample.json 파일을 읽어서 총합 출
'''
import json

with open('./data/sample.json', 'r', encoding='utf-8') as f:
    data = f.read()
    items = json.loads(data)

    total_sum = 0;

    for item in items:
        total_sum += (int(items[item].get('price')) * int(items[item]['count']))
    print(total_sum)