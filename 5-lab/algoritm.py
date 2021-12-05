matrixContiguity = []
point = []
way = []
newKart = []
from player import *
import math 
import pygame
import time
import random


def graf(kart):
	
	for i in range(len(kart.blockMap)):  #координати точок
		for j in range(len(kart.blockMap[0])):
			if kart.blockMap[i][j] == 1:
				point.append([i-1, j])
	# print(point)			


 
	for i in range(len(point)):  #створення матриці суміжності
		matrixContiguity.append([])
		for j in range(len(point)):
			matrixContiguity[i].append(0)

	for i in range(len(point)):
		if i + 1 < len(point) :
			if point[i][0] == point[i+1][0] and point[i][1] == point[i+1][1]-1:  #сумжні точки справа і з ліва
				# print(point[i], point[])
				matrixContiguity[i][i+1] = 1
				matrixContiguity[i+1][i] = 1



		canJump = [[],[],[]]
		right = 0
		rightright = 0
		rightCount = 1
		rightrightcount = 1
		rightdowncount = 1

		left = 0
		leftleft = 0
		leftCount = 1
		leftdowncount = 1
		leftleftCount = 1

		for j in range(len(point)): 
			if point[i][0] == point[j][0]+4 and point[i][1] == point[j][1]: #перевірка на прижок вверх
				canJump[0].append(j)
			elif point[i][0] == point[j][0]+3 and point[i][1] == point[j][1]:
				canJump[0].append(j)
			elif point[i][0] == point[j][0]+2 and point[i][1] == point[j][1]:
				canJump[0].append(j)
			elif point[i][0] == point[j][0]+1 and point[i][1] == point[j][1]:
				canJump[0].append(j)


			if point[i][0] == point[j][0]+4 and point[i][1] == point[j][1]+3: #перевірка на прижок вверх та вправо
				canJump[1].append(j)
			elif point[i][0] == point[j][0]+3 and point[i][1] == point[j][1]+3:
				canJump[1].append(j)
			elif point[i][0] == point[j][0]+2 and point[i][1] == point[j][1]+4:
				canJump[1].append(j)
			elif point[i][0] == point[j][0]+1 and point[i][1] == point[j][1]+5:
				canJump[1].append(j)
			elif point[i][0] == point[j][0] and point[i][1] == point[j][1]+5:
				canJump[1].append(j)		


			if point[i][0] == point[j][0]+4 and point[i][1] == point[j][1]-3: #перевірка на прижок вверх та вліво
				canJump[2].append(j)
			elif point[i][0] == point[j][0]+3 and point[i][1] == point[j][1]-3:
				canJump[2].append(j)
			elif point[i][0] == point[j][0]+2 and point[i][1] == point[j][1]-4:
				canJump[2].append(j)
			elif point[i][0] == point[j][0]+1 and point[i][1] == point[j][1]-5:
				canJump[2].append(j)	
			elif point[i][0] == point[j][0] and point[i][1] == point[j][1]-5:
				canJump[2].append(j)				


			if (point[i][0] == point[j][0] and point[i][1] == point[j][1]+1) or point[i][1] == 0:
				left = 1
			if (point[i][0] == point[j][0] and point[i][1] == point[j][1]-1) or point[i][1] == 19:	
				right = 1

		leftleft = left
		rightright = right
		while not left  : #перевірка на падіння вліво
			for j in range(len(point)):
				if point[i][0] == point[j][0] - leftCount and point[i][1] == point[j][1]+1:
					left = 1
					matrixContiguity[i][j] = 1
			leftCount +=1	

		while not leftleft  and leftdowncount<10: #перевірка на падіння вліво
			for j in range(len(point)):
				if point[i][0] == point[j][0] - leftdowncount and point[i][1] == point[j][1]+math.floor(leftleftCount):
					leftleft = 1
					matrixContiguity[i][j] = 1
			leftdowncount+=1		
			if math.floor(leftleftCount +0.34)<point[i][1]:
				leftleftCount += 0.34		 		
		
		while not right  :  #перевірка на падіння вправо
			for j in range(len(point)):
				if point[i][0] == point[j][0] - rightCount and point[i][1] == point[j][1]-1:
					right = 1
					matrixContiguity[i][j] = 1
			rightCount +=1	 

		while not rightright  and rightdowncount<10:  #перевірка на падіння вправо
			for j in range(len(point)):
				if point[i][0] == point[j][0] - rightdowncount and point[i][1] == point[j][1]-math.floor(rightrightcount):
					rightright = 1
					matrixContiguity[i][j] = 1
			rightdowncount +=1
			# if math.floor(rightdowncount+0.35)<20-point[i][1]:
			rightrightcount+=0.35			
		

		if len(canJump)>0 :
			for k in range(len(canJump)):
				if len(canJump[k])>0:
					matrixContiguity[i][canJump[k][0]] = 1	
					
			

class NewMap():
    def __init__(self, x, y, glass):
    	self.x = x
    	self.y = y
    	self.glass = glass
    	self.coin = False
    	self.visited = False
    	self.stec = False
    	self.way = []



def makeNewMap (kart):
	global newKart
	newKart = []	
	for i in range(len(kart.blockMap)):
		newKart.append([])
		for j in range(len(kart.blockMap[0])):
			newKart[i].append(NewMap(i,j,kart.blockMap[i][j]))


	for i in range(len(kart.coinMap)):
		for j in range(len(kart.coinMap[0])):
			if kart.coinMap[i][j] == 1:
				newKart[i][j].coin = True	



def checkBreak(trief, player, kart):

            plX = round(player.x/50)
            slX = round(trief.x/50)
            if plX < slX:
                first = plX 
                last = slX+1
            else:     
                first = slX 
                last = plX +1

            for i in range(first, last, 1):
                if kart[round(trief.y/50)+1][i].glass == 0:
                    return False
            return True   

def visibility(trief,  player, kart):

    def countA(trief, player, kart):
        aLeft = math.inf
        if trief.x > 20 and kart[round((trief.y+50)/50)][round((trief.x)/50)].glass == 1:
            point = trief.x-50
            aLeft = math.fabs(player.x-point)+math.fabs(point-trief.x)
        aRight = math.inf    
        if trief.x < 930 and kart[round((trief.y+50)/50)][round((trief.x)/50)].glass == 1:    
            point = trief.x+50
            aRight = math.fabs(player.x-point)+math.fabs(point-trief.x)

        if(aRight<aLeft): 
            return True  #right
        else:
            return False #left


    if(trief.y == player.y):   
        if(checkBreak(trief, player, kart)):
            if(countA(trief, player, kart)):
                trief.left= False
                trief.right = True
            else:
                trief.left= True
                trief.right = False
    # return trief            



class Variant():



	def __init__(self, newKart, triefs, lifetriefs, player, point, kart, pointPriv):
		self.myNewKart = []
		self.myTriefs = []
		self.pointNum = 0
		self.pointPriv = pointPriv

		for tr in triefs:
			self.myTriefs.append(Thrief(tr.x, tr.y, tr.color))

		for tr in lifetriefs:
			self.myTriefs.append(LivingThrief(tr.x, tr.y, tr.color))					

		self.myPlayer = Player(player.y, player.x)	

		self.ratingNum = 0

		self.point = point
		# self.myTriefs[0].speed = 2
		for i in range(len(kart.blockMap)):
			self.myNewKart.append([])
			for j in range(len(kart.blockMap[0])):
				self.myNewKart[i].append(NewMap(i,j,kart.blockMap[i][j]))


		for i in range(len(kart.coinMap)):
			for j in range(len(kart.coinMap[0])):
				if kart.coinMap[i][j] == 1:
					self.myNewKart[i][j].coin = True	


	def next(self, point, kart, pointNum, expectimax):
		self.point = point
		self.myPlayer.x = point[1]*50
		self.myPlayer.y = point[0]*50

		self.pointNum = pointNum

		self.myNewKart[point[0]][point[1]].visited = True

		
		if expectimax:
			for i in range(int(len(self.myTriefs)/2)):
				r = random.randint(0, len(self.myTriefs)-1)
				visibility(self.myPlayer, self.myTriefs[r], self.myNewKart)
			for i in range(len(self.myTriefs)):
				self.myTriefs[i].checkNextStep(kart)	

		else:
			for i in range(len(self.myTriefs)):
				visibility(self.myPlayer, self.myTriefs[i], self.myNewKart)
				self.myTriefs[i].checkNextStep(kart)






	def rating(self):
		self.ratingNum = 0
		for i in range(len(self.myNewKart)):
			for j in range(len(self.myNewKart[0])):
				if self.myNewKart[i][j].visited == True and self.myNewKart[i][j].coin == True:
					self.ratingNum =+ 10

		for tr in self.myTriefs:
			if tr.y == self.myPlayer.y:
				if checkBreak(tr, self.myPlayer, self.myNewKart):
					minus = (2 - round(math.fabs(tr.x - self.myPlayer.x)/50))*50
					if minus > 0:
						self.ratingNum =+(- minus)

		









def miniMax(player, kart, triefs, lifetriefs, expectimax):


	nowPoint = 0

	for i in range(len(point)):
		if point[i][0] == round(player.y/50) and point[i][1] == round(player.x/50):
			nowPoint = i
	newKart[point[nowPoint][0]][point[nowPoint][1]].visited = True		

	recess = 4

	algorinm = [[],]


	ratForFirst = 0

	for j in range(len(point)):
		if matrixContiguity[nowPoint][j] == 1:
			if newKart[point[j][0]][point[j][1]].visited == False:
				ratForFirst=+1
				algorinm[0].append(Variant(newKart, triefs, lifetriefs, player, point[nowPoint], kart, [nowPoint]))
				algorinm[0][len(algorinm[0])-1].next(point[j], kart, j, expectimax)
				algorinm[0][len(algorinm[0])-1].rating()

	if ratForFirst == 0:			
		for j in range(len(point)):
			if matrixContiguity[nowPoint][j] == 1:
				algorinm[0].append(Variant(newKart, triefs, lifetriefs, player, point[nowPoint], kart, [nowPoint]))
				algorinm[0][len(algorinm[0])-1].next(point[j], kart, j, expectimax)
				algorinm[0][len(algorinm[0])-1].rating()

		r = random.randint(0, len(algorinm[0])-1)
		y = algorinm[0][r]
		
		algorinm[0][r] = algorinm[0][0]
		algorinm[0][0] = y

	plusRating = 0
	for i in range(recess-1):
		algorinm.append([])
		for k in algorinm[i]:
			if k.ratingNum >= 0:
				plusRating =+ 1
				for j in range(len(point)):
					if matrixContiguity[k.pointNum][j] == 1:
						if k.myNewKart[point[j][0]][point[j][1]].visited == False:
							priv = []
							for pr in k.pointPriv:
								priv.append(pr)
							priv.append(k.pointNum)
							algorinm[i+1].append(Variant(k.myNewKart, k.myTriefs, [], k.myPlayer, k.point, kart, priv))
							algorinm[i+1][len(algorinm[i+1])-1].next(point[j], kart, j, expectimax)
							algorinm[i+1][len(algorinm[i+1])-1].rating()
							priv = []
		if plusRating == 0:
			for k in algorinm[i]:
				for j in range(len(point)):
						if matrixContiguity[k.pointNum][j] == 1:
							if k.myNewKart[point[j][0]][point[j][1]].visited == False:
								priv = k.pointPriv
								priv.append(k.pointNum)
								algorinm[i+1].append(Variant(k.myNewKart, k.myTriefs, [], k.myPlayer, k.point, kart, priv))
								algorinm[i+1][len(algorinm[i+1])-1].next(point[j], kart, j, expectimax)
								algorinm[i+1][len(algorinm[i+1])-1].rating()	
								plusRating=+1
		if plusRating == 0:
			for k in algorinm[i]:
				for j in range(len(point)):
						if matrixContiguity[k.pointNum][j] == 1:
							priv = k.pointPriv
							priv.append(k.pointNum)
							algorinm[i+1].append(Variant(k.myNewKart, k.myTriefs, [], k.myPlayer, k.point, kart, priv))
							algorinm[i+1][len(algorinm[i+1])-1].next(point[j], kart, j, expectimax)
							algorinm[i+1][len(algorinm[i+1])-1].rating()					

		plusRating = 0										
					

	rat = -1000
	num = 0
	now = 0
	for al in range(len(algorinm[recess-1])): 
		if algorinm[recess-1][al].ratingNum >= rat:
			rat = algorinm[recess-1][al].ratingNum
			num = al



	nextPoint = algorinm[len(algorinm)-1][num].pointPriv[1]
	player.x = point[nextPoint][1]*50
	player.y = point[nextPoint][0]*50
			
	newKart[point[nextPoint][0]][point[nextPoint][1]].visited = True			




def drawWay(win):
	PINK = (230, 50, 230)
	for i in range(len(newKart)):
		for j in range(len(newKart[0])):
			if len(newKart[i][j].way)>0	:	
				# pygame.draw.rectgl(win, PINK, ((j)*50+20, (i)*50+50), 20)
				f1 = pygame.font.Font(None, 20)
				tx = str(newKart[i][j].way)
				text1 = f1.render(tx, True,(0, 0, 0))
				win.blit(text1, ((j)*50, (i)*50+52))	
			