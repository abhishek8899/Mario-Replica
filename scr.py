from random import randint as rand
from os import system

gameArray = [[' ' for x in range(1110)] for y in range(40)]

for i in range(1005):
	gameArray[30][i]='='

class Board():

	def gameBoard(self):
		for j in range(0,1005):
			for i in range(1):
				r=rand(1,110)
				if r<25:
					gameArray[r][j]="."

		for j in range(15,1005,30):
			k=rand(1,8)
			gameArray[k][j]='('
			gameArray[k-1][j+1]='_'
			gameArray[k-1][j+2]='_'
			gameArray[k][j+3]=')'
			gameArray[k][j+4]='_'
			gameArray[k][j+5]='('
			gameArray[k-1][j+6]='_'
			gameArray[k][j+7]=')'
			gameArray[k][j+8]='_'
			gameArray[k+1][j-1]='('
			gameArray[k+1][j]='_'
			gameArray[k+1][j+3]='_'
			gameArray[k+1][j+8]='_'
			gameArray[k+1][j+9]=')'
			gameArray[k+2][j]='('
			gameArray[k+2][j+1]='_'
			gameArray[k+2][j+2]=')'
			gameArray[k+2][j+4]='('
			gameArray[k+2][j+5]='_'
			gameArray[k+2][j+6]='_'
			gameArray[k+2][j+7]=')'
		tmp=465
		gameArray[10][495]=','
		gameArray[10][30]=','
		for j in range(11,30):
			gameArray[j][495]='|'
			gameArray[j][30]='|'
		gameArray[11][494]='/'
		gameArray[12][493]='/'
		gameArray[13][492]='/'
		gameArray[14][491]='/'
		gameArray[15][490]='/'
		gameArray[15][491]='_'
		gameArray[15][492]='_'
		gameArray[15][493]='_'
		gameArray[15][494]='_'

		gameArray[11][496-tmp]='\\'
		gameArray[12][497-tmp]='\\'
		gameArray[13][498-tmp]='\\'
		gameArray[14][499-tmp]='\\'
		gameArray[15][500-tmp]='\\'
		gameArray[15][499-tmp]='_'
		gameArray[15][498-tmp]='_'
		gameArray[15][497-tmp]='_'
		gameArray[15][496-tmp]='_'
		return gameArray

	def lev2(self):
		gameArray[10][495]=' '
		for j in range(11,30):
			gameArray[j][495]=' '
		gameArray[11][494]=' '
		gameArray[12][493]=' '
		gameArray[13][492]=' '
		gameArray[14][491]=' '
		gameArray[15][490]=' '
		gameArray[15][491]=' '
		gameArray[15][492]=' '
		gameArray[15][493]=' '
		gameArray[15][494]=' '
		tmp=150
		gameArray[10][495+tmp]=','
		for j in range(11,30):
			gameArray[j][495+tmp]='|'
		gameArray[11][494+tmp]='/'
		gameArray[12][493+tmp]='/'
		gameArray[13][492+tmp]='/'
		gameArray[14][491+tmp]='/'
		gameArray[15][490+tmp]='/'
		gameArray[15][491+tmp]='_'
		gameArray[15][492+tmp]='_'
		gameArray[15][493+tmp]='_'
		gameArray[15][494+tmp]='_'

		gameArray[28][500-10]='/'
		gameArray[28][501-10]='`'
		gameArray[27][501-10]='_'
		gameArray[27][501-10]='_'
		gameArray[27][502-10]='_'
		gameArray[27][503-10]='_'

		gameArray[29][505]='\\'
		gameArray[29][506]='S'
		gameArray[29][507]='P'
		gameArray[29][508]='R'
		gameArray[29][509]='I'
		gameArray[29][510]='N'
		gameArray[29][511]='G'
		gameArray[29][512]='/'
		gameArray[28][505]='|'
		gameArray[28][512]='|'
		for i in range(506,512):
			gameArray[27][i]='_'

		return gameArray

	def moveRight(self):
		for j in range(99):
			for i in range(30):
				gameArray[i][j]=gameArray[i][j+1]
		# for j in range(30):
		# 	if(gameArray[j][99]!='='):
		# 		gameArray[j][99]=' '
		# for i in range(1):
		# 		r=randint(1,110)
		# 		if r<25 and gameArray[r][99]!='=':
		# 			gameArray[r][99]="."
		return gameArray

	def moveLeft(self):
		for j in range(100,0,-1):
			for i in range(30):
				gameArray[i][j]=gameArray[i][j-1]
		# for j in range(30):
		# 	if(gameArray[j][0]!='='):
		# 		gameArray[j][0]=' '
		# for i in range(1,2):
		# 		r=randint(1,110)
		# 		if r<25 and gameArray[r][0]!='=':
		# 			gameArray[r][0]="."
		return gameArray