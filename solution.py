from ast import *
from astor import to_source

#func_def_body = parse("def get_value():\n\treturn 'boi'").body[0]
#print(dump(func_def_body))

with open("coding_challenge.py") as f:
	tree = parse(f.read())

#src = "test = dict(key='Hello, world!')"
#tree = parse(src)
#print(dump(tree))

for statement in tree.body:
	if type(statement)==Assign and statement.targets[0].id=="d": # and type(statement.value)==Dict:
		func_def = FunctionDef(name='get_value', args=arguments(args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]), body=[Return(value=statement.value)], decorator_list=[], returns=None)
		fake_globals = globals()
		exec(to_source(Module(body=[func_def])),fake_globals)
		value = fake_globals["get_value"]()
#		print(", ".join([x.id for x in statement.targets]),"=",value)
#		if type(value)==dict and "key" in value:
#			print("Possible answer:",value["key"])
		print(value["key"])
