"""Helper library for hand-writing AST nodes and executing them. Uses astor and ast to allow for easy hand-writing of AST."""
from astor import to_source
from ast import *
from ast import Module as _Module
from builtins import compile as _compile

def is_sequence(x):
	"""Algorithmically determines if x is a sequence."""
	try:
		len(x)
		x[0:0]
		return True
	except:
		return False

def Module(*args,**kwargs):
	"""Helper function to allow for easy initiation of a Module."""
	if len(args)==1 and is_sequence(args[0]): # Module([FunctionDef,Stmt])
		return _Module(list(args[0]))
	elif "body" in kwargs: # Module(body=[FunctionDef,Stmt])
		return _Module(kwargs["body"])
	else: # Module(FunctionDef,Stmt)
		return _Module(args)

def compile(tree,mode,flags=0):
	"""Compiles a tree to a code object. It works by using astor to convert the AST to code, and then compiling the code."""
	src = to_source(tree)
	return _compile(src,"<ast>",mode,flags=flags)
