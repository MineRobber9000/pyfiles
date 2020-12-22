import inspect

def calling_scope_var(name):
	frame = inspect.stack()[1][0]
	while True:
		if name in frame.f_locals:
			return frame.f_locals[name]
		if name in frame.f_globals:
			return frame.f_globals[name]
		frame=frame.f_back
		if frame is None:
			raise NameError("name {!r} is not defined".format(name))

def __recursive_get(obj,*specs):
	if len(specs)==1:
		return getattr(obj,specs[0])
	return __recursive_get(getattr(obj,specs[0]),*(specs[1:]))

def __recursive_set(obj,val,*specs):
	print(specs)
	if len(specs)==1:
		setattr(obj,specs[0],val)
		return
	__recursive_set(getattr(obj,specs[0]),val,*(specs[1:]))

def get(spec):
	specs = spec.split(".")
	return __recursive_get(calling_scope_var(specs.pop(0)),*specs)

def set(spec,val):
	specs = spec.split(".")
	return __recursive_set(calling_scope_var(specs.pop(0)),val,*specs)

