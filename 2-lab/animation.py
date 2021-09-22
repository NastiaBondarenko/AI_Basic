import pygame


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


animationJump = [pygame.image.load('pictures/jump/Jump (1).png'), 
        pygame.image.load('pictures/jump/Jump (2).png'), pygame.image.load('pictures/jump/Jump (3).png'),
        pygame.image.load('pictures/jump/Jump (4).png'), pygame.image.load('pictures/jump/Jump (5).png'),
        pygame.image.load('pictures/jump/Jump (6).png'), pygame.image.load('pictures/jump/Jump (7).png'),
        pygame.image.load('pictures/jump/Jump (8).png'), pygame.image.load('pictures/jump/Jump (9).png'),
        pygame.image.load('pictures/jump/Jump (10).png'), pygame.image.load('pictures/jump/Jump (11).png'),
        pygame.image.load('pictures/jump/Jump (12).png'), pygame.image.load('pictures/jump/Jump (13).png'),
        pygame.image.load('pictures/jump/Jump (14).png'), pygame.image.load('pictures/jump/Jump (15).png'),
        pygame.image.load('pictures/jump/Jump (16).png'), pygame.image.load('pictures/jump/Jump (17).png'),
        pygame.image.load('pictures/jump/Jump (18).png'), pygame.image.load('pictures/jump/Jump (19).png'),
        pygame.image.load('pictures/jump/Jump (20).png')]        

youWin = [pygame.image.load('pictures/youWin/YouWin-01.png'), 
        pygame.image.load('pictures/youWin/YouWin-02.png'), pygame.image.load('pictures/youWin/YouWin-03.png'),
        pygame.image.load('pictures/youWin/YouWin-04.png'), pygame.image.load('pictures/youWin/YouWin-05.png'),
        pygame.image.load('pictures/youWin/YouWin-06.png'), pygame.image.load('pictures/youWin/YouWin-07.png'),
        pygame.image.load('pictures/youWin/YouWin-08.png'), pygame.image.load('pictures/youWin/YouWin-09.png'),
        pygame.image.load('pictures/youWin/YouWin-10.png'), pygame.image.load('pictures/youWin/YouWin-11.png'),
        pygame.image.load('pictures/youWin/YouWin-12.png'), pygame.image.load('pictures/youWin/YouWin-13.png'),
        pygame.image.load('pictures/youWin/YouWin-14.png'), pygame.image.load('pictures/youWin/YouWin-15.png'),
        pygame.image.load('pictures/youWin/YouWin-16.png'), pygame.image.load('pictures/youWin/YouWin-17.png'),
        pygame.image.load('pictures/youWin/YouWin-18.png'), pygame.image.load('pictures/youWin/YouWin-19.png'),
        pygame.image.load('pictures/youWin/YouWin-20.png'), pygame.image.load('pictures/youWin/YouWin-21.png'),
        pygame.image.load('pictures/youWin/YouWin-22.png'), pygame.image.load('pictures/youWin/YouWin-23.png'),
        pygame.image.load('pictures/youWin/YouWin-24.png'), pygame.image.load('pictures/youWin/YouWin-25.png'),
        pygame.image.load('pictures/youWin/YouWin-26.png'), pygame.image.load('pictures/youWin/YouWin-27.png')]  

youDie = [pygame.image.load('pictures/gameOver/GameOver-01.png'), 
        pygame.image.load('pictures/gameOver/GameOver-02.png'), pygame.image.load('pictures/gameOver/GameOver-03.png'),
        pygame.image.load('pictures/gameOver/GameOver-04.png'), pygame.image.load('pictures/gameOver/GameOver-05.png'),
        pygame.image.load('pictures/gameOver/GameOver-06.png'), pygame.image.load('pictures/gameOver/GameOver-07.png'),
        pygame.image.load('pictures/gameOver/GameOver-08.png'), pygame.image.load('pictures/gameOver/GameOver-09.png'),
        pygame.image.load('pictures/gameOver/GameOver-10.png'), pygame.image.load('pictures/gameOver/GameOver-11.png'),
        pygame.image.load('pictures/gameOver/GameOver-12.png'), pygame.image.load('pictures/gameOver/GameOver-13.png'),
        pygame.image.load('pictures/gameOver/GameOver-14.png')]


dead = [pygame.image.load('pictures/dead/Dead (1).png'), 
        pygame.image.load('pictures/dead/Dead (2).png'), pygame.image.load('pictures/dead/Dead (3).png'),
        pygame.image.load('pictures/dead/Dead (4).png'), pygame.image.load('pictures/dead/Dead (5).png'),
        pygame.image.load('pictures/dead/Dead (6).png'), pygame.image.load('pictures/dead/Dead (7).png'),
        pygame.image.load('pictures/dead/Dead (8).png'), pygame.image.load('pictures/dead/Dead (9).png'),
        pygame.image.load('pictures/dead/Dead (10).png'), pygame.image.load('pictures/dead/Dead (11).png'),
        pygame.image.load('pictures/dead/Dead (12).png'), pygame.image.load('pictures/dead/Dead (13).png'),
        pygame.image.load('pictures/dead/Dead (14).png'), pygame.image.load('pictures/dead/Dead (15).png'),
        pygame.image.load('pictures/dead/Dead (16).png'), pygame.image.load('pictures/dead/Dead (17).png'),
        pygame.image.load('pictures/dead/Dead (18).png'), pygame.image.load('pictures/dead/Dead (19).png'),
        pygame.image.load('pictures/dead/Dead (20).png'), pygame.image.load('pictures/dead/Dead (21).png'),
        pygame.image.load('pictures/dead/Dead (22).png'), pygame.image.load('pictures/dead/Dead (23).png'),
        pygame.image.load('pictures/dead/Dead (24).png'), pygame.image.load('pictures/dead/Dead (25).png'),
        pygame.image.load('pictures/dead/Dead (26).png'), pygame.image.load('pictures/dead/Dead (27).png'),
        pygame.image.load('pictures/dead/Dead (28).png'), pygame.image.load('pictures/dead/Dead (29).png'),
        pygame.image.load('pictures/dead/Dead (30).png')]

thriefWalk = [[
        [pygame.image.load('pictures/thrief/1_walk_L/p1_walk01.png'), 
        pygame.image.load('pictures/thrief/1_walk_L/p1_walk02.png'), pygame.image.load('pictures/thrief/1_walk_L/p1_walk03.png'),
        pygame.image.load('pictures/thrief/1_walk_L/p1_walk04.png'), pygame.image.load('pictures/thrief/1_walk_L/p1_walk05.png'),
        pygame.image.load('pictures/thrief/1_walk_L/p1_walk06.png'), pygame.image.load('pictures/thrief/1_walk_L/p1_walk07.png'),
        pygame.image.load('pictures/thrief/1_walk_L/p1_walk08.png'), pygame.image.load('pictures/thrief/1_walk_L/p1_walk09.png'),
        pygame.image.load('pictures/thrief/1_walk_L/p1_walk10.png'), pygame.image.load('pictures/thrief/1_walk_L/p1_walk11.png')],
        [pygame.image.load('pictures/thrief/1_walk_R/p1_walk01.png'), 
        pygame.image.load('pictures/thrief/1_walk_R/p1_walk02.png'), pygame.image.load('pictures/thrief/1_walk_R/p1_walk03.png'),
        pygame.image.load('pictures/thrief/1_walk_R/p1_walk04.png'), pygame.image.load('pictures/thrief/1_walk_R/p1_walk05.png'),
        pygame.image.load('pictures/thrief/1_walk_R/p1_walk06.png'), pygame.image.load('pictures/thrief/1_walk_R/p1_walk07.png'),
        pygame.image.load('pictures/thrief/1_walk_R/p1_walk08.png'), pygame.image.load('pictures/thrief/1_walk_R/p1_walk09.png'),
        pygame.image.load('pictures/thrief/1_walk_R/p1_walk10.png'), pygame.image.load('pictures/thrief/1_walk_R/p1_walk11.png')]
],[
        [pygame.image.load('pictures/thrief/2_walk_L/p2_walk01.png'), 
        pygame.image.load('pictures/thrief/2_walk_L/p2_walk02.png'), pygame.image.load('pictures/thrief/2_walk_L/p2_walk03.png'),
        pygame.image.load('pictures/thrief/2_walk_L/p2_walk04.png'), pygame.image.load('pictures/thrief/2_walk_L/p2_walk05.png'),
        pygame.image.load('pictures/thrief/2_walk_L/p2_walk06.png'), pygame.image.load('pictures/thrief/2_walk_L/p2_walk07.png'),
        pygame.image.load('pictures/thrief/2_walk_L/p2_walk08.png'), pygame.image.load('pictures/thrief/2_walk_L/p2_walk09.png'),
        pygame.image.load('pictures/thrief/2_walk_L/p2_walk10.png'), pygame.image.load('pictures/thrief/2_walk_L/p2_walk11.png')],
        [pygame.image.load('pictures/thrief/2_walk_R/p2_walk01.png'), 
        pygame.image.load('pictures/thrief/2_walk_R/p2_walk02.png'), pygame.image.load('pictures/thrief/2_walk_R/p2_walk03.png'),
        pygame.image.load('pictures/thrief/2_walk_R/p2_walk04.png'), pygame.image.load('pictures/thrief/2_walk_R/p2_walk05.png'),
        pygame.image.load('pictures/thrief/2_walk_R/p2_walk06.png'), pygame.image.load('pictures/thrief/2_walk_R/p2_walk07.png'),
        pygame.image.load('pictures/thrief/2_walk_R/p2_walk08.png'), pygame.image.load('pictures/thrief/2_walk_R/p2_walk09.png'),
        pygame.image.load('pictures/thrief/2_walk_R/p2_walk10.png'), pygame.image.load('pictures/thrief/2_walk_R/p2_walk11.png')]        
],[
        [pygame.image.load('pictures/thrief/3_walk_L/p3_walk01.png'), 
        pygame.image.load('pictures/thrief/3_walk_L/p3_walk02.png'), pygame.image.load('pictures/thrief/3_walk_L/p3_walk03.png'),
        pygame.image.load('pictures/thrief/3_walk_L/p3_walk04.png'), pygame.image.load('pictures/thrief/3_walk_L/p3_walk05.png'),
        pygame.image.load('pictures/thrief/3_walk_L/p3_walk06.png'), pygame.image.load('pictures/thrief/3_walk_L/p3_walk07.png'),
        pygame.image.load('pictures/thrief/3_walk_L/p3_walk08.png'), pygame.image.load('pictures/thrief/3_walk_L/p3_walk09.png'),
        pygame.image.load('pictures/thrief/3_walk_L/p3_walk10.png'), pygame.image.load('pictures/thrief/3_walk_L/p3_walk11.png')],

        [pygame.image.load('pictures/thrief/3_walk_R/p3_walk01.png'), 
        pygame.image.load('pictures/thrief/3_walk_R/p3_walk02.png'), pygame.image.load('pictures/thrief/3_walk_R/p3_walk03.png'),
        pygame.image.load('pictures/thrief/3_walk_R/p3_walk04.png'), pygame.image.load('pictures/thrief/3_walk_R/p3_walk05.png'),
        pygame.image.load('pictures/thrief/3_walk_R/p3_walk06.png'), pygame.image.load('pictures/thrief/3_walk_R/p3_walk07.png'),
        pygame.image.load('pictures/thrief/3_walk_R/p3_walk08.png'), pygame.image.load('pictures/thrief/3_walk_R/p3_walk09.png'),
        pygame.image.load('pictures/thrief/3_walk_R/p3_walk10.png'), pygame.image.load('pictures/thrief/3_walk_R/p3_walk11.png')]
]]

playerStand = pygame.image.load('pictures/Idle (1).png')

coin = pygame.image.load('pictures/things/star.png')

bg = pygame.image.load('pictures/bg.jpg')

grass = pygame.image.load('pictures/grass/grassHalfMid.png')


                