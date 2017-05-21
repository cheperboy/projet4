import sqlite3
#FSM_STATE = ['UNDEFINED', 'ON', 'OFF', 'ALARM', 'ACK']
#ZONE_STATE = ['UNDEFINED', 'OFF', 'DETECTING', 'DETECTED', 'ACK']

def init_db():
    db = sqlite3.connect('database.db')
    print "Opened database successfully";

    db.execute('CREATE TABLE STATE (fsm_state TEXT, zone1_state TEXT, zone2_state TEXT)')
    print 'Table created successfully';

    cur = db.cursor()

    fsm_state = 'UNDEFINED'
    zone1_state = 'UNDEFINED'
    zone2_state = 'UNDEFINED'

    cur.execute("INSERT INTO STATE (fsm_state,zone1_state,zone2_state) VALUES (?,?,?)",(fsm_state,zone1_state,zone2_state) )            
    db.commit()

    print "Record created successfully";

    db.close()

def get_fsm_state_state():
    db = sqlite3.connect('database.db')
    db.row_factory = sqlite3.Row
    cur = db.cursor()
    cur.execute("select * from STATE")
    rows = cur.fetchall()

    fsm_state = rows[0]['fsm_state']
    
    print "fsm_state="+fsm_state
    return fsm_state
    
def set_fsm_state_state():
    db = sqlite3.connect('database.db')
    db.row_factory = sqlite3.Row
    cur = db.cursor()
    cur.execute("select * from STATE")
    rows = cur.fetchall()
    cur.execute("UPDATE STATE SET fsm_state = ?", "toto")

    print "updated fsm_state="+fsm_state
    
init_db()
get_fsm_state_state()
set_fsm_state_state()
get_fsm_state_state()
