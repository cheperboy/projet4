import sqlite3, os.path
from datetime import datetime

DB_FILE = "database.db"
def init_db():
    if not os.path.isfile(DB_FILE):
        with sqlite3.connect(DB_FILE) as db:
            db.execute("""
                CREATE TABLE events (
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, 
                event_type TEXT, 
                event TEXT, 
                date TEXT)
            """)
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
        cursor.execute("""SELECT id, event_type, event, date FROM events""")
        events = cursor.fetchall()
        for event in events:
            print('{0} : {1} - {2} - {3}'.format(event[0], event[1], event[2], event[3]))
#            print(event['event'])
        return events
#    fsm_state = rows[0]['event']

#init_db()
#add_event("type", "ev name")
#get_events()
