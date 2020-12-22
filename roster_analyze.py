from khutils import html, csv
from collections import defaultdict
import time
average = lambda l: sum(l)/len(l)

# Position average overrides
# Set to None to avoid collecting heights and weights
positions = dict(
	P="K", # punters are kickers too
	LS=None, # no long snapper position in FC2
	CB="DB", # lump CB and S into DB group
	S="DB",
	C="OL", # lump C, G, T into offensive line
	G="OL",
	T="OL",
	DE="DL", # DE, DT, NT are defensive linemen
	DT="DL",
	NT="DL",
	FB="RB" # FC2 has no FB position, but count them as running backs
)

heights = defaultdict(list)
weights = defaultdict(list)

def process_roster(soup):
	global heights, weights
	for table in soup.findAll("table"):
		for row in table.findAll("tr"):
			info = []
			for data in row.findAll("td"):
				info.append(data.text.strip())
			if not info: continue
			num, name, pos, height, weight = info[:5]
			if positions.get(pos,pos) is None: continue
			name = name.splitlines()[0].strip()
			print("{} #{} - {} ({}, {}lbs)".format(pos,num,name,height,weight))
			parts = height.split("-")
			if len(parts)!=2: continue
			feet, inches = parts
			heights[positions.get(pos,pos)].append(int(feet)*12 + int(inches))
			heights[positions.get(pos,pos)].sort()
			try:
				weights[positions.get(pos,pos)].append(int(weight))
				weights[positions.get(pos,pos)].sort()
			except: pass

with open("rosters.txt") as f: rosters = [l.strip() for l in f if l.strip()]

for roster in rosters:
	try:
		process_roster(html.get_html(roster))
		time.sleep(5)
	except: pass

def process_dict(d,n,f):
	for k in d:
		# min
		mi = min(d[k])
		# max
		ma = max(d[k])
		# mean (average)
		me = average(d[k])
		# median
		md = d[k][len(d[k])//2]
		# mode
		mo = max(d[k][::-1],key=d[k].count)
		f.write("{} of {}\n".format(n,k))
		f.write("-------------\n")
		f.write("Min: {}\n".format(mi))
		f.write("Mean: {}\n".format(me))
		f.write("Median: {}\n".format(md))
		f.write("Mode: {}\n".format(mo))
		f.write("Max: {}\n".format(ma))
		f.write("-------------\n")

with open("pos_heights.txt","w") as f:
	process_dict(heights,"Height",f)
with open("pos_weights.txt","w") as f:
	process_dict(weights,"Weight",f)

csv.dump_to_file("heights.csv",[[pos]+heights[pos] for pos in heights])
csv.dump_to_file("weights.csv",[[pos]+weights[pos] for pos in weights])
