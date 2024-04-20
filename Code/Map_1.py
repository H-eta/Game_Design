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

button_rect = pygame.Rect(screen_w-100, 0, 100, 50)
rect_battle1 = pygame.Rect(0, 0, screen_w, 160)
rect_battle2 = pygame.Rect(0, screen_h-160, screen_w, 160)
font = pygame.font.Font(None, 36)

script_dir = os.path.dirname(__file__)
game_design_dir = os.path.dirname(os.path.dirname(script_dir))

#__________importar mapa de jogo nivel 1_____________
mapa_l1 = os.path.join(game_design_dir, 'Game_Design', 'Sprites', 'maps')
#mapa_l1_path = os.path.join(mapa_l1, f'map_circle_I_limbo.png')
mapa_l1_path = os.path.join(mapa_l1, f'map_circle_I_limbo_3.png')
mapa_l1_original = pygame.image.load(mapa_l1_path)

#__________importar animação do player_______________
player_walk_dir = os.path.join(game_design_dir, 'Game_Design', 'Animations', 'animation_chris_walking_front_pov_fixed')
player_walk = []
# Carrega cada quadro da animação de forma isolada
for i in range(4):
    frame_path = os.path.join(player_walk_dir, f'tile00{i}.png')
    frame = pygame.image.load(frame_path)
    frame_w = frame.get_width()
    frame_h = frame.get_height()
    frame = pygame.transform.scale(frame, (frame.get_width() * 5, frame.get_height() * 5))
    player_walk.append(frame)
frame_index_player = 0

#__________importar animação do NPC1_______________
npc1_walk_dir = os.path.join(game_design_dir, 'Game_Design', 'Animations', 'Limbo_NPC_Socrates_fixed')
npc1_walk = []
# Carrega cada quadro da animação de forma isolada
for i in range(4):
    frame_path = os.path.join(npc1_walk_dir, f'tile00{i}.png')
    frame = pygame.image.load(frame_path)
    frame_w = frame.get_width()
    frame_h = frame.get_height()
    frame = pygame.transform.scale(frame, (frame.get_width() * 5, frame.get_height() * 5))
    npc1_walk.append(frame)
frame_index_npc1 = 0

#__________importar animação do NPC2_______________
npc2_walk_dir = os.path.join(game_design_dir, 'Game_Design', 'Animations', 'Limbo_NPC_Horace_fixed')
npc2_walk = []
# Carrega cada quadro da animação de forma isolada
for i in range(4):
    frame_path = os.path.join(npc2_walk_dir, f'tile00{i}.png')
    frame = pygame.image.load(frame_path)
    frame_w = frame.get_width()
    frame_h = frame.get_height()
    frame = pygame.transform.scale(frame, (frame.get_width() * 5, frame.get_height() * 5))
    npc2_walk.append(frame)
frame_index_npc2 = 0

#__________importar animação do NPC3_______________
npc3_walk_dir = os.path.join(game_design_dir, 'Game_Design', 'Animations', 'Limbo_NPC_Homero_fixed')
npc3_walk = []
# Carrega cada quadro da animação de forma isolada
for i in range(4):
    frame_path = os.path.join(npc3_walk_dir, f'tile00{i}.png')
    frame = pygame.image.load(frame_path)
    frame_w = frame.get_width()
    frame_h = frame.get_height()
    frame = pygame.transform.scale(frame, (frame.get_width() * 5, frame.get_height() * 5))
    npc3_walk.append(frame)
frame_index_npc3 = 0

#________importacao do judge___________
judge_1 = os.path.join(game_design_dir, 'Game_Design', 'Sprites', 'judges')
judge_1_path = os.path.join(judge_1, f'judge.png')
judge_1 = pygame.image.load(judge_1_path)
judge_1 = pygame.transform.scale(judge_1, (judge_1.get_width() * 1.2, judge_1.get_height() * 1.2))

#________importacao do barco___________
boat = os.path.join(game_design_dir, 'Game_Design', 'Sprites', 'limbo_boat')
boat_path = os.path.join(boat, f'boat.png')
boat = pygame.image.load(boat_path)
boat = pygame.transform.scale(boat, (boat.get_width() * 5, boat.get_height() * 5))

#_______importacao balao npc1_________
balao_npc1 = os.path.join(game_design_dir, 'Game_Design', 'Sprites', 'limbo_lines')
balao_npc1_path = os.path.join(balao_npc1, f'limbo_npc_line_1.png')
balao_npc1 = pygame.image.load(balao_npc1_path)
balao_npc1 = pygame.transform.scale(balao_npc1, (balao_npc1.get_width() * 4, balao_npc1.get_height() * 4))

#_______importacao balao npc2_________
balao_npc2 = os.path.join(game_design_dir, 'Game_Design', 'Sprites', 'limbo_lines')
balao_npc2_path = os.path.join(balao_npc2, f'limbo_npc_line_2.png')
balao_npc2 = pygame.image.load(balao_npc2_path)
balao_npc2 = pygame.transform.scale(balao_npc2, (balao_npc2.get_width() * 4, balao_npc2.get_height() * 4))

#_______importacao balao npc3_________
balao_npc3 = os.path.join(game_design_dir, 'Game_Design', 'Sprites', 'limbo_lines')
balao_npc3_path = os.path.join(balao_npc3, f'limbo_npc_line_3.png')
balao_npc3 = pygame.image.load(balao_npc3_path)
balao_npc3 = pygame.transform.scale(balao_npc3, (balao_npc3.get_width() * 4, balao_npc3.get_height() * 4))

#_______importacao balao judge 1_________
balao_judge_1 = os.path.join(game_design_dir, 'Game_Design', 'Sprites', 'limbo_lines')
balao_judge_1_path = os.path.join(balao_judge_1, f'limbo_judge_line_1.png')
balao_judge_1 = pygame.image.load(balao_judge_1_path)
balao_judge_1 = pygame.transform.scale(balao_judge_1, (balao_judge_1.get_width() * 4, balao_judge_1.get_height() * 4))

# Define o fator de zoom
zoom_factor = 1

# Redimensiona o mapa original com o fator de zoom
mapa_l1 = pygame.transform.scale(mapa_l1_original, (mapa_l1_original.get_width() * zoom_factor, mapa_l1_original.get_height() * zoom_factor))

# Define a porcentagem da margem em relação à largura e altura da tela
#mapa_margin_percent_w = 38  # 15% da largura da tela
#mapa_margin_percent_h = 28  # 15% da altura da tela

# Calcula a margem do mapa em relação à tela
#mapa_margin_w = int(screen_w * mapa_margin_percent_w / 100)
#mapa_margin_h = int(screen_h * mapa_margin_percent_h / 100)

# Define a posição inicial do mapa na tela (centro da tela)
mapa_x = -820
mapa_y = -300

#_________deslocação do player_______________
desl_player = 15
player_x = (screen_w - player_walk[0].get_width()) // 2
#player_y = (screen_h - player_walk[0].get_height()) // 2
player_y = -275

#________posicao incial do judge________
judge_x = 3160
judge_y = 3910

#________posicao incial do npc1________
npc1_x = 300
npc1_y = 2900

#________posicao incial do npc2________
npc2_x = 3550
npc2_y = 260

#________posicao incial do npc3________
npc3_x = 3730
npc3_y = 2530

#________posição inicial do barco______
boat_x = player_x-120
boat_y = player_y

#________transparencia das setas_________
alpha = 0  # Nível de transparência inicial
delta_alpha = 2  # Incremento/decremento na opacidade

#_______sequencia de danca_________
sequence=0
lista_teclas = ["up", "down", "left", "right"]
count_acertos = 0

#_________import da musica da danca_______
# Caminho para o diretório do script atual
sound_1_file = os.path.join(game_design_dir, 'Game_Design', 'Music', '7_teste.mp3')
sound_1 = pygame.mixer.Sound(sound_1_file)
sound_1_play = True

clock = pygame.time.Clock()
set_judge = False
danca = False
danca_init = False
passar_nivel = False
check_npc1 = False
check_npc2 = False
check_npc3 = False
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Verifica se o clique do mouse foi dentro do botão "Sair"
            if button_rect.collidepoint(event.pos):
                run = False
        elif event.type == pygame.KEYDOWN:
            # Verifica se a tecla pressionada foi a tecla "Esc"
            if event.key == pygame.K_ESCAPE:
                sound_1.stop()
                danca = False
                danca_init = False
                sound_1_play = True
                if set_judge == True:
                    judge_x -= 250
                    judge_y += 400
                    set_judge = False

#_________________deslocaao do player_______________
    # Obtém as teclas pressionadas
    keys = pygame.key.get_pressed()
# as condicoes extra evitam incrementação quando se esta nas barreiras do mapa
    if player_y != (screen_h - player_walk[0].get_height()) // 2:
        player_y += 5
        boat_y += 5
    elif danca == False:
        # Atualiza a posição do mapa com base nas teclas pressionadas
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            mapa_y += desl_player
            judge_y += desl_player
            npc1_y += desl_player
            npc2_y += desl_player
            npc3_y += desl_player
            boat_y += desl_player
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            mapa_y -= desl_player
            judge_y -= desl_player
            npc1_y -= desl_player
            npc2_y -= desl_player
            npc3_y -= desl_player
            boat_y -= desl_player
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            mapa_x += desl_player
            judge_x += desl_player
            npc1_x += desl_player
            npc2_x += desl_player
            npc3_x += desl_player
            boat_x += desl_player
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            mapa_x -= desl_player
            judge_x -= desl_player
            npc1_x -= desl_player
            npc2_x -= desl_player
            npc3_x -= desl_player
            boat_x -= desl_player
    if danca == False and mapa_x>9:
        mapa_x -= desl_player
        judge_x -= desl_player
        npc1_x -= desl_player
        npc2_x -= desl_player
        npc3_x -= desl_player
        boat_x -= desl_player
    if danca == False and mapa_x < -4029:
        mapa_x += desl_player
        judge_x += desl_player
        npc1_x += desl_player
        npc2_x += desl_player
        npc3_x += desl_player
        boat_x += desl_player
    if danca == False and mapa_y > 2:
        mapa_y -= desl_player
        judge_y -= desl_player
        npc1_y -= desl_player
        npc2_y -= desl_player
        npc3_y -= desl_player
        boat_y -= desl_player
    if danca == False and mapa_y < -4022:
        mapa_y += desl_player
        judge_y += desl_player
        npc1_y += desl_player
        npc2_y += desl_player
        npc3_y += desl_player
        boat_y += desl_player

#________verifica se chegou a zona de danca_________
    if passar_nivel == False:
        if danca==False and mapa_x<=-2975 and mapa_x>=-3250 and mapa_y<=-3640 and mapa_y>=-4015:
            if check_npc1 == True and check_npc2 == True and check_npc3 == True:
                danca = True
                if set_judge == False:
                    judge_x += 250
                    judge_y -= 400
                    set_judge = True

#_______posiciona o player na zona de danca__________
    if danca == True:
        if((mapa_x >= -3735) or (mapa_y <= -3450)):
            if (mapa_x >= -3735):
                mapa_x -= 15
                judge_x -= 15
                npc1_x -= 15
                npc2_x -= 15
                npc3_x -= 15
            if (mapa_y <= -3450):
                mapa_y += 5
                judge_y += 5
                npc1_y += 5
                npc2_y += 5
                npc3_y += 5
        else:
            danca_init = True

    print(mapa_x,mapa_y)

#________________mapa_____________________________
    # Garante que a posição do mapa não ultrapasse os limites da tela
    #mapa_x = min(mapa_margin_w, max(mapa_x, screen_w - mapa_l1.get_width() - mapa_margin_w))
    #mapa_y = min(mapa_margin_h, max(mapa_y, screen_h - mapa_l1.get_height() - mapa_margin_h))


    screen.fill(GREEN_MAP)

    # Desenha o mapa na posição correta
    screen.blit(mapa_l1, (mapa_x, mapa_y))

#__________desenhar judge__________________
    screen.blit(judge_1, (judge_x, judge_y))

# __________desenhar balao judge 1__________________
    #if mapa_x > -474 and mapa_x < -60 and mapa_y > -3000 and mapa_y < -2595:
    if passar_nivel == False and danca == False:
        screen.blit(balao_judge_1, (judge_x - 110, judge_y - 200))

# __________desenhar barco__________________
    screen.blit(boat, (boat_x, boat_y))

# ____________desenhar npc1_________________________
    # Desenha o npc1 na posição correta
    frame_index_npc1 += 0.25
    if frame_index_npc1 >= len(npc1_walk):
        frame_index_npc1 = 0
    screen.blit(npc1_walk[int(frame_index_npc1)], (npc1_x, npc1_y))

# __________desenhar balao npc 1__________________
    if mapa_x > -474 and mapa_x < -60 and mapa_y > -3000 and mapa_y < -2595:
        check_npc1 = True
        screen.blit(balao_npc1, (npc1_x - 140, npc1_y - 300))

# ____________desenhar npc2_________________________
    # Desenha o npc2 na posição correta
    frame_index_npc2 += 0.25
    if frame_index_npc2 >= len(npc3_walk):
        frame_index_npc2 = 0
    screen.blit(npc2_walk[int(frame_index_npc2)], (npc2_x, npc2_y))

# __________desenhar balao npc 2__________________
    if mapa_x > -3730 and mapa_x < -3250 and mapa_y > -405 and mapa_y < 0:
        check_npc2 = True
        screen.blit(balao_npc2, (npc2_x - 140, npc2_y - 300))

# ____________desenhar npc3_________________________
    # Desenha o npc3 na posição correta
    frame_index_npc3 += 0.25
    if frame_index_npc3 >= len(npc3_walk):
        frame_index_npc3 = 0
    screen.blit(npc3_walk[int(frame_index_npc3)], (npc3_x, npc3_y))

# __________desenhar balao npc 3__________________
    if mapa_x > -3925 and mapa_x < -3430 and mapa_y > -2700 and mapa_y < -2145:
        check_npc3 = True
        screen.blit(balao_npc3, (npc3_x - 140, npc3_y - 300))

#____________desenhar jogador_________________________
    # Desenha o jogador na posição correta
    frame_index_player += 0.25
    if frame_index_player >= len(player_walk):
        frame_index_player = 0
    screen.blit(player_walk[int(frame_index_player)], (player_x, player_y))

# ____________desenhar barras pretas de battle_________________________
    if danca == True:
        pygame.draw.rect(screen, BLACK, rect_battle1)
        pygame.draw.rect(screen, BLACK, rect_battle2)

# ___________sequencia de dança__________________

    if danca_init == True:
        # inicio da musica da danca
        if sound_1_play == True:
            sound_1.play()
            sound_1_play = False
        # Ajusta o nível de transparência
        alpha += delta_alpha
        if alpha > 255:
            alpha = 0
            sequence += 1
            if sequence == 4:
                sequence = 0
        ###    alpha = 255
        #    delta_alpha = -delta_alpha  # Inverte a direção
        #elif alpha < 0:
        #    alpha = 0
        #    delta_alpha = -delta_alpha  # Inverte a direção
        # seta up brilha
        if lista_teclas[sequence] == "up":
            seta_up = pygame.Surface((108, 108))
            seta_up.set_alpha(alpha)
            seta_up.fill(WHITE)
            screen.blit(seta_up, (player_x+16, player_y-88))
        # seta down brilha
        if lista_teclas[sequence] == "down":
            seta_down = pygame.Surface((108, 108))
            seta_down.set_alpha(alpha)
            seta_down.fill(WHITE)
            screen.blit(seta_down, (player_x + 16, player_y + 254))
        # seta left brilha
        if lista_teclas[sequence] == "left":
            seta_left = pygame.Surface((108, 108))
            seta_left.set_alpha(alpha)
            seta_left.fill(WHITE)
            screen.blit(seta_left, (player_x - 128, player_y + 83))
        # seta right brilha
        if lista_teclas[sequence] == "right":
            seta_right = pygame.Surface((108, 108))
            seta_right.set_alpha(alpha)
            seta_right.fill(WHITE)
            screen.blit(seta_right, (player_x + 160, player_y + 83))

        # verificacao de clique correto na seta
        if sequence == 0 and (keys[pygame.K_w] or keys[pygame.K_UP]):
            alpha = 0
            sequence += 1
            if sequence == 4:
                sequence = 0
            count_acertos += 1
        if sequence == 1 and (keys[pygame.K_s] or keys[pygame.K_DOWN]):
            alpha = 0
            sequence += 1
            if sequence == 4:
                sequence = 0
            count_acertos += 1
        if sequence == 2 and (keys[pygame.K_a] or keys[pygame.K_LEFT]):
            alpha = 0
            sequence += 1
            if sequence == 4:
                sequence = 0
            count_acertos += 1
        if sequence == 3 and (keys[pygame.K_d] or keys[pygame.K_RIGHT]):
            alpha = 0
            sequence += 1
            if sequence == 4:
                sequence = 0
            count_acertos += 1
        if count_acertos == 12:
            danca = False
            danca_init = False
            passar_nivel = True
            sound_1.stop()

    #_________depois de passar o nivel sai do jogo pelas escadas_______
    if passar_nivel == True:
        if danca == False and mapa_x <= -3910 and mapa_y <= -3750:
            run = False

#____________botao de sair_____________________________
    # Desenha o botão "Sair"
    pygame.draw.rect(screen, RED, button_rect)

    # Adiciona texto ao botão "Sair"
    text_surface = font.render("Sair", True, WHITE)
    text_rect = text_surface.get_rect(center=button_rect.center)
    screen.blit(text_surface, text_rect)

    pygame.display.update()

    clock.tick(30)

pygame.quit()