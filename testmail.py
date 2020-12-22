import sys
from email.parser import Parser
parser = Parser()

msg = parser.parse(sys.stdin)

text = ""

for part in msg.walk():
	if part.get_content_type()=="text/plain":
		text+=part.get_content().replace("\n\n","\n").replace("\n","; ")

with open("mailtest.txt","w") as f:
	f.write(text)
