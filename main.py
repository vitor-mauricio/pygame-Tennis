from classes import *
from settings import *
import pygame



bg = pygame.image.load('bg12.png')
#Classe Pai dos Placares
class Score:
	def __init__(self):
		self.p1_score = 0
		self.p2_score = 0
		
	def AddScore(self,player,add):
		if player == 1:
			self.p1_score += add
		elif player == 2:
			self.p2_score += add
#Classe que comanda quem saca e as posicoes de todos os objetos envolvidos no Tênis
class Juiz:
	
	def __init__(self):
		self.p1_position = 1
		self.p2_position = 1
		self.ballposition = 1
		self.whosaque = 1

	def SetPlayers(self):
		if self.p1_position >= 2 or self.p2_position >= 2: 
			self.p1_position -= 1
			self.p2_position -= 1
			print("diminiu")
		else:
			self.p1_position += 1
			self.p2_position += 1
			print("aumentou")
		if self.whosaque == 1:
			self.whosaque += 1
		else:
			self.whosaque -= 1
		
#Classe que define como o placar Score adiciona seus pontos, se desenha no display etc
class GameScore(Score):

	def __init__(self):
		super().__init__()
		self.font_padrao = pygame.font.get_default_font()
		self.fonte_placar = pygame.font.SysFont(self.font_padrao,45)
		self.fonte_player = pygame.font.SysFont(self.font_padrao,20)
		self.deuce = False
		self.playerwin = 0
		
	
	def DrawWhoSaque(self):
		pass
	def Draw(self,fundo):
		self.placar_score1 = self.fonte_placar.render(str(self.p1_score),1,(255,255,255))
		self.placar_score2 = self.fonte_placar.render(str(self.p2_score),1,(255,255,255))

		self.placar_player1 = self.fonte_player.render("PLAYER 1",1,(255,255,255))
		self.placar_player2 = self.fonte_player.render("PLAYER 2",1,(255,255,255))
		fundo.blit(self.placar_score1,(150,150))
		fundo.blit(self.placar_score2,(150,100))

		fundo.blit(self.placar_player1,(50,160))
		fundo.blit(self.placar_player2,(50,105))
		self.DrawWhoSaque()

	def AddScore(self,player):
		if player == 1:
			if self.p1_score >= 30:
				super().AddScore(player,10)
			else:
				super().AddScore(player,15)
		elif player == 2:
			if self.p2_score >= 30:
				print("ola")
				super().AddScore(player,10)
			else:
				super().AddScore(player,15)
	def TestWin(self):
		if self.p1_score > 40:
			self.p1_score = 0
			self.playerwin = 1
		elif self.p2_score > 40:
			self.p2_score = 0
			self.playerwin = 2
		elif self.p1_score == 40 and self.p2_score == 40:
			self.Deuce()
	def Deuce(self):
		return True
#Classe que define como o placar dos Games funcionam e como se desenha no display
class SetScore(Score):
	
	def __init__(self):
		super().__init__()
		self.font_padrao = pygame.font.get_default_font()
		self.fonte_placar = pygame.font.SysFont(self.font_padrao,45)
		self.win = False

	def AddScore(self,playerwin):

		if playerwin == 1:
			super().AddScore(1,1)
			self.win = True
			print(self.win)
			print("P1 GANHOU")
		
		elif playerwin == 2:
			super().AddScore(1,1)
			self.win = True
			print("p2 ganhou")
			print(self.win)
		
	def Draw(self,fundo):
		self.placar_game1 = self.fonte_placar.render(str(self.p1_score),1,(255,255,40))
		self.placar_game2 = self.fonte_placar.render(str(self.p2_score),1,(255,255,40))
		fundo.blit(self.placar_game1,(130,150))
		fundo.blit(self.placar_game2,(130,100))
#Classe que trata o cenário de 'Deuce', iguais no Tênis
class DeuceScore(Score):
	def __init__(self):
		super().__init__()
		self.font_padrao  = pygame.font.get_default_font()
		self.fonte_placar = pygame.font.SysFont(self.font_padrao,45)
		self.win = False
		self.p1_score = "40"
		self.p2_score = "40"
	
	def AddScore(self,playerwin):
		if playerwin == 1:
			if self.p1_score == "40":
				if self.p2_score == "AD":
					self.p1_score = "40"
					self.p2_score = "40"
				else:
					self.p1_score = "AD"
			elif self.p1_score == "AD":
				return 1
		elif playerwin == 2:
			if self.p2_score == "40":
				if self.p1_score == "AD":
					self.p1_score = "40"
					self.p2_score = "40"
				else:
					self.p2_score = "AD"
			elif self.p2_score == "AD":
				return 2
#Classe 'main' do Game. Contem metodos que comandam a ação dos objetos, comportamento de display/eventos etc
class Game:
	
	def __init__(self):
		pygame.init()
		self.fundo = pygame.display.set_mode((largura,altura))
		self.clock = pygame.time.Clock()
		pygame.font.init()
		self.placarScore = GameScore()
		self.placarGame = SetScore()
		self.player_saque = "1"
		self.juiz = Juiz()
		self.player1 = Player(int(largura/2 - 60),int(altura - 90),"1",-1)
		self.player2 = Player(int(largura/2 - 10),int(altura/4 - 120),"2",1)
		self.ball = Ball(self.player1.pos_x - 40,self.player1.pos_y,1)
		self.endgame = False
		self.win = False
		self.deuce = False
		
		#self.running = True
#método que especifica quando o jogo termina, no caso, quando um player atingir 5 games
	def GameEnd(self):
		if self.placarGame.p1_score >= 5:
			self.endgame = True
			return True
		elif self.placarGame.p2_score >= 5:
			self.endgame = True
			return True
#Metodo que controla o jogo
	def GameControl(self):
		while self.GameEnd() != True:
			self.win = False
			self.Juiz()
			print(self.juiz.p1_position)
			self.ball.start = False
			#Define as posições iniciais de cada Game de cada Player, de acordo com o Juiz
			self.player1.SetPosition(self.juiz.p1_position,1)
			self.player2.SetPosition(self.juiz.p2_position,2)

			self.Run()
#Metodo que define quando ocorre vitória por algum player
	def Win(self):
		if self.ball.pos_x < 0 and self.ball.pos_y < altura/2:
			self.placarScore.AddScore(1)		
			self.win = True
		if self.ball.pos_y < 0:			
			self.placarScore.AddScore(1)
			self.win = True
		if self.ball.pos_x > largura and self.ball.pos_y < altura/2:
			self.placarScore.AddScore(2)
			self.win = True
		if self.ball.pos_y > altura:
			self.placarScore.AddScore(2)
			self.win = True
#Metodo que faz o jogo funcionar, função RUN!. Ela chama os outros métodos de eventos e de desenho no display
	def Run(self):
		self.ball.SetPosition(self.player1.pos_x - 40,self.player1.pos_y)
		self.playing = True
		self.Draw()
		while self.playing:
			self.Events()
			self.Draw()
			if self.win == True:
				return
		
			
#Metodo que chama a funcionalidade do juiz
	def Juiz(self):
		if self.placarGame.win == True:
			self.juiz.SetPlayers()
			self.placarGame.win = False

#Metodo que comanda e trata todos os eventos uteis para o Tennis Game
	def Events(self):
		
		self.clock.tick(20)
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.playing = False
			self.MapHit(event)
		keys = pygame.key.get_pressed()
		self.ball.Moviment()
		self.MovimentsPlayer1(keys)
		self.MovimentsPlayer2(keys)
		self.Win()
		self.placarScore.TestWin()
		self.placarGame.AddScore(self.placarScore.playerwin)

		

		self.placarScore.playerwin = 0



	#Codigo que define o aumento da força gradativa enquanto o evento mouse released naõ for acionado
		if self.player1.hit == True:
			if self.player1.force >= 10:
				self.player1.force -= 1
			else:
				self.player1.force += 1
		if self.player2.hit == True:
			if self.player2.force >= 10:
				self.player2.force -= 1
			else:
				self.player2.force += 1


	def MapHit(self,event):
		#Map Hit do PLayer 1 - Mapeia quais teclas são utilizadas para bater na bola por cada player
		if event.type == pygame.KEYDOWN and event.key == pygame.K_RSHIFT:
				self.player1.force = 0
				self.player1.hit = True
	
		if event.type == pygame.KEYUP and event.key == pygame.K_RSHIFT:
			self.player1.hit = False
			self.player1.hitrelease = True
			print(self.player1.force)
			self.ball.Hit(self.fundo,self.player1)
		#Map hit do Player 2
		if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
				self.player2.force = 0
				self.player2.hit = True
	
		if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
			self.player2.hit = False
			self.player2.hitrelease = True
			print(self.player2.force)
			self.ball.Hit(self.fundo,self.player2)
		
		 
		

# Mapeamento de Teclas para a movimentação do Player1, jogador de baixo \/
	def MovimentsPlayer1(self,keys):
		if keys[pygame.K_LEFT] and self.player1.pos_x > 10:
			self.player1.movement = True
			self.player1.balldirection = -1
			if keys[pygame.K_LEFT] and keys[pygame.K_UP]:
				self.player1.pos_x -= 8
				self.player1.pos_y -= 8
			elif keys[pygame.K_LEFT] and keys[pygame.K_DOWN]:
				self.player1.pos_x -= 8
				self.player1.pos_y += 8
			elif keys[pygame.K_RSHIFT]:
				self.player1.hit = True
			else:
				self.player1.pos_x -= 10
		elif keys[pygame.K_RIGHT] and self.player1.pos_x < 1000:
			self.player1.movement = True
			self.player1.balldirection = 1
			if keys[pygame.K_RIGHT] and keys[pygame.K_UP]:
				self.player1.pos_x += 8
				self.player1.pos_y -= 8
			elif keys[pygame.K_RIGHT] and keys[pygame.K_DOWN]:
				self.player1.pos_x += 8
				self.player1.pos_y += 8
			elif keys[pygame.K_RSHIFT]:
				self.player1.hit = True
			else:
				self.player1.pos_x += 10
		elif keys[pygame.K_UP] and self.player1.pos_y > 10:
			self.player1.balldirection = 0
			self.player1.pos_y -= 10
			self.player1.movement = True
		elif keys[pygame.K_DOWN] and self.player1.pos_y < 1000:
			self.player1.balldirection = 0
			self.player1.pos_y += 8
			self.player1.movement = True
		else:
			self.player1.balldirection = 0
			self.player1.movement = False


# Mapeamento de Teclas para a movimentação do Player2, jogador de cima /\
	def MovimentsPlayer2(self,keys):
		if keys[pygame.K_a] and self.player2.pos_x > 10:
			self.player2.movement = True
			self.player2.balldirection = -1
			if keys[pygame.K_a] and keys[pygame.K_w]:
				print("opa")
				self.player2.pos_x -= 8
				self.player2.pos_y -= 8
			elif keys[pygame.K_a] and keys[pygame.K_s]:
				self.player2.pos_x -= 8
				self.player2.pos_y += 8
			elif keys[pygame.K_SPACE]:
				self.player2.hit = True
			else:
				self.player2.pos_x -= 10
		elif keys[pygame.K_d] and self.player2.pos_x < 1000:
			self.player2.movement = True
			self.player2.balldirection = 1
			if keys[pygame.K_d] and keys[pygame.K_w]:
				self.player2.pos_x += 8
				self.player2.pos_y -= 8
			elif keys[pygame.K_d] and keys[pygame.K_s]:
				self.player2.pos_x += 8
				self.player2.pos_y += 8
			elif keys[pygame.K_SPACE]:
				self.player2.hit = True
			else:
				self.player2.pos_x += 10
		elif keys[pygame.K_w] and self.player2.pos_y > -10:
			self.player2.balldirection = 0
			self.player2.pos_y -= 10
			self.player2.movement = True
		elif keys[pygame.K_s] and self.player2.pos_y < 1000:
			self.player2.balldirection = 0
			self.player2.pos_y += 8
			self.player2.movement = True
		else:
			self.player2.balldirection = 0
			self.player2.movement = False
#Metodo que desenha tudo no display, chamando, também, cada Objeto para se desenhar
	def Draw(self):
		self.fundo.blit(bg,(0,0))
		self.ball.Draw(self.fundo)
		self.player1.Draw(self.fundo)
		self.player2.Draw(self.fundo)
		self.placarScore.Draw(self.fundo)
		self.placarGame.Draw(self.fundo)
		pygame.display.update()
		
		
game = Game()
game.GameControl()

pygame.quit()
