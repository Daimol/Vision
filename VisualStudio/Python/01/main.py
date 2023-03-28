import pygame

# Inicializace knihovny Pygame
pygame.init()

# Nastavení velikosti okna
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# Nastavení názvu okna
pygame.display.set_caption("Ovládání pomocí kláves")

# Počáteční pozice hráče
player_x = screen_width // 2
player_y = screen_height // 2

# Pomocné proměnné pro uchování stavu kláves
key_up_pressed = False
key_down_pressed = False
key_left_pressed = False
key_right_pressed = False

# Čas poslední iterace smyčky
last_tick = pygame.time.get_ticks()

# Hlavní smyčka programu
running = True
while running:
    # Procházení událostí (klávesnice, myš)
    for event in pygame.event.get():
        # Pokud byla stisknuta klávesa Escape, ukončit program
        if event.type == pygame.QUIT:
            running = False

        # Pohyb hráče pomocí kláves W, A, S a D
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                key_up_pressed = True
            elif event.key == pygame.K_s:
                key_down_pressed = True
            elif event.key == pygame.K_a:
                key_left_pressed = True
            elif event.key == pygame.K_d:
                key_right_pressed = True

        # Zastavení pohybu hráče po uvolnění klávesy
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                key_up_pressed = False
            elif event.key == pygame.K_s:
                key_down_pressed = False
            elif event.key == pygame.K_a:
                key_left_pressed = False
            elif event.key == pygame.K_d:
                key_right_pressed = False

    # Výpočet časového rozdílu od poslední iterace smyčky
    current_tick = pygame.time.get_ticks()
    time_diff = current_tick - last_tick
    last_tick = current_tick

    # Pohyb hráče podle stisknutých kláves s rychlostí 50 pixelů za sekundu
    if key_up_pressed:
        player_y -= 50 * (time_diff / 1000)
    if key_down_pressed:
        player_y += 50 * (time_diff / 1000)
    if key_left_pressed:
        player_x -= 50 * (time_diff / 1000)
    if key_right_pressed:
        player_x += 50 * (time_diff / 1000)

    # Vyplnění pozadí bílou barvou
    screen.fill((255, 255, 255))

    # Vykreslení hráče na obrazovku
    pygame.draw.circle(screen, (255, 0, 0), (player_x, player_y), 20)

    # Obnovení obsahu obrazovky
    pygame.display.flip()

# Ukončení programu a Pygame
pygame.quit()