from animation import *
import pygame
from pygame import *


class Character(sprite.Sprite):
    def __init__(self, x, y, playerStand, width, walkLeft, walkRight, numberOfAmin, left, right, speed):
        sprite.Sprite.__init__(self)
        self.speed = speed
        self.x = x 
        self.y = y
        self.playerStand = playerStand
        self.width = width
        
        self.left = left
        self.right = right

        self.numberOfAmin = numberOfAmin
        self.animCount = 0      

        self.walkLeft = walkLeft
        self.walkRight = walkRight

        self.die = False

    def goleft(self):
        self.x-=self.speed
        self.left = True
        self.right = False

    def goright(self):
        self.x+=self.speed
        self.left = False
        self.right = True

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
        Character.__init__(self, x, y, playerStand, 60, walkLeft, walkRight,20, False, False, 10)

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
            thriefWalk[color][0], thriefWalk[color][1], 11, False, False, 5)
        self.color = color



         
           

