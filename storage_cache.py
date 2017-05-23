from appconfig import *
import json

from werkzeug.contrib.cache import SimpleCache
cache = SimpleCache()


DATA_JSON_FILE_ZONES = 'zones.json'
DATA_JSON_FILE_SYSTEM = 'system.json'

def init_data_cache():
    global ZONES
    global SYSTEM_IN
    zones = cache.get('zones')
    if zones is None:
        cache.set('zones', json.dumps(ZONES), timeout=5 * 60)

    system = cache.get('system')
    if system is None:
        cache.set('system', json.dumps(SYSTEM_IN), timeout=5 * 60)

def get_zone_from_cache():
    zones = cache.get('zones')
    if zones is None:
        init_data_cache()
        zones = cache.get('zones')
    return json.loads(zones)

def get_system_from_cache():
    system = cache.get('system')
    if system is None:
        init_data_cache()
        system = cache.get('system')
    return json.loads(system)

def save_zone_to_cache(zones):
    cache.set('zones', json.dumps(zones), timeout=5 * 60)

def save_system_to_cache(system):
    cache.set('system', json.dumps(system), timeout=5 * 60)
