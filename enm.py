import time
from random import randint as rand
# enm = [[' ' for x in range(1100)] for y in range(40)]

# for i in range(40):
# 	for j in range(100):
# 		obs[i][j]=' '
pos=dict()
vel=dict()
prev = time.time()

class enemy():

	def build(self):
		pos.clear()
		for j in range(130,493,50):
			pos[(j-130)/50]=j
			vel[(j-130)/50]=-1
		return pos

	def pos_upd(self,a,b,lev):
		for j in range(len(pos)):
			pos[j]=max(-1,pos[j]+vel[j])
		if(b>7 and lev=='2'):
			for j in range(0,len(pos),2):
				if(pos[j]-a>0):
					vel[j]=-1
				else:
					vel[j]=1
			global prev
			if(time.time()-prev>rand(3,7)):
				for j in range(1,len(pos),2):
					vel[j]*=-1
				prev=time.time()
		return pos		