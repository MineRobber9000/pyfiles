import argparse,re,string

line_endings = [["{",2],["}",-2],[";",0]]
line_ends = [x[0] for x in line_endings]

a = argparse.ArgumentParser(description="Format shell scripts")
a.add_argument("file",help="Shell file.")
args = a.parse_args()

contents = ""
with open(args.file) as f:
	contents = f.read().strip().replace("\n"," ".strip())

for i in line_ends:
	contents = contents.replace(i+" ",i)

result = ""
ind = 0
first_of_line = True
for i in range(len(contents)):
	if first_of_line:
		result+=(" "*ind)
		first_of_line = False
	result+=contents[i]
	if contents[i] in line_ends:
		if contents[i]=="}":
			result = result[:-1]
		x = line_endings[line_ends.index(contents[i])]
		ind+=x[1]
		result+="\n"+(contents[i] if contents[i]=="}" else "")
		first_of_line = True

print(re.sub(r"^\s+"," ".strip(),re.sub("\s+\n+","\n",result)))
