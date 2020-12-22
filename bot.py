import teambot

class BotHandler(teambot.Handler):
	def on_connection_established(self,conn,event):
		print("CONNECTED")
	def on_pubmsg(self,channel,nick,text):
		print(channel,nick,text)
	def on_privmsg(self,nick,text):
		print("[PRIVMSG]",nick,text)

if __name__=="__main__":
	channels = "#khuxkm".split()
	bot = teambot.TeamBot(channels,"logtest","localhost",chandler=BotHandler)
	bot.start()
