# Shitdown - A shitty markdown parser
# By Robert "khuxkm" Miles, khuxkm@tilde.team

import re

def header_render(match):
	tag = "h"+str(match.group(1).count("#"))
	return "<{0}>{1}</{0}>".format(tag,match.group(2))

class Keys:
	HEADER = r"(#{1,6}) (.+)"
	HEADER_F = header_render
	@classmethod
	def get(self,name):
		return re.compile(getattr(self,name.upper()))
	@classmethod
	def get_render(self,name):
		return getattr(self,name.upper()+"_F")

class Passage:
	def __init__(self,lines=["# Shitdown example text"," ".strip(),"This is a test."]):
		self.lines = lines
		self.process()
	def process(self):
		tokens = []
		for line in self.lines:
			tokens.append(self.process_line(line))
		self.tokens = tokens
		text = "\n".join(tokens)
		self.out = text
	def process_line(self,line):
		for key in "header".split():
			m = Keys.get(key).search(line)
			if m is not None:
				return Keys.get_render(key)(m)
		return line
