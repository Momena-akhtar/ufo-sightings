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

    # Typing effect variables
    typing_speed = 80  # ms per character
    title_shown_chars = 0
    last_update = pygame.time.get_ticks()

    # Credit text (fade-in)
    credit_text = "vision by momena"
    credit_base_surf = small_font.render(credit_text, True, (230, 230, 230))
    credit_rect = credit_base_surf.get_rect(bottomright=(size[0] - 20, size[1] - 20))
    credit_alpha = 0

    # Load generic button SVG from file
    button_svg_path = os.path.join(base_dir, "assets", "buttons", "button.svg")
    import cairosvg
    button_png = cairosvg.svg2png(url=button_svg_path)
    import io
    button_surface = pygame.image.load(io.BytesIO(button_png))
    button_surface = pygame.transform.scale(button_surface, (210, 70))  # Adjust button size
    button_rect = button_surface.get_rect(center=(size[0] // 2, size[1] // 2 + 100))

    # Render button text using heading font
    button_text = "BEGIN"
    button_text_surf = font.render(button_text, True, (255, 255, 255))
    button_text_rect = button_text_surf.get_rect(center=button_surface.get_rect().center)
    button_surface.blit(button_text_surf, button_text_rect)

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        now = pygame.time.get_ticks()

        # Typing logic
        if title_shown_chars < len(TITLE) and now - last_update > typing_speed:
            title_shown_chars += 1
            last_update = now

        cursor_visible = (now // 400) % 2 == 0 and title_shown_chars < len(TITLE)

        # Fade in credit after title completes
        if title_shown_chars == len(TITLE) and credit_alpha < 255:
            credit_alpha = min(255, credit_alpha + 3)

        # Draw bg
        if background:
            screen.blit(background, (0, 0))
        else:
            screen.fill((10, 10, 24))

        # Build title text
        current_text = TITLE[:title_shown_chars]
        if cursor_visible:
            current_text += "_"

        if current_text:
            text_surf = font.render(current_text, True, (240, 240, 240))
            text_rect = text_surf.get_rect(center=(size[0] // 2, size[1] // 2 - 120))
            screen.blit(text_surf, text_rect)

        # Fade-in credit
        if credit_alpha > 0:
            credit_surf = credit_base_surf.copy()
            credit_surf.set_alpha(credit_alpha)
            screen.blit(credit_surf, credit_rect)

        # Draw button
        screen.blit(button_surface, button_rect)

        # Handle button click
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()
        if button_rect.collidepoint(mouse_pos) and mouse_click[0]:
            print("BEGIN button clicked!")

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
