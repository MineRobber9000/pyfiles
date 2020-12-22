import sqlalchemy
from sqlalchemy.ext import declarative
import sqlalchemy.orm

def _include_module(obj,module):
	for key in module.__all__:
		if not hasattr(obj,key):
			setattr(obj,key,getattr(module,key))

class Database:
	"""A database."""
	def __init__(self,url="sqlite:///:memory:"):
		self.engine = sqlalchemy.create_engine(url)
		self.Model = self.make_base()
		self.Model.metadata.bind = self.engine
		self.session = sqlalchemy.orm.sessionmaker(bind=self.engine)()
		_include_module(self,sqlalchemy)
		_include_module(self,sqlalchemy.orm)
	def make_base(self):
		return declarative.declarative_base()
