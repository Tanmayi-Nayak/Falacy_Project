import json

def save_json(data):

    with open(
        "data/processed/output.json",
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            indent=4
        )