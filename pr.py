import math

def points(wins,losses,points_for,points_against,yards_for,yards_against,prestige=70,offTalent=70,defTalent=70,week=0,sov=42,cc=False,nc=False):
	n = 8-week
	if n<0: n=0
	score = (wins*200 + (points_for-points_against)*3 + (yards_for-yards_against)/40 + n*3*(prestige+offTalent+defTalent) + sov)/10
	score = math.floor(score)
	score+=30 if cc else 0
	score+=100 if nc else 0
	score+=50 if losses==0 else (20 if losses==1 else 0)
	return score
