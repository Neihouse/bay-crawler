import json

def load_settings():
    with open('config.json', 'r') as config_file:
        settings = json.load(config_file)
    return settings