TITLE = "The Night The Sky Got Weird"

def main():
    try:
        import pygame
    except Exception:
        print("pygame is not installed. Install with: pip install pygame")
        return

    pygame.init()

    # Fullscreen
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    size = screen.get_size()
    pygame.display.set_caption(TITLE)

    import os
    base_dir = os.path.dirname(__file__)

    # Background image
    bg_path = os.path.join(base_dir, "assets", "images", "night.jpeg")
    background = None
    if os.path.exists(bg_path):
        background = pygame.image.load(bg_path)
        background = pygame.transform.scale(background, size)

    # Fonts
    bundled_font = os.path.join(base_dir, "assets", "fonts", "bitend-font", "BitenddemoRegular-nA240.otf")
    try:
        if os.path.exists(bundled_font):
            font = pygame.font.Font(bundled_font, 60)   
            small_font = pygame.font.Font(bundled_font, 28)
        else:
            font = pygame.font.SysFont(None, 60)
            small_font = pygame.font.SysFont(None, 28)
    except Exception:
        font = pygame.font.Font(None, 60)
        small_font = pygame.font.Font(None, 28)

    # Main centered text
    text_surf = font.render(TITLE, True, (240, 240, 240))
    text_rect = text_surf.get_rect(center=(size[0] // 2, size[1] // 2))

    # Bottom-right credit
    credit_surf = small_font.render("vision by momena", True, (230, 230, 230))
    credit_rect = credit_surf.get_rect(bottomright=(size[0] - 20, size[1] - 20))

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        # Draw background
        if background:
            screen.blit(background, (0, 0))
        else:
            screen.fill((10, 10, 24))

        # Draw texts
        screen.blit(text_surf, text_rect)
        screen.blit(credit_surf, credit_rect)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()


if __name__ == "__main__":
    main()
