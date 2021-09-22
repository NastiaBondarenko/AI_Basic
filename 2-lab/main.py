from player import *
import pygame
import random
from animation import *
from map import*
from algoritm import *

pygame.init()
win = pygame.display.set_mode((1000,570))
pygame.display.set_caption("Asya's Game")
player = Player(0,500)
kart = Map()

thriefs = []


def drawWindow():
	bground = pygame.transform.scale(bg, (1000, 550))
	win.blit(bground, (0,0))
		
	for i in range(len(kart.blockMap)):
		for j in range(len(kart.blockMap[i])):
			if( kart.blockMap[i][j] == 1):
				win.blit(grass, (j*50,  i*50))
			if(kart.coinMap[i][j] == 1):
				win.blit(coin, (j*50, i*50))	
	drawWay(win)		
	for tr in thriefs:
			win.blit(tr.draw(), (tr.x,tr.y))			

	if player.winner:
		pygame.draw.rect(win,(0, 0 , 0), (0, 0, 1000, 600))
		win.blit(youWin1(), (260,120))
	elif player.die:
		youDie1()			
	else:				
		win.blit(player.draw(), (player.x, player.y))
		
	pygame.display.update()		

def youDie1():
	player.youDieAnim +=1
	if player.youDieAnim < 30:
		win.blit(player.dead[player.youDieAnim], (player.x, player.y))
	elif player.youDieAnim == 42:
			global run 
			run = False
			player.winner = False
			pygame.draw.rect(win,(0, 0 , 0), (0, 0, 1000, 600))
			win.blit(player.youDie[player.youDieAnim-29], (260,120))
	else:
		pygame.draw.rect(win,(0, 0 , 0), (0, 0, 1000, 600))
		win.blit(player.youDie[player.youDieAnim-29], (260,120))	

def youWin1():
	player.youWinAnim +=1

	if player.youWinAnim == 27:
		global run 
		run = False
		player.winner = False
	return player.youWin[player.youWinAnim-1]


def checkNextStep(tr):
	if tr.left:
		if tr.x > 20 and kart.blockMap[round((tr.y+50)/50)][round((tr.x)/50)] == 1:
			tr.goleft()
		else:
			tr.goright()
	else:
		if tr.x < 930 and kart.blockMap[round((tr.y+50)/50)][round((tr.x)/50)] == 1:	
			tr.goright()
		else:
			tr.goleft()		

def checkBlock():
	return kart.blockMap[round((player.y+50)/50)][round((player.x)/50)] == 1 

def checkCoin():
	return kart.coinMap[round((player.y)/50)][round((player.x)/50)] == 1 

def checkThrief():
	for i in range(len(kart.thriefMap)):
		for j in range(len(kart.thriefMap[i])):
			if kart.thriefMap[i][j] > 0:
				thriefs.append(Thrief(j*50, i*50, kart.thriefMap[i][j]-1))



checkThrief()
graf(kart)
makeNewMap(kart)

al = 0
algoritm = [DFS1(kart), BFS1(kart), USF1(kart)]
algoritm[0].mainAlgoritm()


run = True
while run:
	pygame.time.delay(40)
	

	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	for tr in thriefs:
		checkNextStep(tr)	
		if tr.y == player.y and round(tr.x/50) == round(player.x/50) :
			player.die = True	

	if checkCoin():
		kart.coinMap[round((player.y)/50)][round((player.x)/50)] = 0 	
		kart.coin -= 1
		
	if kart.coin == 0:
		player.winner = True

	keys = pygame.key.get_pressed()

	if keys[pygame.K_SPACE]:
		kart = Map()
		player.x = 0
		player.y = 500
		thriefs = []
		checkThrief()
		algoritm = [DFS1(kart), BFS1(kart), USF1(kart)]
		algoritm[al].newAlgoritm()
		algoritm[al].mainAlgoritm()

	if keys[pygame.K_z]:
		if al == 2:
			al = 0
			algoritm[al].newAlgoritm()

			algoritm[al].mainAlgoritm()
			
		else:
			al+=1
			algoritm[al].newAlgoritm()
			algoritm[al].mainAlgoritm()

		
	if keys[pygame.K_LEFT] and player.x > 0 and not player.die:
		player.goleft()

	elif keys[pygame.K_RIGHT] and player.x < 1000 - player.width-10 and not player.die:
		player.goright()

	else:
		player.stand() 	

	if not(player.jump):
		if not checkBlock():
			player.godown()
		else:		
			if keys[pygame.K_UP] and not player.die:
				player.jump = True

	else:
		if player.countJump >= -10:
			if player.countJump < 0:
				if checkBlock() and player.y > -60:
					player.y = round((player.y)/50) * 50
					player.jump = False
					player.countJump = 11
				else:	
					player.y += (player.countJump**2)/2
			else:
				player.y -= (player.countJump**2)/2
			player.countJump -=1
		else:		
			player.jump = False
			player.countJump = 10

	if player.down :
		player.countDown-=1
		player.y += 25
		if(player.countDown == 0):
			player.down = False 	

	drawWindow()
		
	