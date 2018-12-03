from __future__ import print_function
import signal,copy,sys,time
from random import randint
from os import system

posArray = [[' ' for x in range(110)] for y in range(40)]


class position():

	def playerpos(self,pl):
		for i in range(40):
			for j in range(100):
				posArray[i][j]=' '
		posArray[27-pl][49]='O'
		posArray[28-pl][49]='|'
		#posArray[26][48]=posArray[26][50]=posArray[26][52]='X'
		posArray[28-pl][48]=posArray[28-pl][50]='='
		posArray[29-pl][48]='/'
		posArray[29-pl][50]="\\"
		return posArray

	#def moveUp(self):
		


