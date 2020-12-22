import sys
from ast import *

module=Module(body=[FunctionDef(name='square',args=arguments(args=[arg(arg='x',annotation=None,lineno=1,col_offset=1)],vararg=None,kwonlyargs=[],kw_defaults=[],kwarg=None,defaults=[],lineno=1),body=[Return(value=BinOp(left=Name(id='x',ctx=Load(),lineno=1,col_offset=1),op=Pow(),right=Num(n=2,lineno=1,col_offset=1),lineno=1,col_offset=1),lineno=1,col_offset=1)],decorator_list=[],returns=None,lineno=1,col_offset=1)])
modobj=type(sys)(__name__)
exec(compile(module,"<ast>","exec"),None,modobj.__dict__)
sys.modules[__name__]=modobj
