import pygame
import constants as c
from logger import log_state

def main():
	pygame.init()
	clock = pygame.time.Clock()
	dt = 0
	screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
	while(True):
		log_state()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill("black")
		pygame.display.flip()
		dt = clock.tick(60) / 1000
		print(dt)

if __name__ == "__main__":
    main()
