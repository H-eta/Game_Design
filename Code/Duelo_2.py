import pygame
import os

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# player = pygame.Rect((100, 400, 50, 50))
#judge = pygame.Rect((600, 80, 80, 80))
barra = pygame.Rect((0, 220, 800, 120))
guia = pygame.Rect((300, 205, 200, 150))

# moving_rect = pygame.Rect((barra.left, barra.centery - 25, 50, 50))  # Posicionando o retângulo dentro da barra

moving_rect1 = pygame.Rect((800, barra.centery - 25, 50, 50))  # Posicionando o retângulo dentro da barra
moving_rect2 = pygame.Rect((800 + 150, barra.centery - 25, 50, 50))  # Segundo retângulo com deslocamento
moving_rect3 = pygame.Rect((800 + 300, barra.centery - 25, 50, 50))
moving_rect4 = pygame.Rect((800 + 450, barra.centery - 25, 50, 50))

# Contador de frames e frequência de movimento
# frame_count = 0
# move_frequency = 20  # Mova o retângulo a cada 60 frames (menor número = movimento mais lento)

script_dir = os.path.dirname(__file__)
game_design_dir = os.path.dirname(os.path.dirname(script_dir))

frames_dir_3 = os.path.join(game_design_dir, 'Game_Design', 'Sprites', 'judges')
judge_path = os.path.join(frames_dir_3, f'judge.png')
judge = pygame.image.load(judge_path)
judge = pygame.transform.scale(judge, (judge.get_width() * 1.2, judge.get_height() * 1.2))

frames_dir = os.path.join(game_design_dir, 'Game_Design', 'Animations', 'animation_chris_walking')
frames = []
# Carrega cada quadro da animação de forma isolada
for i in range(4):
    frame_path = os.path.join(frames_dir, f'tile00{i}.png')
    frame = pygame.image.load(frame_path)
    frame = pygame.transform.scale(frame, (frame.get_width() * 4, frame.get_height() * 4))
    frames.append(frame)

frame_index = 0

frames_dir_2 = os.path.join(game_design_dir, 'Game_Design', 'Animations', 'judge_judging_animation_10_color')
frames_2 = []
# Carrega cada quadro da animação de forma isolada
for i in range(6):
    frame_path = os.path.join(frames_dir_2, f'tile00{i}.png')
    frame = pygame.image.load(frame_path)
    frame = pygame.transform.scale(frame, (frame.get_width() * 2, frame.get_height() * 2))
    frames_2.append(frame)

frame_index_2 = 0

player_x = 80
player_y = 380

judge_x = 520
judge_y = -15

frame_count = 0
frame_count_1 = 0
frame_count_2 = 0
frame_switch_frequency = 10
frame_switch_frequency_1 = 1
frame_switch_frequency_2 = 12

font = pygame.font.Font(None, 36)
letters = ['W', 'S', 'A', 'D']

animacao_ativa = False
run = True
clock = pygame.time.Clock()
while run:

    clock.tick(60)

    screen.fill((180, 90, 70))

    # pygame.draw.rect(screen, (152, 152, 152), player)
    #pygame.draw.rect(screen, (255, 255, 0), judge)
    pygame.draw.rect(screen, (200, 200, 200), barra)
    pygame.draw.rect(screen, (250, 250, 250), guia, 10)

    # pygame.draw.rect(screen, (152, 152, 152), moving_rect)

    screen.blit(frames[frame_index], (player_x, player_y))

    screen.blit(judge, (judge_x, judge_y))

    pygame.draw.rect(screen, (150, 100, 150), moving_rect1)
    pygame.draw.rect(screen, (50, 128, 128), moving_rect2)  # Diferente cor para o segundo retângulo
    pygame.draw.rect(screen, (100, 110, 150), moving_rect3)
    pygame.draw.rect(screen, (110, 80, 80), moving_rect4)

    for i, rect in enumerate([moving_rect1, moving_rect2, moving_rect3, moving_rect4]):
        letter_surface = font.render(letters[i], True, (255, 255, 255))
        text_rect = letter_surface.get_rect(center=rect.center)  # Centraliza o texto no retângulo
        screen.blit(letter_surface, text_rect.topleft)

    # Incrementa o contador de frames
    frame_count += 1
    frame_count_1 += 1

    if frame_count >= frame_switch_frequency:
        frame_index += 1
        if frame_index >= len(frames):
            frame_index = 0
        frame_count = 0

    if animacao_ativa:
        frame_count_2 += 1
        if frame_count_2 >= frame_switch_frequency_2:
            frame_index_2 += 1
            if frame_index_2 >= len(frames_2):
                frame_index_2 = 0
                animacao_ativa= False
            frame_count_2 = 0
        screen.blit(frames_2[frame_index_2], (judge_x, judge_y))

    # Se o contador de frames alcançar a frequência de movimento, mova o retângulo e redefina o contador
    if frame_count_1 >= frame_switch_frequency_1:
        moving_rect1.x -= 1  # Move o primeiro retângulo para a esquerda
        moving_rect2.x -= 1  # Move o segundo retângulo para a esquerda com um deslocamento de atraso
        moving_rect3.x -= 1
        moving_rect4.x -= 1
        frame_count_1 = 0  # Redefine o contador de frames

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
        animacao_ativa = True
        if player_x > 60:
            player_x = player_x - 3
    elif key[pygame.K_d]:
        animacao_ativa = True
        if player_x < 100:
            player_x = player_x + 3
    elif key[pygame.K_w]:
        animacao_ativa = True
        if player_y > 360:
            player_y = player_y - 3
    elif key[pygame.K_s]:
        animacao_ativa = True
        if player_y < 400:
            player_y = player_y + 3


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
