
# SET APP MODE
MODE_APP_PROD = False
MODE_APP_TEST = True

if MODE_APP_PROD:
    import RPi.GPIO as GPIO
    from manage_gpio import *

#FSM_STATE = ['UNDEFINED', 'ON', 'OFF', 'ALARM']
#ZONE_STATE = ['UNDEFINED', 'OFF', 'DETECTING', 'DETECTED']

# GPIO PINS
PIN_POWER_ALARM = 20
PIN_READ_STATE = 21
PIN_ZONE1 = 23
PIN_ZONE2 = 24
PIN_ZONE3 = 25
PIN_ZONE4 = 26

#INPUTS
ZONES = {
   PIN_ZONE1 : {'name' : 'zone_1', 'gpio' : 0, 'status' : 'UNDEFINED'},
   PIN_ZONE2 : {'name' : 'zone_2', 'gpio' : 0, 'status' : 'UNDEFINED'},
   PIN_ZONE3 : {'name' : 'zone_3', 'gpio' : 0, 'status' : 'UNDEFINED'},
   PIN_ZONE4 : {'name' : 'zone_4', 'gpio' : 0, 'status' : 'UNDEFINED'}
   }

SYSTEM_IN = {
    PIN_READ_STATE : {'name' : 'system_out', 'gpio' : 0, 'status' : 'UNDEFINED'}
    }

#OUTPUTS
SYSTEM_OUT = {
    PIN_POWER_ALARM : {'name' : 'system_out', 'gpio' : 0, 'status' : 'UNDEFINED'}
    }

if MODE_APP_PROD:
    get_sates_from_gpio()
