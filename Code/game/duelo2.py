import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = pygame.Rect((100, 400, 50, 50))
judge = pygame.Rect((600, 80, 80, 80))
barra = pygame.Rect((0, 220, 800, 120))
guia = pygame.Rect((300, 205, 200, 150))


#moving_rect = pygame.Rect((barra.left, barra.centery - 25, 50, 50))  # Posicionando o retângulo dentro da barra

moving_rect1 = pygame.Rect((800, barra.centery - 25, 50, 50))  # Posicionando o retângulo dentro da barra
moving_rect2 = pygame.Rect((800 + 150, barra.centery - 25, 50, 50))  # Segundo retângulo com deslocamento
moving_rect3 = pygame.Rect((800 + 300, barra.centery - 25, 50, 50))
moving_rect4 = pygame.Rect((800 + 450, barra.centery - 25, 50, 50))


# Contador de frames e frequência de movimento
frame_count = 0
move_frequency = 20  # Mova o retângulo a cada 60 frames (menor número = movimento mais lento)

run = True
while run:

    screen.fill((128, 50, 50))

    pygame.draw.rect(screen, (152, 152, 152), player)
    pygame.draw.rect(screen, (255, 255, 0), judge)
    pygame.draw.rect(screen, (200, 200, 200), barra)
    pygame.draw.rect(screen, (250, 250, 250), guia, 10)

    #pygame.draw.rect(screen, (152, 152, 152), moving_rect)

    pygame.draw.rect(screen, (152, 152, 152), moving_rect1)
    pygame.draw.rect(screen, (0, 255, 0), moving_rect2)  # Diferente cor para o segundo retângulo
    pygame.draw.rect(screen, (0, 255, 255), moving_rect3)
    pygame.draw.rect(screen, (255, 255, 0), moving_rect4)

    # Incrementa o contador de frames
    frame_count += 1

    # Se o contador de frames alcançar a frequência de movimento, mova o retângulo e redefina o contador
    if frame_count >= move_frequency:
        moving_rect1.x -= 1  # Move o primeiro retângulo para a esquerda
        moving_rect2.x -= 1  # Move o segundo retângulo para a esquerda com um deslocamento de atraso
        moving_rect3.x -= 1
        moving_rect4.x -= 1
        frame_count = 0  # Redefine o contador de frames

        # Verifica se os retângulos atingiram o lado esquerdo da barra
        if moving_rect1.right <= barra.left:
            moving_rect1.x = barra.right  # Reposiciona o primeiro retângulo para o lado direito da barra
        if moving_rect2.right <= barra.left:
            moving_rect2.x = barra.right  # Reposiciona o segundo retângulo para o lado direito da barra
        if moving_rect3.right <= barra.left:
            moving_rect3.x = barra.right
        if moving_rect4.right <= barra.left:
            moving_rect4.x = barra.right

    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
        if player.left > 80:
            player.move_ip(-1, 0)
    elif key[pygame.K_d]:
        if player.right < 200:
            player.move_ip(1, 0)
    elif key[pygame.K_w]:
        if player.top > 400:
            player.move_ip(0, -1)
    elif key[pygame.K_s]:
        if player.bottom < 520:
            player.move_ip(0, 1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()