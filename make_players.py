import libthings, random
from khutils import csv

override = dict(CB="DB",S="DB")

poscount = csv.load_from_file("poscount.csv")
poscount.pop(0)

hguass = {x[0]: [float(y) for y in x[1:]] for x in csv.load_from_file("heights.normal.csv")}
wguass = {x[0]: [float(y) for y in x[1:]] for x in csv.load_from_file("weights.normal.csv")}

def get_name():
	return libthings.dude()[0]

out = []
for pos, count in poscount:
	for i in range(int(count)):
		name=get_name()
		year=random.choice("Fr Fr Jr".split())
		height=int(round(random.gauss(*hguass[override.get(pos,pos)])))
		weight=int(round(random.gauss(*wguass[override.get(pos,pos)])))
		out.append(["PLAYER","DVSU",pos,name,year,height,weight,"1"])

csv.dump_to_file("players.csv",out)
