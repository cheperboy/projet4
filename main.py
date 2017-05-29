#PROJET 4

from flask import *
from manage_data import *
from appconfig import *
from manage_gpio import *
from database import *
from datetime import datetime

app = Flask(__name__)

init_data()
init_db()

def update_zones(ZONES):
    ZONES = get_zone()
    ZONES = set_zone_status_from_state(ZONES)
    save_zone(ZONES)
    return(ZONES)
    
@app.route("/")
@app.route("/index")
def main():
    global ZONES
    global PIN_READ_STATE
    global SYSTEM_IN

    if MODE_APP_PROD:
        get_gpio_state()
        system_state = SYSTEM_IN[str(PIN_READ_STATE)]['status']

    if MODE_APP_TEST:
        events = get_events()
        ZONES = update_zones(ZONES)
        SYSTEM_IN = get_system()
        system_state = SYSTEM_IN[str(PIN_READ_STATE)]['status']

    templateData = {
      'zones' : ZONES,
      'system_state' : system_state,
      'system' : SYSTEM_IN,
      'events' : events
    }
    return render_template('index.html', **templateData)


@app.route('/SetSystem', methods=['POST'])
def SetSystem():
    global ZONES
    action = request.form['btnAction'];    
    if MODE_APP_TEST:
        set_system_state(action)

    if MODE_APP_PROD:
        set_gpio_power_alarm(action)
        sleep(150)
        get_gpio_state()
        system_state = SYSTEM_IN[str(PIN_READ_STATE)]['status']
            
    return json.dumps({'status':'OK'});

if __name__ == "__main__":
   app.run(host="0.0.0.0", debug=True)
