from appconfig import *

if MODE_APP_PROD:
    GPIO.setmode(GPIO.BCM)

    # Set each zone pin as an intput and make it low:
    for pin in ZONES:
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    
    for pin in SYSTEM_IN:
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    
    # Set each out pin as an output and make it low:
    for pin in SYSTEM_IN:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)

    # set callbacks
    for pin in ZONES:
        GPIO.add_event_detect(pin, GPIO.BOTH, callback='callback_gpio', bouncetime=300)
    for pin in SYSTEM_IN:
        GPIO.add_event_detect(pin, GPIO.BOTH, callback='callback_gpio', bouncetime=300)
    for pin in SYSTEM_OUT:
        GPIO.add_event_detect(pin, GPIO.BOTH, callback='callback_gpio', bouncetime=300)

# CALLBACK FUNCTIONS
def callback_gpio(pin):
    get_gpio_state()

def get_gpio_state():
    for pin in ZONES:
        ZONES[pin]['gpio'] = GPIO.input(pin)
        set_zone_status_from_state(pin)
    for pin in SYSTEM_IN:
        SYSTEM_IN[pin]['gpio'] = GPIO.input(pin)
        set_input_status_from_state(pin)

def set_fake_data_for_debug():
    for pin in ZONES:
        set_zone_status_from_state(pin)
    for pin in SYSTEM_IN:
        set_input_status_from_state(pin)

def set_zone_status_from_state(ZONES):
    for pin in ZONES:
        # previous status unknown => status is DETECTING or OFF
        if ZONES[pin]['status'] == 'UNDEFINED':
            if ZONES[pin]['gpio'] == 1:
                ZONES[pin]['status'] = 'DETECTING'
            elif ZONES[pin]['gpio'] == 0:
                ZONES[pin]['status'] = 'OFF'
        # previous status was set
        else:
            if ZONES[pin]['gpio'] == 1:
                ZONES[pin]['status'] = 'DETECTING'
            elif ZONES[pin]['gpio'] == 0:
                if ZONES[pin]['status'] == 'DETECTING' or ZONES[pin]['status'] == 'DETECTED':
                    ZONES[pin]['status'] = 'DETECTED'
                else:
                    ZONES[pin]['status'] = 'OFF'
    print(ZONES)
    return(ZONES)
    
def set_input_status_from_state(pin):
    if SYSTEM_IN[pin]['gpio'] == 1:
        SYSTEM_IN[pin]['status'] = 'ON'
    else:
        SYSTEM_IN[pin]['status'] = 'OFF'

def set_gpio_power_alarm(action):
    if action == 'ON':
        GPIO.output(PIN_POWER_ALARM, GPIO.HIGH)
    elif action == 'OFF':
        GPIO.output(PIN_POWER_ALARM, GPIO.LOW)
