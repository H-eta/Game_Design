import pygame
import os
import pyautogui

pygame.init()

screen_w, screen_h = pyautogui.size()
screen = pygame.display.set_mode((screen_w, screen_h), pygame.FULLSCREEN)

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN_MAP = (66, 82, 34)
BROWN_MAP = (46, 27, 21)

button_rect = pygame.Rect(screen_w - 100, 0, 100, 50)
font = pygame.font.Font(None, 36)

script_dir = os.path.dirname(__file__)
game_design_dir = os.path.dirname(os.path.dirname(script_dir))

#__________importar mapa de jogo nivel 1_____________
mapa_l2 = os.path.join(game_design_dir, 'Game_Design', 'Sprites', 'maps')
mapa_l2_path = os.path.join(mapa_l2, f'map_circle_II_lust_not_finished_v3.png')
mapa_l2_original = pygame.image.load(mapa_l2_path).convert_alpha()

#__________importar animação do player_______________
player_walk_dir = os.path.join(game_design_dir, 'Game_Design', 'Animations', 'animation_chris_walking_front_pov_fixed')
player_walk = []
# Carrega cada quadro da animação de forma isolada
for i in range(4):
    frame_path = os.path.join(player_walk_dir, f'tile00{i}.png')
    frame = pygame.image.load(frame_path).convert_alpha()
    frame_w = frame.get_width()
    frame_h = frame.get_height()
    frame = pygame.transform.scale(frame, (frame.get_width() * 5, frame.get_height() * 5))
    player_walk.append(frame)
frame_index_player = 0

#__________importar animação do player rotate_______________
player_rotate_dir = os.path.join(game_design_dir, 'Game_Design', 'Animations', 'animation_chris_rotating')
player_rotate = []
# Carrega cada quadro da animação de forma isolada
for i in range(4):
    frame_path = os.path.join(player_rotate_dir, f'tile00{i}.png')
    frame = pygame.image.load(frame_path).convert_alpha()
    frame_w = frame.get_width()
    frame_h = frame.get_height()
    frame = pygame.transform.scale(frame, (frame.get_width() * 5, frame.get_height() * 5))
    player_rotate.append(frame)
frame_index_player_rotate = 0

#__________importar animação do NPC1_______________
npc1_walk_dir = os.path.join(game_design_dir, 'Game_Design', 'Animations', 'Lust_NPC_Francesca')
npc1_walk = []
# Carrega cada quadro da animação de forma isolada
for i in range(4):
    frame_path = os.path.join(npc1_walk_dir, f'tile00{i}.png')
    frame = pygame.image.load(frame_path).convert_alpha()
    frame_w = frame.get_width()
    frame_h = frame.get_height()
    frame = pygame.transform.scale(frame, (frame.get_width() * 5, frame.get_height() * 5))
    npc1_walk.append(frame)
frame_index_npc1 = 0

#__________importar animação do vortice_______________
vortice_dir = os.path.join(game_design_dir, 'Game_Design', 'Animations', 'map_lust_vortex_souls_animation')
vortice = []
# Carrega cada quadro da animação de forma isolada
for i in range(9):
    frame_path = os.path.join(vortice_dir, f'tile00{i}.png')
    frame = pygame.image.load(frame_path).convert_alpha()
    frame_w = frame.get_width()
    frame_h = frame.get_height()
    frame = pygame.transform.scale(frame, (frame.get_width() * 4, frame.get_height() * 4))
    vortice.append(frame)
frame_index_vortice = 0

#__________importar intro do mapa_______________
intro_map = os.path.join(game_design_dir, 'Game_Design', 'Sprites', 'map_intro')
intro_map_path = os.path.join(intro_map, f'lust_intro.png')
intro_map = pygame.image.load(intro_map_path).convert_alpha()
intro_map = pygame.transform.scale(intro_map, (intro_map.get_width() * 0.8, intro_map.get_height() * 0.8))
alpha_intro_map = 0  # Nível de transparência inicial

# Define o fator de zoom
zoom_factor = 4

# Redimensiona o mapa original com o fator de zoom
mapa_l2 = pygame.transform.scale(mapa_l2_original, (mapa_l2_original.get_width() * zoom_factor, mapa_l2_original.get_height() * zoom_factor))

# Define a posição inicial do mapa na tela (centro da tela)
mapa_x = -570
mapa_y = -600

#_________deslocação do player_______________
desl_player = 15
player_x = (screen_w - player_walk[0].get_width()) // 2
#player_y = (screen_h - player_walk[0].get_height()) // 2
player_y = 250

#________posicao incial do npc1________
npc1_x = 600
npc1_y = 2250

#________posicao incial do vortice________
vortice_x = 1900
vortice_y = 0

#________posicao incial do intro mapa________
intro_map_x = 0
intro_map_y = -80

clock = pygame.time.Clock()
set_judge = False
danca = False
danca_init = False
passar_nivel = False
intro = False
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Verifica se o clique do mouse foi dentro do botão "Sair"
            if button_rect.collidepoint(event.pos):
                run = False

#_________________deslocaao do player_______________
    # Obtém as teclas pressionadas
    keys = pygame.key.get_pressed()
    if player_y != (screen_h - player_walk[0].get_height()) // 2:
        player_y += 5
    elif danca == False:
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            if not(mapa_x > -1260 and mapa_y > -600):
                mapa_y += desl_player
                npc1_y += desl_player
                vortice_y += desl_player
                intro_map_y += desl_player
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            mapa_y -= desl_player
            npc1_y -= desl_player
            vortice_y -= desl_player
            intro_map_y -= desl_player
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            if not (mapa_x > -1275 and mapa_y > -580):
                mapa_x += desl_player
                npc1_x += desl_player
                vortice_x += desl_player
                intro_map_x += desl_player
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            mapa_x -= desl_player
            npc1_x -= desl_player
            vortice_x -= desl_player
            intro_map_x -= desl_player
        if danca == False and mapa_x>-100:
            mapa_x -= desl_player
            npc1_x -= desl_player
            vortice_x -= desl_player
            intro_map_x -= desl_player
        if danca == False and mapa_x < -3730:
            mapa_x += desl_player
            npc1_x += desl_player
            vortice_x += desl_player
            intro_map_x += desl_player
        if danca == False and mapa_y > 2:
            mapa_y -= desl_player
            npc1_y -= desl_player
            vortice_y -= desl_player
            intro_map_y -= desl_player
        if danca == False and mapa_y < -3400:
            mapa_y += desl_player
            npc1_y += desl_player
            vortice_y += desl_player
            intro_map_y += desl_player


    print(mapa_x, mapa_y)

    screen.fill(BROWN_MAP)

    # Desenha o mapa na posição correta
    screen.blit(mapa_l2, (mapa_x, mapa_y))

    # ____________desenhar npc1_________________________
    # Desenha o npc1 na posição correta
    frame_index_npc1 += 0.25
    if frame_index_npc1 >= len(npc1_walk):
        frame_index_npc1 = 0
    screen.blit(npc1_walk[int(frame_index_npc1)], (npc1_x, npc1_y))

    # ____________desenhar vortice_________________________
    frame_index_vortice += 0.25
    if frame_index_vortice >= len(vortice):
        frame_index_vortice = 0
    screen.blit(vortice[int(frame_index_vortice)], (vortice_x, vortice_y))

    # ____________desenhar jogador_________________________
    if mapa_x < -1980 and mapa_x > -3360 and mapa_y < -400 and mapa_y > -1440:
        frame_index_player_rotate += 0.2
        if frame_index_player_rotate >= len(player_rotate):
            frame_index_player_rotate = 0
        screen.blit(player_rotate[int(frame_index_player_rotate)], (player_x, player_y))
    else:
        frame_index_player += 0.25
        if frame_index_player >= len(player_walk):
            frame_index_player = 0
        screen.blit(player_walk[int(frame_index_player)], (player_x, player_y))

    #________apresentar intro do mapa__________
    if player_y == (screen_h - player_walk[0].get_height()) // 2:
        intro_map.set_alpha(alpha_intro_map)
        if intro == False:
            alpha_intro_map += 5
        if alpha_intro_map > 255 or intro == True:
            if alpha_intro_map > -1:
                alpha_intro_map -= 5
            intro = True
        screen.blit(intro_map, (intro_map_x, intro_map_y))

    # ____________botao de sair_____________________________
    # Desenha o botão "Sair"
    pygame.draw.rect(screen, RED, button_rect)

    # Adiciona texto ao botão "Sair"
    text_surface = font.render("Sair", True, WHITE)
    text_rect = text_surface.get_rect(center=button_rect.center)
    screen.blit(text_surface, text_rect)

    pygame.display.update()

    clock.tick(30)

pygame.quit()