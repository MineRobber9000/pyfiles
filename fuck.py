import ast

class _Fucker(ast.NodeTransformer):
	def generic_visit(self,node):
		ast.NodeTransformer.generic_visit(self,node)
		if isinstance(node,ast.stmt) and not isinstance(node,ast.FunctionDef):
			new_node = ast.Try(body=[node],handlers=[ast.copy_location(ast.ExceptHandler(type=None,name=None,body=[ast.copy_location(ast.Pass(),node)]),node)],orelse=[],finalbody=[ast.copy_location(ast.Pass(),node)])
			return ast.copy_location(new_node,node)
		return node

def it(code):
	parsed = ast.parse(code)
	parsed = _Fucker().visit(parsed)
	exec(compile(parsed,"<string>","exec"))
