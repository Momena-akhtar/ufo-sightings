import os
import io


def run_night_files(screen, size, bundled_font, small_font, background, base_dir):
    """Run a simple 'Night Files' scene on the provided screen.

    This reuses the existing Pygame window (does NOT create a new window).
    The function returns when the user clicks BACK or presses ESC.
    If the user closes the window, we call pygame.quit() and exit.
    """
    try:
        import pygame
        import cairosvg
    except Exception:
        print("Missing dependency for night_files scene. Make sure pygame and cairosvg are installed.")
        return

    clock = pygame.time.Clock()

    # Title
    title_text = "Night Files"
    try:
        title_font = pygame.font.Font(bundled_font, 72)
    except Exception:
        title_font = pygame.font.SysFont(None, 72)

    # Back button using the same svg button asset as intro
    button_svg_path = os.path.join(base_dir, "assets", "buttons", "button.svg")
    button_surface = None
    if os.path.exists(button_svg_path):
        try:
            button_png = cairosvg.svg2png(url=button_svg_path)
            button_surface = pygame.image.load(io.BytesIO(button_png))
            button_surface = pygame.transform.scale(button_surface, (180, 60))
        except Exception:
            button_surface = None

    if button_surface is None:
        # fallback: simple rect button
        button_surface = pygame.Surface((180, 60))
        button_surface.fill((40, 40, 80))

    back_text = "BACK"
    try:
        back_font = pygame.font.Font(bundled_font, 28)
        back_font.set_bold(True)
    except Exception:
        back_font = pygame.font.SysFont(None, 28)

    back_surf = back_font.render(back_text, True, (255, 255, 255))
    back_rect = button_surface.get_rect(center=(size[0] // 2, size[1] - 120))
    # center text on the button surface
    bt_rect = back_surf.get_rect(center=button_surface.get_rect().center)
    button_surface.blit(back_surf, bt_rect)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()

        # Draw
        if background:
            screen.blit(background, (0, 0))
        else:
            screen.fill((5, 5, 20))

        # Title
        title_surf = title_font.render(title_text, True, (240, 240, 240))
        title_rect = title_surf.get_rect(center=(size[0] // 2, 120))
        screen.blit(title_surf, title_rect)

        # Example body text (placeholder for 'night files' content)
        body_lines = [
            "This is the Night Files scene.",
            "Put your night-related content here (logs, images, etc.).",
        ]
        for i, line in enumerate(body_lines):
            surf = small_font.render(line, True, (220, 220, 220))
            rect = surf.get_rect(center=(size[0] // 2, 220 + i * 34))
            screen.blit(surf, rect)

        # Draw back button and handle click
        screen.blit(button_surface, back_rect)
        if back_rect.collidepoint(mouse_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            if mouse_click[0]:
                # simple debounce: wait until mouse released
                while pygame.mouse.get_pressed()[0]:
                    pygame.event.pump()
                    clock.tick(60)
                running = False
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        pygame.display.flip()
        clock.tick(60)
