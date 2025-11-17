
TITLE = "The Night The Sky Got Weird"

def main():
	try:
		import pygame
	except Exception:
		print("pygame is not installed. Install with: pip install pygame")
		return

	pygame.init()
	size = (800, 200)
	screen = pygame.display.set_mode(size)
	pygame.display.set_caption(TITLE)

	import os
	base_dir = os.path.dirname(__file__)
	bundled_font = os.path.join(base_dir, "assets", "fonts", "bitend-font", "BitenddemoRegular-nA240.otf")
	try:
		if os.path.exists(bundled_font):
			font = pygame.font.Font(bundled_font, 48)
		else:
			font = pygame.font.SysFont(None, 48)
	except Exception:
		# Final fallback
		font = pygame.font.Font(None, 48)

	text_surf = font.render(TITLE, True, (240, 240, 240))
	text_rect = text_surf.get_rect(center=(size[0] // 2, size[1] // 2))

	clock = pygame.time.Clock()
	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					running = False

		screen.fill((10, 10, 24))
		screen.blit(text_surf, text_rect)
		pygame.display.flip()
		clock.tick(30)

	pygame.quit()


if __name__ == "__main__":
	main()