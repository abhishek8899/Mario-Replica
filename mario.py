#from __future__ import print_function
import signal,copy,sys,time,select
from random import randint
from os import system
from scr import *
from getchunix import *
from alarmexception import *
from position import *
from obs import *
from enm import *
from colorama import *
from coin import *
from bul import *

init(autoreset=True)

getch = GetchUnix()
bo=Board()
co=coins()
ob=obstacle()
pos=position()
eny=enemy()

def alarmHandler(signum, frame):
    raise AlarmException

def input_char(timeout=1):
    signal.signal(signal.SIGALRM, alarmHandler)
    signal.setitimer(signal.ITIMER_REAL,0.3,0.3)
    # signal.alarm(timeout)
    try:
        text = getch()
        signal.alarm(0)
        return text
    except AlarmException:
        klfmrk=1
        #print("\n Prompt timeout. Continuing...")
    signal.signal(signal.SIGALRM, signal.SIG_IGN)
    return ''

gameArray=bo.gameBoard()
gameArray=ob.build()
gameArray=co.build()
pos=eny.build()
cur=0
prev=0
a=16
u=24
tof=(u/a)*2
toh=(u/a)
dis=0
x=0
y=0
falling=0
jump=0
cur=0
score=0
shift=15
swm=0
bx=26
by=560
gun=0
bosshealth=30

print ("Enter level (1 or 2):")
lev=input()

if(lev==2):
	lev='2'
if(lev==1):
	lev='1'

while(True):
	pos=eny.pos_upd(y+49-shift+dis,x,lev)
	bul.bul_upd()
	for j in range(len(bulx)):
		if(buly[j]>=by and buly[j]<=by+7 and bulx[j]>=bx and bulx[j]<=bx+3):
			bosshealth-=10
	ninair=0
	support=0
	base=0
	if(bx==26):
		brise=1
	if(bx==2):
		brise=0
	if(x==16):
		falling=1

	# print (lev,swm)

	if(lev=='2' and swm==0):
		swm=1
		gameArray=bo.lev2()

	# print (x,"  jump ",jump,"  falling ",falling)
	# print (x)
	if(x<8) and (gameArray[29-x][y+49-shift+dis]=='_' or gameArray[29-x][y+48-shift+dis]=='_' or gameArray[29-x][y+50-shift+dis]=='_'):
		jump=1
		falling=0
		cur=6

	if(gameArray[30-x][y+49-shift+dis]=='=' or gameArray[30-x][y+48-shift+dis]=='=' or gameArray[30-x][y+50-shift+dis]=='='):
		base=1
		cur=x
	if(gameArray[26-x][y+49-shift+dis]=='=' or gameArray[26-x][y+48-shift+dis]=='=' or gameArray[26-x][y+50-shift+dis]=='='):
		falling=1
		jump=0
	# if(gameArray[30-x][y+49-shift+dis]=='^' or gameArray[30-x][y+48-shift+dis]=='^' or gameArray[30-x][y+50-shift+dis]=='^'):
	if x==2:
		for i in range(len(pos)):
			if y+49-shift+dis-pos[i]>=-3 and y+49-shift+dis-pos[i]<=1:
				vel[i]=0
				pos[i]=1005
				score+=100

	for i in range(len(pos)):
		if vel[i]==1 and pos[i]>460:
			vel[i]=-1
		if vel[i]==1 and gameArray[28][pos[i]+1]=='=':
			vel[i]*=-1
		if vel[i]==-1 and (gameArray[28][pos[i]-3]=='=' or pos[i]==2):
			vel[i]*=-1
	
	system("clear")

	if(dis>=463 and lev=='1'):
		print ("You have completed first level successfully...")
		print ("Score",score)
		print ("Press 2 to go to the next level or any other key to exit")
		lev=input()
		if lev!='2':
			sys.exit(0)	
		lev='2'
		dis=0
		pos=eny.build()
		gameArray=co.build()
		bulx.clear()
		buly.clear()

	if(bosshealth==0 or dis>562):
		print ("You win")
		score+=200
		print ("Score",score)
		sys.exit(0)

	if(x==0 and lev=='2' and y+49-shift+dis==501-10):
		gameArray[28][500-10]=' '
		gameArray[28][501-10]=' '
		gameArray[27][501-10]=' '
		gameArray[27][501-10]=' '
		gameArray[27][502-10]=' '
		gameArray[27][503-10]=' '
		gun=1


	for i in range(len(pos)):
		if x>1:
			break
		if y+49-shift+dis-pos[i]>=-3 and y+49-shift+dis-pos[i]<=1:
			print ("GAME OVER")
			print ("Score: ",score)
			sys.exit(0)
		
	if(base==1):
		if(falling==1):
			falling=0
			jump=0
	else:
		if(jump==0):
			falling=1

	for i in range(102):
		print (Fore.GREEN+'X',end='')
	print ('')
	for i in range(31):
		print (Fore.GREEN+'X',end='')
		for j in range(100):
			enmprsnt=0
			# if(posArray[i][j]==' '):
			
			fl=0

			#print bullets
			if gun==1:
				for p in range(len(bulx)):
					if(i==bulx[p] and j==buly[p]-dis):
						print (Fore.RED+'>',end='')
						fl=1
						break
			
			if fl==1:
				continue



			#print enemy


			if (i==28 or i==29):
				for k in range(len(pos)):
					if pos[k]-dis==j or pos[k]-dis==j+1 or pos[k]-dis==j+2:
						enmprsnt=1
						if(i==28):
							if pos[k]-dis==j or pos[k]-dis==j+2:
								print (Fore.YELLOW+'^',end='')
							else:
								print (Fore.YELLOW+'-',end='')
						elif pos[k]-dis==j:
							print (Fore.YELLOW+'\\',end='')
						elif pos[k]-dis==j+2:
							print (Fore.YELLOW+'/',end='')
						else:
							print(Fore.WHITE+' ',end='')
			if enmprsnt==1:
				continue;




			#print player

			if(i==29-x and j==y+48-shift):
				if(base==1):
					print (Fore.WHITE+'/',end='')
				else:
					print (Fore.WHITE+'}',end='')
				if gameArray[i][j+dis]=='O':
					gameArray[i][j+dis]=' '
					score+=50
			elif(i==29-x and j==y+50-shift):
				if(base==1):
					print (Fore.WHITE+'\\',end='')
				else:
					print (Fore.WHITE+'}',end='')
				if gameArray[i][j+dis]=='O':
					gameArray[i][j+dis]=' '
					score+=50
			elif(i==28-x and j==y+49-shift):
				print (Fore.WHITE+'|',end='')
				if gameArray[i][j+dis]=='O':
					gameArray[i][j+dis]=' '
					score+=50
			elif(i==28-x and j==y+48-shift):
				if(base==1 and gun==0):
					print (Fore.WHITE+'=',end='')
				elif gun==0:
					print (Fore.WHITE+'\\',end='')
				else:
					print (Fore.BLUE+'>',end='')
				if gameArray[i][j+dis]=='O':
					gameArray[i][j+dis]=' '
					score+=50
			elif(i==28-x and j==y+50-shift):
				if(base==1 and gun==0):
					print (Fore.WHITE+'=',end='')
				elif gun==0:
					print (Fore.WHITE+'/',end='')
				else:
					print (Fore.BLUE+'>',end='')
				if gameArray[i][j+dis]=='O':
					gameArray[i][j+dis]=' '
					score+=50
			elif(i==27-x and j==y+49-shift):
				if(base==1):
					print (Fore.WHITE+'O',end='')
				else:
					print (Fore.WHITE+'@',end='')



			#print boss enemy level 2

			elif(lev=='2' and i>=bx and i<bx+4 and j>=by-dis and j<=by-dis+7):
				if(i==bx and j==by-dis):
					print (Fore.CYAN+'<',end='')
				if(i==bx and j==by+1-dis):
					print (Fore.CYAN+'.',end='')
				if(i==bx and j==by+2-dis):
					print (Fore.CYAN+'>',end='')
				if(i==bx and j==by+3-dis):
					print (Fore.CYAN+' ',end='')
				if(i==bx and j==by+4-dis):
					print (Fore.CYAN+' ',end='')
				if(i==bx and j==by+5-dis):
					print (Fore.CYAN+'<',end='')
				if(i==bx and j==by+6-dis):
					print (Fore.CYAN+'.',end='')
				if(i==bx and j==by+7-dis):
					print (Fore.CYAN+'>',end='')

				if(i==bx+1 and j==by-dis):
					print (Fore.CYAN+' ',end='')
				if(i==bx+1 and j==by+1-dis):
					print (Fore.CYAN+' ',end='')
				if(i==bx+1 and j==by+2-dis):
					print (Fore.CYAN+' ',end='')
				if(i==bx+1 and j==by+3-dis):
					print (Fore.CYAN+'(',end='')
				if(i==bx+1 and j==by+4-dis):
					print (Fore.CYAN+')',end='')
				if(i==bx+1 and j==by+5-dis):
					print (Fore.CYAN+' ',end='')
				if(i==bx+1 and j==by+6-dis):
					print (Fore.CYAN+' ',end='')
				if(i==bx+1 and j==by+7-dis):
					print (Fore.CYAN+' ',end='')	

				if(i==bx+2) and (j>=by-dis or j<=by+7-dis):
					print (Fore.RED+'+',end='')

				if(i==bx+3 and j==by-dis):
					print (Fore.CYAN+'[',end='')
				if(i==bx+3 and j==by+1-dis):
					print (Fore.CYAN+' ',end='')
				if(i==bx+3 and j==by+2-dis):
					print (Fore.CYAN+' ',end='')
				if(i==bx+3 and j==by+3-dis):
					print (Fore.CYAN+'|',end='')
				if(i==bx+3 and j==by+4-dis):
					print (Fore.CYAN+'|',end='')
				if(i==bx+3 and j==by+5-dis):
					print (Fore.CYAN+' ',end='')
				if(i==bx+3 and j==by+6-dis):
					print (Fore.CYAN+' ',end='')
				if(i==bx+3 and j==by+7-dis):
					print (Fore.CYAN+']',end='')



			#print background

			else:
				if gameArray[i][j+dis]=='=' or gameArray[i][j+dis]=='-':
					print (Fore.RED+gameArray[i][j+dis],end='')
				elif gameArray[i][j+dis]=='.':
					print (Fore.WHITE+gameArray[i][j+dis],end='')
				else:
					print (Fore.BLUE+gameArray[i][j+dis],end='')
			
			
			#collect coins

			if(i>=27-x and i<=29-x and j>=y+48-shift and j<=y+50-shift and gameArray[i][j+dis]=='O'):
				gameArray[i][j+dis]=' '
				score+=50

		print (Fore.GREEN+'X')

	for i in range(102):
		print ('X',end='')
	print ('')
	print ("Score ",score,end=" ...   ")
	if j+dis>500 and lev=='2':
		print ("BOSS HEALTH: ",end='')
		if bosshealth==30:
			for i in range(30):
				print (Fore.WHITE+'+',end='')
		if bosshealth==20:
			for i in range(20):
				print (Fore.YELLOW+'+',end='')
		if bosshealth==10:
			for i in range(10):
				print (Fore.RED+'+',end='')
	# print ("cur ",cur,"   time.time() ",time.time(),"      prev ",prev
		# x=cur=0
		# prev=time.time()
		# posArray=pos.playerpos(int(cur))
		# print ("flying")

	inp = input_char()
	if(inp == 'q'):
		sys.exit(0)

	if(inp == 'w' and base==1):
		#prev=time.time()
		jump=1
		falling=0

	if(inp == 'b' and gun==1):
		bul.build(29-x,y+50-shift+dis)

	if(inp == 'a' and dis>0 and gameArray[29-x][y+47-shift+dis]!='=' and gameArray[28-x][y+47-shift+dis]!='=' and gameArray[27-x][y+47-shift+dis]!='='):
		# gameArray=bo.moveLeft()
		dis-=1

	if(inp == 'd' and dis<510 and gameArray[29-x][y+51-shift+dis]!='=' and gameArray[28-x][y+51-shift+dis]!='=' and gameArray[27-x][y+51-shift+dis]!='='):
		# gameArray=bo.moveRight()
		dis+=1

	if(x==16+cur):
		falling=1
		jump=0

	# if(base==0):
		# cur=u*(time.time()-prev)-0.5*(a)*(time.time()-prev)*(time.time()-prev)
		#posArray=pos.playerpos(int(cur))

	if(brise==1):
		bx-=2
	else:
		bx+=2

	if(x<16+cur):
		if(jump==1):
			x+=2
		elif(falling==1):
			x-=2
	elif(falling==1):
		x-=2;
	if(x<0):
		x=0

	# for i in range(10):
	# 	print ('')
	# for i in range(100):
	# 	print ("|",end='')
	# print ('')