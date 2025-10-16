
import pygame
from settings import *



class Player(pygame.sprite.Sprite):
	"""Classe que representa o jogador controlável"""

	def __init__(self, pos, groups):
		
		super().__init__(groups)

		self.image = pygame.Surface((64, 64))  
		self.image.fill('blue')  

		self.rect = self.image.get_rect(center=pos)

		self.pos = pygame.math.Vector2(self.rect.center)
		self.direction = pygame.math.Vector2(0, 0) 
		self.speed = 200


	def input(self):
		"""Captura as teclas pressionadas e define a direção do movimento"""
		keys = pygame.key.get_pressed()


		self.direction.x = 0
		self.direction.y = 0

		if keys[pygame.K_UP] or keys[pygame.K_w]:
			self.direction.y = -1
		if keys[pygame.K_DOWN] or keys[pygame.K_s]:
			self.direction.y = 1
		if keys[pygame.K_LEFT] or keys[pygame.K_a]:
			self.direction.x = -1
		if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
			self.direction.x = 1

		if self.direction.magnitude() > 0:
			self.direction = self.direction.normalize()	

	def move(self, dt):
		"""Move o personagem baseado na direção e velocidade"""

		self.pos.x += self.direction.x * self.speed * dt
		self.pos.y += self.direction.y * self.speed * dt

		self.rect.centerx = round(self.pos.x)
		self.rect.centery = round(self.pos.y)


	def update(self, dt):
		"""Método chamado a cada frame"""
		self.input()    
		self.move(dt)     


