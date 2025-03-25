import schedule
import time
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
import json

# Load events from events.json
with open('calendar_reminder/events.json', 'r') as f:
    events = json.load(f)

def send_reminder(event):
    msg = MIMEText(f"Reminder: {event['description']} - File: {event['file']}")
    msg['Subject'] = f"Reminder for {event['description']}"
    msg['From'] = "your_email@example.com"
    msg['To'] = "your_email@example.com"

    with smtplib.SMTP("smtp.example.com") as server:
        server.login("your_email@example.com", "password")
        server.sendmail(msg['From'], [msg['To']], msg.as_string())

def schedule_events():
    for event in events:
        event_time = f"{event['date']} {event['time']}"
        schedule_time = datetime.strptime(event_time, "%Y-%m-%d %H:%M")
        schedule.every().day.at(schedule_time.strftime("%H:%M")).do(send_reminder, event=event)

if __name__ == "__main__":
    schedule_events()
    while True:
        schedule.run_pending()
        time.sleep(1)
