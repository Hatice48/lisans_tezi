import requests

import flask

from flask import Flask,render_template
from gcsa.google_calendar import GoogleCalendar

app = Flask(__name__)

def get_google_calendar_events():
    calendar = GoogleCalendar('hatice.yslv36@gmail.com')
    events = [event for event in calendar]
    return events

@app.route('/')
def index():
    events = get_google_calendar_events()
    return render_template('index.html', events=events)

if __name__=='__main__':
    app.run(debug=True)

# Uygulama çalıştığında etkinlikleri konsola yazdırmak için:
events = get_google_calendar_events()
for event in events:
    print(event)
