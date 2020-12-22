import threading

class BFThread(threading.Thread):
	def __init__(self,prog):
		super(BFThread,self).__init__()
		self.prog=prog
		self.killswitch=threading.Event()
		self.stdout=""
	def run(self):
		prog=self.prog
		looptbl={}
		stack=[]
		for i,c in enumerate(prog):
			if c=="[": stack.append(i)
			if c=="]":
				t=stack.pop(-1)
				looptbl[t]=i
				looptbl[i]=t
		assert len(stack)==0
		del stack
		tape={}
		ptr=0
		i=0
		while i<len(prog) and (not self.killswitch.is_set()):
			c=prog[i]
			if c==">": ptr=(ptr-1)%30000
			if c=="<": ptr=(ptr+1)%30000
			if c=="+": tape[ptr]=(tape.get(ptr,0)+1)&0xFF
			if c=="-": tape[ptr]=(tape.get(ptr,0)-1)&0xFF
			if c=="[" and tape.get(ptr,0)==0: i=looptbl[i]
			if c=="]" and tape.get(ptr,0)!=0: i=looptbl[i]
			if c==".": self.stdout+=chr(tape.get(ptr,0))
			i+=1
		if not self.stdout:
			self.stdout="(pointer finished at {})".format(tape.get(ptr,0))
