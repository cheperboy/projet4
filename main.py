#PROJET 4

from flask import *
from mydata import *
from appconfig import *
from manage_gpio import *
app = Flask(__name__)

init_data()

@app.route("/")
@app.route("/index")
def main():
    global ZONES
    global PIN_READ_STATE
    global SYSTEM_IN

    if MODE_APP_PROD:
        get_gpio_state()
        system_state = SYSTEM_IN[PIN_READ_STATE]['status']

    if MODE_APP_TEST:
        ZONES = get_zone_state_from_file()
        ZONES = set_zone_status_from_state(ZONES)
        save_zone_to_file(ZONES)
        
        SYSTEM_IN = get_system_state_from_file()
        system_state = SYSTEM_IN[str(PIN_READ_STATE)]['status']
         
    templateData = {
      'zones' : ZONES,
      'system_state' : system_state
    }
    return render_template('index.html', **templateData)


@app.route('/SetSystem', methods=['POST'])
def SetSystem():
    action = request.form['btnAction'];    
    if MODE_APP_TEST:
        set_system_state(action)
        system_state = SYSTEM_IN[PIN_READ_STATE]['status']
        ZONES = get_zone_state_from_file()
        ZONES = set_fake_data_for_debug(ZONES)
        save_zone_to_file(ZONES)

    if MODE_APP_PROD:
        set_gpio_power_alarm(action)
        sleep(150)
        get_gpio_state()        
        system_state = SYSTEM_IN[PIN_READ_STATE]['status']
            
    return json.dumps({'status':'OK','system_state':system_state});

if __name__ == "__main__":
   app.run(host="0.0.0.0", debug=True)
