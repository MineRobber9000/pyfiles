"""Assigned, Sealed, Delivered - A small library to catch regular object assignments.

ASD works on items that don't require execution of non-standard functions. For example:

dictionary = dict(python="a large heavy-bodied nonvenomous snake occurring throughout the Old World tropics, killing prey by constriction and asphyxiation.")
program_keys = {"python":"password"}

These work. These don't:

test = foo()
bar = baz()

ASD works by examining the Abstract Source Tree."""
import ast, astor

class GlobalsProxy:
	"""Allows for access to globals without polluting the global table."""
	def __init__(self):
		self.values={}
	def __getitem__(self,k):
		if k not in self.values:
			return globals()[k]
		return self.values[k]
	def __setitem__(self,k,v):
		self.values[k]=v
	def clear(self):
		self.values.clear()

def get_funcdef(value):
	return astor.to_source(ast.Module(body=[ast.FunctionDef(name='get_value', args=ast.arguments(args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]), body=[ast.Return(value=value)], decorator_list=[], returns=None)]))

def get_assignments(src):
	if type(src)!=ast.Module: src=ast.parse(src)
	ret = dict()
	gp = GlobalsProxy()
	for stmt in src.body:
		if type(stmt)==ast.Assign and len(stmt.targets)==1:
			name = stmt.targets[0].id
			gp.clear()
			funcdef = get_funcdef(stmt.value)
			exec(funcdef,globals(),gp.values)
			value=gp["get_value"]()
			ret[name]=value
	return ret
