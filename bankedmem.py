from py65emu import Block
from py65emu.mmu import ReadOnlyError
from py65emu.mmio import MMIORegister
from math import floor

class BankedMemory(Block):
	def __init__(self,start,banks,split=2):
		assert len(banks)>=split,"Cannot have less banks then memory splits"
		assert all(len(x)==len(banks[0]) for x in banks),"All banks must be same size"
		self.banks = banks
		self.inmem = [x for x in range(split)]
		self.banklength = len(self.banks[0])
		super(BankedMemory,self).__init__(start,self.banklength*len(self.inmem),True)
	def reset(self,force=False):
		return
	def _getIndex(self,addr):
		return super(BankedMemory,self).getIndex(addr)
	def getIndex(self,addr):
		index = self._getIndex(addr)
		page = floor(index / self.banklength)
		assert page<len(self.inmem),"Invalid access at address {} (no page {})".format(addr,page)
		index = index-(page*self.banklength)
		bank = self.inmem[page]
		return bank,index
	def read(self,addr):
		bank, index = self.getIndex(addr)
		return self.banks[bank][index]
	def write(self,addr,val):
		if self.readonly: raise ReadOnlyError()
		bank, index = self.getIndex(addr)
		self.banks[bank][index]=val&0xFF
	def swapBank(self,page,bank):
		assert page<len(self.inmem),"No page {}".format(page)
		assert bank<len(self.banks),"No bank {}".format(bank)
		self.inmem[page]=bank

class BankSwapRegister(MMIORegister):
	def __init__(self,block,page):
		assert page<len(block.inmem),"No page {} of block {!r}".format(page,block)
		self.block=block
		self.page=page
	def read(self):
		return self.block.inmem[self.page]
	def write(self,val):
		self.block.swapBank(self.page,val)

def setup_banks(start,banks,split=2):
	retblock = BankedMemory(start,banks,split)
	mmio = [BankSwapRegister(retblock,x) for x in range(split)]
	return retblock, mmio
