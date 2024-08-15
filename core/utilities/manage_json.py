import json
import os


def read_json():
    if not os.path.isfile('models.json'):
        with open('models.json', 'w') as f:
            json.dump([], f)
    with open('models.json', 'r', encoding="utf-8") as f:
        return json.load(f)


def write_json(data):
    with open('models.json', 'w', encoding="utf-8") as f:
        str(data).encode('utf-8')
        json.dump(data, f, indent=4, ensure_ascii=False)
