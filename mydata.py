import json, os.path
from appconfig import *

DATA_JSON_FILE_ZONES = 'zones.json'
DATA_JSON_FILE_SYSTEM = 'system.json'

def init_data():
    global ZONES
    global SYSTEM_IN
    print('init_data')
    print(ZONES)
    if not os.path.isfile(DATA_JSON_FILE_ZONES):
        save_zone_to_file(ZONES)
    if not os.path.isfile(DATA_JSON_FILE_SYSTEM):
        save_system_to_file(SYSTEM_IN)

def get_zone_state_from_file():
    with open(DATA_JSON_FILE_ZONES, 'r') as f:
         data = json.load(f)
    return data

def get_system_state_from_file():
    with open(DATA_JSON_FILE_SYSTEM, 'r') as f:
         data = json.load(f)
    return data

def save_zone_to_file(zones):
    with open(DATA_JSON_FILE_ZONES, 'w') as f:
        json.dump(zones, f)

def save_system_to_file(system):
    with open(DATA_JSON_FILE_SYSTEM, 'w') as f:
        json.dump(system, f)

def set_system_state(action):
    data = get_system_state_from_file()
    if action == 'ON':
        data[str(PIN_READ_STATE)]['gpio'] = 1
        data[str(PIN_READ_STATE)]['status'] = 'ON'
    elif action == 'OFF':
        data[str(PIN_READ_STATE)]['gpio'] = 0
        data[str(PIN_READ_STATE)]['status'] = 'OFF'
    save_system_to_file(data)
