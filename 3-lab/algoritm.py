matrixContiguity = []
point = []
way = []
newKart = []
passed = []
import math 
import pygame
import time
# from map import*


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



def makeNewMap (kart, player, thriefs):
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

	# for i in range(len(passed)):
	# 	newKart[point[passed[i]][0]][point[passed[i]][1]].visited = True

	coordinate = []
	for i in range(len(thriefs)):
		coordinate.append([thriefs[i].y, thriefs[i].x])
	for i in range(len(coordinate)):
	# print(coordinate)
		if (coordinate[i][0] == player.y and (math.fabs(coordinate[i][1] - player.x) <= 100 )):	
			newKart[round(coordinate[i][0]/50)][round(coordinate[i][1]/50)].visited = True		


			
class Algoritm(object):
	def __init__(self, name):
		self.name = name
		self.length = 0
		self.coin = 10
		self.first = [10,0]

		self.nowNumber = 0
		self.noWay = False

		self.visited = []
		self.prev = []      
		
	def numberCoin(self):
		coins = 0
		for i in range(len(self.kart.coinMap)):
			for j in range(len(self.kart.coinMap[0])):
				if self.kart.coinMap[i][j] == 1:
					coins +=1
		self.coin = coins	

	def newAlgoritm(self, player, thriefs):
		global matrixContiguity
		global point
		global  way 
		global newKart
		matrixContiguity = []
		point = []
		way = []
		newKart = []

		graf(self.kart)
		makeNewMap(self.kart, player, thriefs)
		self.length = 0
		self.coin = 10
		self.first = [round((player.y)/50), round((player.x)/50)]

		self.nowNumber = 0
		self.noWay = False

		self.visited = []
		self.prev = []  		

				
			


	def printLength(self, start_time):
			if not self.noWay:
				print(self.name, "    " ,self.length)	
				print("--- %s seconds ---" % (time.time() - start_time))
	
	def searchFirst(self):
		for i in range(len(point)):
			if point[i] == self.first:
				self.nowNumber = i
				newKart[point[i][0]][point[i][1]].visited = True


			
def checkMonstr(y, x, thriefs):
	coordinate = []
	for i in range(len(thriefs)):
		coordinate.append([thriefs[i].y, thriefs[i].x])
	for i in range(len(coordinate)):
		# print(coordinate, "y = ", y, "x = ",x)
		if (coordinate[i][0] == y and (math.fabs(coordinate[i][1] - x) <= 150 )):
		 	return False
	return True	 	

					
class DFS1(Algoritm):
	def __init__(self,kart):
		Algoritm.__init__(self, "DFS")
		self.kart = kart
		super(DFS1, self).searchFirst()

		super(DFS1, self).numberCoin()
		newKart[point[self.nowNumber][0]][point[self.nowNumber][1]].way.append(1)
		self.prev.append(self.nowNumber)



	def mainAlgoritm(self, thriefs):

		nextOne = False
		for i in range(len(matrixContiguity)):
			if (not nextOne) and matrixContiguity[self.nowNumber][i] == 1 and not newKart[point[i][0]][point[i][1]].visited :
				# print(i, point[i])
				if(checkMonstr(point[i][0]*50, (point[i][1]+1)*50, thriefs)):
					# print("true")
					nextOne = True
					self.prev.append(i)
					# print(k, nowNumber, point[nowNumber],point[i])
					x = (point[i][0] - point[self.nowNumber][0])
					y = (point[i][1] - point[self.nowNumber][1])
					pr = math.fabs(x) + math.fabs(y)
					self.length += pr
					self.nowNumber = i

					newKart[point[i][0]][point[i][1]].visited = True
					if newKart[point[i][0]][point[i][1]].coin:
						self.coin -= 1 


		if not nextOne:
			# print("back")
			if len(self.prev) == 0:
				print("Шляху не існує")
				self.noWay = True
				return  0
			r = self.prev[len(self.prev)-1]
			if (checkMonstr(point[r][0]*50, (point[r][1]+1)*50, thriefs)):	
				# print("back, back")
				x = (point[self.prev[len(self.prev)-1]][0] - point[self.nowNumber][0])
				y = (point[self.prev[len(self.prev)-1]][1] - point[self.nowNumber][1])
				pr = math.fabs(x) + math.fabs(y)
				self.length += pr	
				self.nowNumber = self.prev[len(self.prev)-1]
				self.prev.pop(len(self.prev)-1)
			else:
				if not (checkMonstr(point[self.nowNumber][0]*50, (point[self.nowNumber][1]+1)*50, thriefs)):
					for i in range(len(matrixContiguity)):
						if matrixContiguity[self.nowNumber][i] == 1 :
							# print(i, point[i])
							if(checkMonstr(point[i][0]*50, (point[i][1]+1)*50, thriefs)):
								# print("back true")
								# print(k, nowNumber, point[nowNumber],point[i])
								x = (point[i][0] - point[self.nowNumber][0])
								y = (point[i][1] - point[self.nowNumber][1])
								pr = math.fabs(x) + math.fabs(y)
								self.length += pr
								self.nowNumber = i
		way.append(self.nowNumber)
		newKart[point[self.nowNumber][0]][point[self.nowNumber][1]].way.append(len(way)+1)	


		# super(DFS1, self).printLength(startDFS_time)	



	


	# def checkNextStep(self, thriefs):	
	# 	nextOne = False
	# 	for i in range(len(matrixContiguity)):
	# 		if (not nextOne) and matrixContiguity[self.nowNumber][i] == 1 and not newKart[point[i][0]][point[i][1]].visited and checkMonstr(point[i][0],point[i][1], thriefs):
	# 			nextOne = True
	# 			self.prev.append(i)
	# 			# print(k, nowNumber, point[nowNumber],point[i])
	# 			x = (point[i][0] - point[self.nowNumber][0])
	# 			y = (point[i][1] - point[self.nowNumber][1])
	# 			pr = math.fabs(x) + math.fabs(y)
	# 			self.length += pr
	# 			self.nowNumber = i

	# 			newKart[point[i][0]][point[i][1]].visited = True
	# 			if newKart[point[i][0]][point[i][1]].coin:
	# 				self.coin -= 1 
	# 	if not nextOne:
	# 		if len(self.prev) == 0:
	# 			print("Шляху не існує")
	# 			self.noWay = True
	# 			return 0
	# 		x = (point[self.prev[len(self.prev)-1]][0] - point[self.nowNumber][0])
	# 		y = (point[self.prev[len(self.prev)-1]][1] - point[self.nowNumber][1])
	# 		pr = math.fabs(x) + math.fabs(y)
	# 		self.length += pr	
	# 		self.nowNumber = self.prev[len(self.prev)-1]
	# 		self.prev.pop(len(self.prev)-1)
	# 	way.append(self.nowNumber)
	# 	newKart[point[self.nowNumber][0]][point[self.nowNumber][1]].way.append(len(way)+1)



	# def tryOneMore(self, numb, thriefs):
	# 	global way
	# 	withTrief = numb+1
	# 	way1 = []
	# 	for i in range(numb-1):
	# 		way1.append(way[i])

	# 	for i in range(numb, len(way)):
	# 		newKart[point[way[i]][0]][point[way[i]][1]].visited = False 
	# 		pr = []
	# 		for j in range(len(newKart[point[way[i]][0]][point[way[i]][1]].way)):
	# 			if newKart[point[way[i]][0]][point[way[i]][1]].way[j] < numb:
	# 				pr.append(newKart[point[way[i]][0]][point[way[i]][1]].way[j])
	# 		newKart[point[way[i]][0]][point[way[i]][1]].way = pr		




	# 	way = way1	
	# 	nextOne = False
	# 	self.nowNumber = numb
	# 	self.checkNextStep(thriefs)





	


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
			