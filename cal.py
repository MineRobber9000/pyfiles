import requests, ics, sys
from datetime import datetime

NOW = datetime.utcnow()

_, url = sys.argv
r = requests.get(url)
r.raise_for_status()
cal = ics.Calendar(r.text)

for event in cal.timeline:
	if event.begin.naive>NOW: print(event.begin.strftime("%Y-%m-%dT%H:%M:%S"),event.name)
