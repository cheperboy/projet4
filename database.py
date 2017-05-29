import sqlite3, os.path
from datetime import datetime

DB_FILE = "database.db"
def init_db():
    if not os.path.isfile(DB_FILE):
        with sqlite3.connect(DB_FILE) as db:
            db.execute("CREATE TABLE events (eid INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, event_type TEXT, event TEXT, date TEXT)")
            print 'Table created successfully';
            db.commit()

def add_event(event_type, event):
    with sqlite3.connect(DB_FILE) as db:
        cursor = db.cursor()
        cursor.execute("INSERT INTO events (event_type, event, date) VALUES (?,?,?)",(event_type, event, datetime.now()))
        db.commit()
        print "Record Added created successfully"

def get_events():
    with sqlite3.connect(DB_FILE) as db:
        cursor = db.cursor()
        cursor.execute("SELECT eid, event_type, event, date FROM events")
        events = cursor.fetchall()
        #print(events)
        datas = dict()
        for event in events:
            datetemp = datetime.strptime(event[3], "%Y-%m-%d %H:%M:%S.%f") #parse string as a datetime format
            date = datetemp.strftime("%d/%m/%Y %H:%M")
            temp = {'name' : event[2], 'date' : date}
            datas.update({event[0] : temp})
        #for key,val in datas.items(): print key, "=>", val.get('name'), "/", val.get('date')
        #for event in datas: print(datas[event].get('name'))
        return(datas)

def save_get_events():
    with sqlite3.connect(DB_FILE) as db:
        cursor = db.cursor()
        cursor.execute("SELECT id, event_type, event, date FROM events")
        events = cursor.fetchall()
        print(events)
        eventts = []
        for event in events:
            eventt = [4]
            eventt[0] = event[0]
            eventts.append(eventt)
        for event in eventts:
            event = list(event)
            date = datetime.strptime(event[3], "%Y-%m-%d %H:%M:%S.%f") #parse string as a datetime format
            event[3] = date.strftime("%Y-%m-%d %H")
            print('{0} : {1} - {2} - {3}'.format(event[0], event[1], event[2], event[3]))
        for event in events:
            print('{0} : {1} - {2} - {3}'.format(event[0], event[1], event[2], event[3]))
        return events

#init_db()
#add_event("type", "ev name")
#add_event("toto", "titi")
get_events()
