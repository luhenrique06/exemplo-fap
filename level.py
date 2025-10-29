import pygame
from player import Player
from obstacle import Obstacle


class Level:
	"""Classe que representa o nível/fase do jogo"""

	def __init__(self):
		self.display_surface = pygame.display.get_surface()

		self.all_sprites = pygame.sprite.Group()

		self.obstacles = pygame.sprite.Group()


		self.player = Player(
			pos=(640, 360),
			groups=self.all_sprites,
		)


		Obstacle(pos=(400, 300), groups=[self.all_sprites, self.obstacles])
		Obstacle(pos=(250, 400), groups=[self.all_sprites, self.obstacles])
		Obstacle(pos=(699, 500), groups=[self.all_sprites, self.obstacles])


		self.game_over = False

	def check_collision(self):

		collisions = pygame.sprite.spritecollide(self.player, self.obstacles, True)

		if collisions:
			player_died = self.player.take_damage()


	def run(self, dt):
		"""Método executado a cada frame - atualiza e desenha tudo"""


		self.display_surface.fill('darkgreen')

		self.all_sprites.update(dt)


		self.check_collision()
		self.all_sprites.draw(self.display_surface)  

