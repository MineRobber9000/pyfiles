import time,timer

def say_hi(state):
	if not hasattr(state,"first"):
		state.first=True
		return
	print("Hi from timer!")

t = timer.Timer()
t.add_task(say_hi,1)

start_time = time.monotonic()
t.start()
while (time.monotonic()-start_time)<=30: pass
t.stop()
while t.thread.is_alive(): pass
