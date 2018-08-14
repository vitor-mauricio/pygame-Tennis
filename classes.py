import pygame
from settings import *

#Classe que define os players
class Player:
	p1_1 = [int(largura/2 - 100),int(altura - 90)]
	p1_2 = [int(largura/2 + 180),int(altura - 90)]

	p2_1 = [int(largura/2 + 80),int(altura/4 - 120)]
	p2_2 = [int(largura/2 - 100),int(altura/4 - 120)]
	def __init__(self,x,y,player,sentido):
		self.player = player		
		self.pos_x = x
		self.pos_y = y
		self.altura = 10
		self.largura = 30
		self.contador_passo = 0
		self.movement = False
		self.hit = False
		self.hitrelease = False
		self.hitbox = (self.pos_x + 20,self.pos_y + 20, 28,40)
		self.force = 0
		self.forcebox = (self.pos_x, self.pos_y - 10, 10,self.force)
		self.balldirection = 0
		self.hitsentido = sentido
#Metodo que define a posição do player baseado nos parametros passados(No caso, pelo juiz)
	def SetPosition(self,position,player):
		if position == 1 and player == 1 :
			self.pos_x = self.p1_1[0]
			self.pos_y = self.p1_1[1]
		elif position == 2 and player == 1:
			self.pos_x = self.p1_2[0]
			self.pos_y = self.p1_2[1]
		elif position == 1 and player == 2 :
			self.pos_x = self.p2_1[0]
			self.pos_y = self.p2_1[1]
		elif position == 2 and player == 2:
			self.pos_x = self.p2_2[0]
			self.pos_y = self.p2_2[1]
#Metodo que desenha o player no display (chamado toda vez no loop, para dar sensação de movimento)
			#Alem disso, foram mapeados aqui também os sprites dos players que ditam quando serão acionados,
			#de acordo com os mapeamento das teclas de cada personagem
	def Draw(self,surface):
		
		if self.contador_passo + 1 >= 20:
			self.contador_passo = 0
		if self.player == "1":
			if self.movement == True:
				if self.hit == True:
					if self.pos_x > int(largura/2):
						surface.blit(charHitR, (self.pos_x,self.pos_y))
					else:
						surface.blit(charHitL, (self.pos_x,self.pos_y))
				elif self.hitrelease == True:
					if self.pos_x > int(largura/2):
						for x in range(0,3):
							surface.blit(charHittedR[x], (self.pos_x,self.pos_y))
						self.hitrelease = False
						self.contador_passo = 0
					else:
						for x in range(0,3):
							surface.blit(charHittedL[x], (self.pos_x,self.pos_y))
						self.hitrelease = False
						
				else:
					surface.blit(charMovement[self.contador_passo//5], (self.pos_x,self.pos_y))
					self.contador_passo += 1
		
			else:
				if self.hit == True:
					if self.pos_x > int(largura/2):
						surface.blit(charHitR, (self.pos_x,self.pos_y))
					else:
						surface.blit(charHitL, (self.pos_x,self.pos_y))
				elif self.hitrelease == True:
					if self.pos_x > int(largura/2):
						for x in range(0,3):
							surface.blit(charHittedR[x], (self.pos_x,self.pos_y))
						self.hitrelease = False
					else:
						for x in range(0,3):
							surface.blit(charHittedL[x], (self.pos_x,self.pos_y))
						self.hitrelease = False
				else:
					surface.blit(char[self.contador_passo], (self.pos_x,self.pos_y))
					self.contador_passo += 1
		elif self.player == "2":
			if self.movement == True:
				if self.hit == True:
					if self.pos_x > int(largura/2):
						surface.blit(char2HitR, (self.pos_x,self.pos_y))
					else:
						surface.blit(char2HitL, (self.pos_x,self.pos_y))
				elif self.hitrelease == True:
					if self.pos_x > int(largura/2):
						for x in range(0,3):
							surface.blit(char2HittedR[x], (self.pos_x,self.pos_y))
						self.hitrelease = False
						self.contador_passo = 0
					else:
						for x in range(0,3):
							surface.blit(char2HittedL[x], (self.pos_x,self.pos_y))
						self.hitrelease = False
						
				else:
					surface.blit(char2Movement[self.contador_passo//5], (self.pos_x,self.pos_y))
					self.contador_passo += 1
		
			else:
				if self.hit == True:
					if self.pos_x > int(largura/2):
						surface.blit(char2HitR, (self.pos_x,self.pos_y))
					else:
						surface.blit(char2HitL, (self.pos_x,self.pos_y))
				elif self.hitrelease == True:
					if self.pos_x > int(largura/2):
						for x in range(0,3):
							surface.blit(char2HittedR[x], (self.pos_x,self.pos_y))
						self.hitrelease = False
					else:
						for x in range(0,3):
							surface.blit(char2HittedL[x], (self.pos_x,self.pos_y))
						self.hitrelease = False
				else:
					surface.blit(char2[self.contador_passo], (self.pos_x,self.pos_y))
					self.contador_passo += 1
		self.hitbox = (self.pos_x + 20,self.pos_y + 20, 28,40)
		self.forcebox = (self.pos_x + 20, self.pos_y - 5, self.force * 3,0)
		pygame.draw.rect(surface, (255,0,0), self.forcebox, 2)
		
		

	
		
		
#Classe da bola
class Ball:
	

	def __init__(self,x,y,sentido):
		self.pos_x = x
		self.pos_y = y
		self.altura = 10
		self.largura = 30
		self.sentido = sentido
		self.forca = 1
		self.velocidade = self.forca * sentido
		self.start = False
		self.field_distance = 0
		self.ball_sentido = 1
		self.hitbox = (self.pos_x ,self.pos_y, 10,10)
		self.direcao = 0
#Metodo que desenha a bola na tela
	def Draw(self,surface):
		surface.blit(ball, (self.pos_x,self.pos_y))
		surface.blit(ballShadow, (self.pos_x, self.pos_y + self.field_distance + 5))
		self.hitbox = (self.pos_x ,self.pos_y, 10,10)
		pygame.draw.rect(surface, (255,0,0),self.hitbox,2)
#Metodo que aplica movimento aos parametros x e y da bola
	def Moviment(self):
		if self.start == True:
			if self.sentido > 0:
				self.pos_y += self.velocidade
				self.pos_x += self.direcao * 5
			else:
				self.pos_y -= self.velocidade
				self.pos_x += self.direcao * 5
#Metodo que define onde devera se posicionar a bola, de acordo com parametros do Juiz
	def SetPosition(self,x,y):
		self.pos_x = x
		self.pos_y = y
#Metodo que define quando ocorrerá colisão e o que deverá acontecer com a bola
	def Hit(self,surface,player):
		ht_player = pygame.draw.rect(surface, (255,0,0),player.hitbox,2)
		ht_ball = pygame.draw.rect(surface, (255,0,0),self.hitbox,2)
		collision = ht_ball.colliderect(ht_player)
		if collision:
			self.start = True
			self.velocidade = player.force
			self.direcao = player.balldirection
			self.sentido = player.hitsentido
		
		
		
		
		
		
