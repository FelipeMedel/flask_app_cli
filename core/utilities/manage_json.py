import json
import os


def read_json(path: str):
    if not os.path.isfile(path):
        with open(path, 'w') as f:
            json.dump({}, f)
    with open(path, 'r', encoding="utf-8") as f:
        return json.load(f)


def write_json(path: str, data: dict):
    with open(path, 'w', encoding="utf-8") as f:
        str(data).encode('utf-8')
        json.dump(data, f, indent=4, ensure_ascii=False)
