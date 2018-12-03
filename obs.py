from random import randint as rand
from scr import *

# obs = [[' ' for x in range(110)] for y in range(110)]

# for i in range(40):
# 	for j in range(100):
# 		obs[i][j]=' '

class obstacle():

	def build(self):
		for j in range(110,450,rand(30,52)):
			sz=0
			for t in range(rand(5,15)):
				for i in range(18,21,2):
					gameArray[i][j+t]="="
					gameArray[19][j+t]="-"
				sz=t
			i=j+rand(10,15)+sz
			for t in range(rand(4,10)):
				gameArray[28][i+t]="="
				gameArray[29][i+t]="-"
		return gameArray

	#def fall(self,x):
	#	for i in (1,x+1):
			