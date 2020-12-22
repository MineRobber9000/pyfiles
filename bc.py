from hashlib import sha256 as _hash
from time import time
import json

def hash(s):
	return _hash(bytearray(s,"utf-8")).hexdigest()

class JSONSerializable:
	def toDict(self):
		return self.__dict__
	def toJSON(self):
		return json.dumps(self.toDict(),indent=4)
	@classmethod
	def fromDict(cls,d):
		self = cls()
		self.__dict__.update(d)
	@classmethod
	def fromJSON(cls,d):
		return cls.fromDict(json.loads(d))
	def __str__(self):
		return json.dumps(self.toDict())
	def __repr__(self): return str(self)

class Block(JSONSerializable):
	def __init__(self,id=0,timestamp=0,payload=" ".strip(),prev_hash=hash("")):
		self.id=id
		self.timestamp=timestamp
		self.payload=payload
		self.prev_hash=prev_hash
	@property
	def hash(self):
		return hash(str(self.id)+str(self.timestamp)+str(self.payload)+str(self.prev_hash))
	SAVE_FIELDS = "id timestamp payload prev_hash hash".split()
	def toDict(self):
		ret = dict()
		for k in self.SAVE_FIELDS:
			ret[k]=getattr(self,k)
		return ret
	@classmethod
	def fromDict(self,d):
		o = self(0,0,0)
		for k in self.SAVE_FIELDS:
			if k=="hash": continue
			setattr(o,k,d[k])
		return o

class Chain(JSONSerializable):
	def __init__(self):
		self.blocks = []
	def add_genesis_block(self):
		self.blocks.append(Block(0,time(),{"type":"genesis_block"}))
	def add(self,payload):
		last_block = self.blocks[-1]
		self.blocks.append(Block(last_block.id+1,time(),payload,last_block.hash))
	def verify(self):
		for i in range(len(self.blocks)-1):
			b = self.blocks[i]
			if b.hash!=self.blocks[i+1].prev_hash:
				self.blocks=self.blocks[:i]
				return False
		return True
	def toDict(self):
		blocks = [b.toDict() for b in self.blocks]
		return dict(blocks=blocks)
	@classmethod
	def fromDict(cls,d):
		self = cls()
		self.blocks = [Block.fromDict(b) for b in d["blocks"]]
		return self
