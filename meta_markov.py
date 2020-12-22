import markovify, re

URL = re.compile(r"((?:https?|gopher)://[^\s/?.#].[^\s]*)")
NICK_MENTION = re.compile(r"[A-Za-z0-9]+\:")
MULTI_SPACE = re.compile("\s+")

with open("meta.log") as f:
	corpus = list(filter(None,[MULTI_SPACE.sub(' ',NICK_MENTION.sub("",URL.sub('',l.strip()))) for l in f if not "bot>" in l or not "bot2>" in l]))
	corpus = list(filter(None,map(lambda s: s.split("> ",1)[1] if "> " in s else None,corpus)))

model = markovify.NewlineText("\n".join(corpus))

s=model.make_sentence()
while not s: s=model.make_sentence()

print(s)
