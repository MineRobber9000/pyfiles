from flask import *

f = Flask(__name__)

@f.route("/post",methods=["POST"])
def post():
	return str(request.headers["Content-Length"]),200
