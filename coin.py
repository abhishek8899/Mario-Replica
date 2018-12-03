from random import randint as rand
from scr import *

# obs = [[' ' for x in range(110)] for y in range(110)]

# for i in range(40):
# 	for j in range(100):
# 		obs[i][j]=' '

class coins():

	def build(self):
		for i in range(80,440,30):
			k=rand(12,27)
			p=rand(-1,1)
			if p==0:
				p=-1
			if(gameArray[k][i]=='=' or gameArray[k][i]=='-'):
				gameArray[k+p*3][i]='O'
			else:
				gameArray[k][i]='O'
		return gameArray

	#def fall(self,x):
	#	for i in (1,x+1):
			
