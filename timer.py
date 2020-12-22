import sched, threading, string

ALPHABET = string.ascii_letters+string.digits

def base(id):
	if id<len(ALPHABET):
		return ALPHABET[id]
	q,r = divmod(id,len(ALPHABET))
	return base(q-1)+ALPHABET[r]

class TimerState:
	def __init__(self): pass
	def __contains__(self,k): return hasattr(self,k)
	def __getitem__(self,k):
		if k in self: return getattr(self,k)
		raise KeyError(k)
	def __setitem__(self,k,v): return setattr(self,k,v)

class Timer:
	def __init__(self):
		self.scheduler = sched.scheduler()
		self.event = threading.Event()
		self.thread = threading.Thread(target=self.run)
		self.thread.daemon=True
		self.states = dict()
		self.tasks = dict()
		self.state_class = TimerState
	def add_task(self,func,interval,state=dict(),name=None):
		if name is None:
			i=0
			while base(i) in self.tasks: i+=1
			name=base(i)
		self.tasks[name]=[func,interval]
		sto = None
		if type(state)==dict and len(state.keys())>1:
			sto = self.state_class()
			for k in state.keys(): setattr(sto,k,state[k])
		elif type(state)==self.state_class:
			sto = state
		if sto is not None: self.states[name]=sto
	def runner(self,name):
		func, interval = self.tasks[name]
		state = self.states.get(name,self.state_class())
		s=func(state)
		if s is not None: state=s
		self.states[name]=state
		if not self.event.is_set(): self.scheduler.enter(interval,1,self.runner,argument=(name,))
	def run(self):
		for k in self.tasks:
			self.scheduler.enterabs(0,1,self.runner,argument=(k,))
		self.scheduler.run()
	def start(self):
		if self.thread.is_alive(): return
		self.thread.start()
	def stop(self):
		list(map(self.scheduler.cancel,self.scheduler.queue))
		self.event.set()
