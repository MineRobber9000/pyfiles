import sqla, totp, base64

db = sqla.Database("sqlite:///auth.sqlite")

class Account(db.Model):
	__tablename__="accounts"
	id=db.Column(db.Integer,primary_key=True)
	label=db.Column(db.String)
	secret=db.Column(db.Binary)
	issuer=db.Column(db.String)
	counter=db.Column(db.Integer)

db.Model.metadata.create_all()

def add_account(label,secret,issuer="unknown",counter=-1):
	if type(secret)!=bytes: secret=base64.b32decode(secret+(type(secret)("=")*(8-(len(secret)%8) if (len(secret)%8)!=0 else 0)))
	if label.startswith(issuer+":"): label=label[len(issuer)+1:].strip()
	acc = Account(label=label,secret=secret,issuer=issuer,counter=-1)
	db.session.add(acc)
	db.session.commit()

def get_accounts():
	accounts = db.session.query(Account).all()
	ret = []
	for account in accounts:
		r = {}
		r["label"]=account.label
		r["issuer"]=account.issuer
		if account.counter==-1:
			r["passcode"]=lambda: totp.totp(account.secret)
		else:
			def passcode():
				ret = totp.hotp(account.secret,account.counter)
				account.counter+=1
				db.session.commit()
				return ret
			r["passcode"]=passcode
		ret.append(r)
	return ret
