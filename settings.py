#Define em variáveis o tamanho da tela do display
largura = 1133
altura = 504

import pygame


#ABAIXO SÃO AS IMPORTAÇÕES DE TODOS OS SPRITES DOS OBJETOS QUE POSSUEM SPRITES

#BALL - Shadow e Sprite
ball = pygame.image.load('Sprites/Ball/ball.png')
ballShadow = pygame.image.load('Sprites/Ball/shadow.png')




#CHAR2 - CIMA  /\  ----------------------------

char2Movement = [pygame.image.load('Sprites/Player_2/playerup_3.png'),pygame.image.load('Sprites/Player_2/playerup_4.png'),pygame.image.load('Sprites/Player_2/playerup_5.png'),pygame.image.load('Sprites/Player_2/playerup_6.png')]

char2HitR = pygame.image.load('Sprites/Player_2/playerup_12.png')

char2HittedR= [pygame.image.load('Sprites/Player_2/playerup_13.png'),pygame.image.load('Sprites/Player_2/playerup_14.png'),pygame.image.load('Sprites/Player_2/playerup_14.png')]

char2HitL = pygame.image.load('Sprites/Player_2/playerup_15.png')
char2HittedL = [pygame.image.load('Sprites/Player_2/playerup_16.png'),pygame.image.load('Sprites/Player_2/playerup_17.png'),pygame.image.load('Sprites/Player_2/playerup_17.png')]

char2 = [pygame.image.load('Sprites/Player_2/playerup_1.png'),pygame.image.load('Sprites/Player_2/playerup_1.png'),pygame.image.load('Sprites/Player_2/playerup_1.png'),pygame.image.load('Sprites/Player_2/playerup_1.png'),pygame.image.load('Sprites/Player_2/playerup_1.png'),pygame.image.load('Sprites/Player_2/playerup_1.png'),pygame.image.load('Sprites/Player_2/playerup_1.png'),pygame.image.load('Sprites/Player_2/playerup_1.png'),pygame.image.load('Sprites/Player_2/playerup_1.png'),pygame.image.load('Sprites/Player_2/playerup_1.png'),pygame.image.load('Sprites/Player_2/playerup_1.png'),pygame.image.load('Sprites/Player_2/playerup_2.png'),pygame.image.load('Sprites/Player_2/playerup_2.png'),pygame.image.load('Sprites/Player_2/playerup_2.png'),pygame.image.load('Sprites/Player_2/playerup_2.png'),pygame.image.load('Sprites/Player_2/playerup_2.png'),pygame.image.load('Sprites/Player_2/playerup_2.png'),pygame.image.load('Sprites/Player_2/playerup_2.png'),pygame.image.load('Sprites/Player_2/playerup_2.png'),pygame.image.load('Sprites/Player_2/playerup_2.png'),pygame.image.load('Sprites/Player_2/playerup_2.png'),pygame.image.load('Sprites/Player_2/playerup_2.png')]






#CHAR1 - BAIXO \/  ----------------------------

charMovement = [pygame.image.load('Sprites/Player_1/playerdown_3.png'),pygame.image.load('Sprites/Player_1/playerdown_4.png'),pygame.image.load('Sprites/Player_1/playerdown_5.png'),pygame.image.load('Sprites/Player_1/playerdown_6.png')]

charHitR = pygame.image.load('Sprites/Player_1/playerdown_12.png')
charHittedR = [pygame.image.load('Sprites/Player_1/playerdown_13.png'),pygame.image.load('Sprites/Player_1/playerdown_14.png'),pygame.image.load('Sprites/Player_1/playerdown_14.png')]

charHitL = pygame.image.load('Sprites/Player_1/playerdown_15.png')
charHittedL = [pygame.image.load('Sprites/Player_1/playerdown_16.png'),pygame.image.load('Sprites/Player_1/playerdown_17.png'),pygame.image.load('Sprites/Player_1/playerdown_17.png')]

char = [pygame.image.load('Sprites/Player_1/playerdown_1.png'),pygame.image.load('Sprites/Player_1/playerdown_1.png'),pygame.image.load('Sprites/Player_1/playerdown_1.png'),pygame.image.load('Sprites/Player_1/playerdown_1.png'),pygame.image.load('Sprites/Player_1/playerdown_1.png'),pygame.image.load('Sprites/Player_1/playerdown_1.png'),pygame.image.load('Sprites/Player_1/playerdown_1.png'),pygame.image.load('Sprites/Player_1/playerdown_1.png'),pygame.image.load('Sprites/Player_1/playerdown_1.png'),pygame.image.load('Sprites/Player_1/playerdown_1.png'),pygame.image.load('Sprites/Player_1/playerdown_1.png'),pygame.image.load('Sprites/Player_1/playerdown_2.png'),pygame.image.load('Sprites/Player_1/playerdown_2.png'),pygame.image.load('Sprites/Player_1/playerdown_2.png'),pygame.image.load('Sprites/Player_1/playerdown_2.png'),pygame.image.load('Sprites/Player_1/playerdown_2.png'),pygame.image.load('Sprites/Player_1/playerdown_2.png'),pygame.image.load('Sprites/Player_1/playerdown_2.png'),pygame.image.load('Sprites/Player_1/playerdown_2.png'),pygame.image.load('Sprites/Player_1/playerdown_2.png'),pygame.image.load('Sprites/Player_1/playerdown_2.png'),pygame.image.load('Sprites/Player_1/playerdown_2.png'),pygame.image.load('Sprites/Player_1/playerdown_2.png')]
