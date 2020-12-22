import linebuffer,time

t = linebuffer.LineBuffer("Counting... (100/100)")
for i in range(100,0,-1):
	t.set("Counting... ({!s}/100)".format(i))
	time.sleep(0.5)
	t.draw()
t.set("Done!")
t.draw()
print()
