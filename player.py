
import pygame
from settings import *



class Player(pygame.sprite.Sprite):
	"""Classe que representa o jogador controlável"""

	def __init__(self, pos, groups):

		super().__init__(groups)

		self.sprite_sheets = {
			'down': pygame.image.load('char/walk_Down.png').convert_alpha(),
			'up': pygame.image.load('char/walk_Up.png').convert_alpha(),
			'left_down': pygame.image.load('char/walk_Left_Down.png').convert_alpha(),
			'left_up': pygame.image.load('char/walk_Left_Up.png').convert_alpha(),
			'right_down': pygame.image.load('char/walk_Right_Down.png').convert_alpha(),
			'right_up': pygame.image.load('char/walk_Right_Up.png').convert_alpha()
		}

		self.animations = {}
		self.frame_count = 8
		self.scale_factor = 2  
		for direction, sheet in self.sprite_sheets.items():
			frames = []
			frame_width = sheet.get_width() // self.frame_count
			frame_height = sheet.get_height()
			for i in range(self.frame_count):
				frame = sheet.subsurface((i * frame_width, 0, frame_width, frame_height))
				scaled_frame = pygame.transform.scale(frame,
					(frame_width * self.scale_factor, frame_height * self.scale_factor))
				frames.append(scaled_frame)
			self.animations[direction] = frames

		# Controle de animação
		self.current_direction = 'down'
		self.frame_index = 0
		self.animation_speed = 10  # Frames por segundo da animação
		self.animation_timer = 0

		self.image = self.animations[self.current_direction][self.frame_index]
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

	def update_sprite(self, dt):
		"""Atualiza a sprite baseado na direção do movimento"""
		if self.direction.magnitude() > 0:
			
			if self.direction.y > 0: 
				if self.direction.x > 0:
					self.current_direction = 'right_down'
				elif self.direction.x < 0:
					self.current_direction = 'left_down'
				else:
					self.current_direction = 'down'
			elif self.direction.y < 0:  
				if self.direction.x > 0:
					self.current_direction = 'right_up'
				elif self.direction.x < 0:
					self.current_direction = 'left_up'
				else:
					self.current_direction = 'up'
			elif self.direction.x > 0:  
				self.current_direction = 'right_down'
			elif self.direction.x < 0:  
				self.current_direction = 'left_down'

			
			self.animation_timer += dt * self.animation_speed
			if self.animation_timer >= 1:
				self.animation_timer = 0
				self.frame_index = (self.frame_index + 1) % self.frame_count
		else:
			
			self.frame_index = 0

	
		self.image = self.animations[self.current_direction][self.frame_index]

	def move(self, dt):
		"""Move o personagem baseado na direção e velocidade"""

		self.pos.x += self.direction.x * self.speed * dt
		self.pos.y += self.direction.y * self.speed * dt

		self.rect.centerx = round(self.pos.x)
		self.rect.centery = round(self.pos.y)


	def update(self, dt):
		"""Método chamado a cada frame"""
		self.input()
		self.update_sprite(dt)
		self.move(dt)     


