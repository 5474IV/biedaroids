import pygame
import constants as c
from logger import log_state
from player import Player

def main():
	pygame.init()
	clock = pygame.time.Clock()
	dt = 0
	
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	Player.containers = (updatable, drawable)

	screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
	player = Player(c.SCREEN_WIDTH / 2, y = c.SCREEN_HEIGHT / 2)
	

	while(True):
		log_state()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill("black")
		updatable.update(dt)
		for drawing in drawable:
			drawing.draw(screen)
		pygame.display.flip()
		dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
