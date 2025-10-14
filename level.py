import pygame
from player import Player



class Level:
	"""Classe que representa o nível/fase do jogo"""

	def __init__(self):

		self.display_surface = pygame.display.get_surface()

		self.all_sprites = pygame.sprite.Group()





	def run(self, dt):
		"""Método executado a cada frame - atualiza e desenha tudo"""

		self.all_sprites.update(dt)

		self.all_sprites.draw(self.display_surface) 

