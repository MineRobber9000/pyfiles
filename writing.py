import requests, ics
from datetime import datetime

NOW = datetime.utcnow()

r = requests.get("https://trello.com/calendar/5acfe57ab43c4b0e67b2e610/5e9de8e3a73a0507805c867a/81b2d227b6ca577dfabe95e3a1f12225.ics")
r.raise_for_status()
cal = ics.Calendar(r.text)

for event in cal.timeline:
	if event.begin.naive>NOW: print(event.begin.strftime("%Y-%m-%d"),event.name)
