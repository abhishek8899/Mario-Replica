
bulx=dict()
buly=dict()

class bul():

	def build(x,y):
		sz=len(bulx)
		bulx[sz]=x
		buly[sz]=y

	def bul_upd():
		for j in range(len(bulx)):
			buly[j]=buly[j]+3
				