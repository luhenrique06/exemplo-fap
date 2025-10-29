import pygame
from settings import *


class Obstacle(pygame.sprite.Sprite):
	"""
	Classe que representa um obstáculo no jogo.
	Quando o jogador colidir com um obstáculo, o jogo acaba (game over).
	"""

	def __init__(self, pos, groups):
		"""
		Inicializa o obstáculo
		Args:
			pos: tupla (x, y) com a posição do obstáculo
			groups: grupos de sprites aos quais o obstáculo pertence
		"""
		super().__init__(groups)


		self.image = pygame.Surface((64, 64))
		self.image.fill('red') 

		self.rect = self.image.get_rect(center=pos)
