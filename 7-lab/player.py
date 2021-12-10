from animation import *
import pygame
from pygame import *
import math 
from map import *

class Character(sprite.Sprite):
    def __init__(self, x, y, playerStand, width, walkLeft, walkRight, numberOfAmin, left, right, speed):
        sprite.Sprite.__init__(self)
        self.speed = speed
        self.x = x 
        self.y = y
        self.beforeX = x
        self.boforeY = y
        self.playerStand = playerStand
        self.width = width
        
        self.left = left
        self.right = right

        self.numberOfAmin = numberOfAmin
        self.animCount = 0      

        self.walkLeft = walkLeft
        self.walkRight = walkRight

        self.die = False

    

    def stand(self):
        self.right = False
        self.left = False

    def draw(self):
        if self.animCount + 1 >= self.numberOfAmin:
            self.animCount = 0

        if self.left:
            self.animCount+=1
            return self.walkLeft[self.animCount]
        elif self.right:
            self.animCount+=1
            return self.walkRight[self.animCount]
        else:
            return self.playerStand 


class Player(Character):
    def __init__(self, x, y):
        Character.__init__(self, x, y, playerStand, 60, walkLeft, walkRight,20, False, False, 50)

        self.jump = False
        self.down = False
        self.countDown = 2
        self.countJump = 10

        self.winner = False
        self.youWinAnim = 0   
        self.youDieAnim = 0
        self.youWin = youWin 
        self.dead = dead
        self.youDie = youDie

    def godown(self):
        self.down = True
        if self.countDown == 0:
            self.countDown = 2    


        
class Thrief(Character):
    def __init__(self, x,y, color):    
        Character.__init__(self, x, y, thriefWalk[color][0][0],50, 
            thriefWalk[color][0], thriefWalk[color][1], 11, False, False, 50)
        self.color = color

    def goleft(self, kart):
        xb = round((self.x)/50)
        y = round((self.y)/50)
        self.beforeX = self.x
        self.x-=self.speed
        xn = round((self.x)/50)
        kart.thriefMap[y][xb] = 0
        kart.thriefMap[y][xn] = 2
        self.left = True
        self.right = False

    def goright(self, kart):
        xb = round((self.x)/50)
        y = round((self.y)/50)
        self.beforeX = self.x
        self.x+=self.speed
        xn = round((self.x)/50)
        kart.thriefMap[y][xb] = 0
        kart.thriefMap[y][xn] = 2
        self.left = False
        self.right = True    

    
   


    
    def visibility(self, player, kart):

        def checkBreak(self, player, kart):

            plX = round(player.x/50)
            slX = round(self.x/50)
            if plX < slX:
                first = plX 
                last = slX+1
            else:     
                first = slX 
                last = plX +1

            for i in range(first, last, 1):
                if kart.blockMap[round(self.y/50)+1][i] == 0:
                    return False
            return True   


        def countA(self, player, kart):
            aLeft = math.inf
            if self.x > 20 and kart.blockMap[round((self.y+50)/50)][round((self.x)/50)] == 1:
                point = self.x-50
                aLeft = math.fabs(player.x-point)+math.fabs(point-self.x)
            aRight = math.inf    
            if self.x < 930 and kart.blockMap[round((self.y+50)/50)][round((self.x)/50)] == 1:    
                point = self.x+50
                aRight = math.fabs(player.x-point)+math.fabs(point-self.x)

            if(aRight<aLeft): 
                return True  #right
            else:
                return False #left


        if(self.y == player.y):   
            if(checkBreak(self, player, kart)):
                if(countA(self, player, kart)):
                    self.left= False
                    self.right = True
                else:
                    self.left= True
                    self.right = False
    



                





            


         
           

