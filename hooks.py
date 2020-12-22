from functools import update_wrapper

INTROSPECT=False

try:
	import introspect
	INTROSPECT=True
except:
	pass

class HookedFunction:
	def __init__(self,func):
		update_wrapper(self,func)
		self.__function__ = func
		self.__pre_hooks__ = []
		self.__post_hooks__ = []
	def __call__(self,*args,**kwargs):
		for f in self.__pre_hooks__:
			args, kwargs = f(self.__function__,args,kwargs)
		ret = self.__function__(*args,**kwargs)
		for f in self.__post_hooks__:
			rv = f(self.__function__,args,kwargs,ret)
			if rv is not None:
				ret = rv
		return ret
	def add_hook(self,func,pre=False):
		if pre:
			self.__pre_hooks__.append(func)
		else:
			self.__post_hooks__.append(func)
	def clear_hooks(self):
		self.__pre_hooks__ = []
		self.__post_hooks__ = []
	def hook(self,pre=False):
		def _add_hook(func):
			self.add_hook(func,pre)
		return _add_hook

def hooked(func):
	return HookedFunction(func)

class ModuleNotFoundError(Exception):
	def __init__(self,module):
		super(ModuleNotFoundError,self).__init__("Unable to load module {!r}.".format(module))

def hook(spec):
	if not INTROSPECT: raise ModuleNotFoundError("introspect")
	f = introspect.get(spec)
	if type(f)!=type(hooked):
		raise Exception("Unable to hook non-function {!r}".format(spec))
	introspect.set(spec,HookedFunction(f))
