# manage data
from storage_file import *
from storage_cache import *
from appconfig import *

STORAGE_TYPE = 'cache'

def get_toto():
    toto = cache.get('toto')
    if toto is None:
        cache.set('toto', 'toto_init', timeout=5 * 60)
        toto = cache.get('toto')
    return toto

def set_toto(val):
    cache.set('toto', val, timeout=5 * 60)

def init_data():
    if STORAGE_TYPE is 'file':
        init_data_file()
    elif STORAGE_TYPE is 'cache':
        init_data_cache()

def get_zone():
    if STORAGE_TYPE is 'file':
        return(get_zone_from_file())
    elif STORAGE_TYPE is 'cache':
        return(get_zone_from_cache())

def get_system():
    if STORAGE_TYPE is 'file':
        return get_system_from_file()
    elif STORAGE_TYPE is 'cache':
        return get_system_from_cache()

def save_system(system):
    if STORAGE_TYPE is 'file':
        save_system_to_file(system)
    elif STORAGE_TYPE is 'cache':
        save_system_to_cache(system)

def save_zone(zones):
    if STORAGE_TYPE is 'file':
        save_zone_to_file(zones)
    elif STORAGE_TYPE is 'cache':
        save_zone_to_cache(zones)

def set_system_state(action):
    set_toto(action)
    data = get_system()
    if action == 'ON':
        data[str(PIN_READ_STATE)]['gpio'] = 1
        data[str(PIN_READ_STATE)]['status'] = 'ON'
    elif action == 'OFF':
        data[str(PIN_READ_STATE)]['gpio'] = 0
        data[str(PIN_READ_STATE)]['status'] = 'OFF'
    save_system(data)

