import pygame
import random

block1 = [[1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1],
[0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
[0,0,1,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,1,1,1,0,0,0,1,1,1,1,1,1],
[0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
[1,1,1,1,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

pygame.init()
win = pygame.display.set_mode((1000,570))

pygame.display.set_caption("Asya's Game")

walkRight = [pygame.image.load('pictures/walkR/Walk (1).png'), 
pygame.image.load('pictures/walkR/Walk (2).png'), pygame.image.load('pictures/walkR/Walk (3).png'),
pygame.image.load('pictures/walkR/Walk (4).png'), pygame.image.load('pictures/walkR/Walk (5).png'),
pygame.image.load('pictures/walkR/Walk (6).png'), pygame.image.load('pictures/walkR/Walk (7).png'),
pygame.image.load('pictures/walkR/Walk (8).png'), pygame.image.load('pictures/walkR/Walk (9).png'),
pygame.image.load('pictures/walkR/Walk (10).png'), pygame.image.load('pictures/walkR/Walk (11).png'),
pygame.image.load('pictures/walkR/Walk (12).png'), pygame.image.load('pictures/walkR/Walk (13).png'),
pygame.image.load('pictures/walkR/Walk (14).png'), pygame.image.load('pictures/walkR/Walk (15).png'),
pygame.image.load('pictures/walkR/Walk (16).png'), pygame.image.load('pictures/walkR/Walk (17).png'),
pygame.image.load('pictures/walkR/Walk (18).png'), pygame.image.load('pictures/walkR/Walk (19).png'),
pygame.image.load('pictures/walkR/Walk (20).png')]


walkLeft = [pygame.image.load('pictures/walkL/Walk (1).png'), 
pygame.image.load('pictures/walkL/Walk (2).png'), pygame.image.load('pictures/walkL/Walk (3).png'),
pygame.image.load('pictures/walkL/Walk (4).png'), pygame.image.load('pictures/walkL/Walk (5).png'),
pygame.image.load('pictures/walkL/Walk (6).png'), pygame.image.load('pictures/walkL/Walk (7).png'),
pygame.image.load('pictures/walkL/Walk (8).png'), pygame.image.load('pictures/walkL/Walk (9).png'),
pygame.image.load('pictures/walkL/Walk (10).png'), pygame.image.load('pictures/walkL/Walk (11).png'),
pygame.image.load('pictures/walkL/Walk (12).png'), pygame.image.load('pictures/walkL/Walk (13).png'),
pygame.image.load('pictures/walkL/Walk (14).png'), pygame.image.load('pictures/walkL/Walk (15).png'),
pygame.image.load('pictures/walkL/Walk (16).png'), pygame.image.load('pictures/walkL/Walk (17).png'),
pygame.image.load('pictures/walkL/Walk (18).png'), pygame.image.load('pictures/walkL/Walk (19).png'),
pygame.image.load('pictures/walkL/Walk (20).png')]


trief_1_Right = [pygame.image.load('pictures/thrief/1_walk_R/p1_walk01.png'), 
pygame.image.load('pictures/thrief/1_walk_R/p1_walk02.png'), pygame.image.load('pictures/thrief/1_walk_R/p1_walk03.png'),
pygame.image.load('pictures/thrief/1_walk_R/p1_walk04.png'), pygame.image.load('pictures/thrief/1_walk_R/p1_walk05.png'),
pygame.image.load('pictures/thrief/1_walk_R/p1_walk06.png'), pygame.image.load('pictures/thrief/1_walk_R/p1_walk07.png'),
pygame.image.load('pictures/thrief/1_walk_R/p1_walk08.png'), pygame.image.load('pictures/thrief/1_walk_R/p1_walk09.png'),
pygame.image.load('pictures/thrief/1_walk_R/p1_walk10.png'), pygame.image.load('pictures/thrief/1_walk_R/p1_walk11.png'),
] 


bg = pygame.image.load('pictures/bg.jpg')
bground = pygame.transform.scale(bg, (1000, 550))

playerStand = pygame.image.load('pictures/Idle (1).png')

grass = pygame.image.load('pictures/grass/grassHalfMid.png')


x = 0
y = 500
width = 40
height = 60
speed = 10

isJump = False
jumpCount = 10

left = False
right = False
animCount = 0

DOWN = False
countDown = 0



trief = True
triefCount = 0
def drawWindow():
	global animCount 
	global triefCount
	
	win.blit(bground, (0,0))

	for i in range(len(block1)):
		for j in range(len(block1[i])):
			if( block1[i][j] == 1):
				win.blit(grass, (j*50,  i*50))

	if animCount + 1 >= 40:
		animCount = 0

	if left:
		win.blit(walkLeft[animCount//2], (x,y))
		animCount+=1
	elif right:
		win.blit(walkRight[animCount//2], (x,y))
		animCount+=1
	else:
		win.blit(playerStand, (x,y))	
	# if triefCount + 1 >= 11:
	# 	triefCount = 0	
	# win.blit(trief_1_Right[triefCount], (20+triefCount,20+triefCount))
	# triefCount +=1	
	pygame.display.update()		

def down():
	global y
	if block1[round((y+50)/50)][round((x)/50)] != 1:
		global DOWN
		DOWN = True
		global countDown
		if countDown == 0:
			countDown = 2

run = True
while run:
	pygame.time.delay(40)
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	

	keys = pygame.key.get_pressed()
	if keys[pygame.K_LEFT] and x>0:
		x-=speed
		if not isJump:
			down()
		left = True
		right = False
	elif keys[pygame.K_RIGHT] and x < 1000 - width-10:
		x+=speed
		if not isJump:
			down()
		left = False
		right = True
	else:
		left = False
		right = False 
		animCount = 0
	if not(isJump):	
		# if keys[pygame.K_UP] and y > 25:
		# 	y-=speed
		# if keys[pygame.K_DOWN] and y < 600 - height - 25:
		# 	y+=speed
		if keys[pygame.K_UP] and not DOWN:
			isJump = True
	else:
		if jumpCount >= -10:
			if jumpCount < 0:
				if block1[round((y+50)/50)][round((x)/50)] == 1 and jumpCount >-40 and y > -60 :
					y = round((y)/50) * 50
					isJump= False
					jumpCount = 11


				else:	
					y += (jumpCount**2)/2
			else:
				y -= (jumpCount**2)/2
			jumpCount -=1
		else:		
			isJump = False
			jumpCount = 10
			down()
	if DOWN :
		countDown-=1
		y += 25
		if(countDown==0):
			DOWN = False 	
			down()		

	drawWindow()
		
	