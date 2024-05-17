import pygame
import os
import pyautogui
import menu
from menu import *
import lv3

pygame.init()

screen_w, screen_h = pyautogui.size()
screen = pygame.display.set_mode((screen_w, screen_h), pygame.FULLSCREEN)
pygame.display.set_caption("Lv2")

def play():
    set_curr_lvl(2)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    BLACK = (0, 0, 0)
    GREEN_MAP = (66, 82, 34)
    BROWN_MAP = (46, 27, 21)
    button_alpha = 150  # Valor de alfa (0-255)

    button_rect = pygame.Rect(screen_w - 70, 0, 70, 60)
    button_rect2 = pygame.Rect(0, 50, 270, 80)
    button_rect3 = pygame.Rect(0, 50, 300, 80)
    rect_battle1 = pygame.Rect(0, 0, screen_w, 160)
    rect_battle2 = pygame.Rect(0, screen_h - 160, screen_w, 160)
    font = pygame.font.Font(None, 36)

    script_dir = os.path.dirname(__file__)
    game_design_dir = os.path.dirname(os.path.dirname(script_dir))

    text_font = pygame.font.Font('pixelplay.ttf', 40)
    text2_font = pygame.font.Font('pixelplay.ttf', 60)

    # __________importar mapa de jogo nivel 2_____________
    mapa_l2 = os.path.join(game_design_dir, 'Game_Design', 'Sprites', 'maps')
    mapa_l2_path = os.path.join(mapa_l2, f'map_circle_II_lust_not_finished_v3.png')
    mapa_l2_original = pygame.image.load(mapa_l2_path).convert_alpha()

    # __________importar animação do player_______________
    player_walk_dir = os.path.join(game_design_dir, 'Game_Design', 'Animations',
                                   'animation_chris_walking_front_pov_fixed_2')
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

    # __________importar animação do player rotate_______________
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

    # __________importar animação do player a acertar a tecla_______________
    player_dance_dir = os.path.join(game_design_dir, 'Game_Design', 'Animations', 'floating_stars_animation')
    player_dance_good = []
    # Carrega cada quadro da animação de forma isolada
    for i in range(4):
        frame_path = os.path.join(player_dance_dir, f'tile00{i}.png')
        frame = pygame.image.load(frame_path).convert_alpha()
        frame_w = frame.get_width()
        frame_h = frame.get_height()
        frame = pygame.transform.scale(frame, (frame.get_width() * 5, frame.get_height() * 5))
        player_dance_good.append(frame)

    # __________importar animação do player a errar a tecla_______________
    player_dance_dir = os.path.join(game_design_dir, 'Game_Design', 'Animations', 'floating_cloud_animation')
    player_dance_bad = []
    # Carrega cada quadro da animação de forma isolada
    for i in range(4):
        frame_path = os.path.join(player_dance_dir, f'tile00{i}.png')
        frame = pygame.image.load(frame_path).convert_alpha()
        frame_w = frame.get_width()
        frame_h = frame.get_height()
        frame = pygame.transform.scale(frame, (frame.get_width() * 5, frame.get_height() * 5))
        player_dance_bad.append(frame)

    frame_index_player_dance_good = 0
    frame_index_player_dance_bad = 0

    # __________importar animação do NPC1_______________
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

    # _______importacao balao npc1_________
    balao_npc1 = os.path.join(game_design_dir, 'Game_Design', 'Sprites', 'lust_lines')
    balao_npc1_path = os.path.join(balao_npc1, f'lust_npc_line_1.png')
    balao_npc1 = pygame.image.load(balao_npc1_path).convert_alpha()
    balao_npc1 = pygame.transform.scale(balao_npc1, (balao_npc1.get_width() * 0.4, balao_npc1.get_height() * 0.4))

    # __________importar animação do vortice_______________
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

    # __________importar intro do mapa_______________
    intro_map = os.path.join(game_design_dir, 'Game_Design', 'Sprites', 'map_intro')
    intro_map_path = os.path.join(intro_map, f'lust_intro.png')
    intro_map = pygame.image.load(intro_map_path).convert_alpha()
    intro_map = pygame.transform.scale(intro_map, (intro_map.get_width() * 0.8, intro_map.get_height() * 0.8))
    alpha_intro_map = 0  # Nível de transparência inicial

    # __________importar intro de fail_______________
    intro_fail = os.path.join(game_design_dir, 'Game_Design', 'Sprites', 'map_intro')
    intro_fail_path = os.path.join(intro_fail, f'intro_fail.png')
    intro_fail = pygame.image.load(intro_fail_path).convert_alpha()
    intro_fail = pygame.transform.scale(intro_fail, (intro_fail.get_width() * 0.8, intro_fail.get_height() * 0.8))
    alpha_intro_fail = 0  # Nível de transparência inicial

    # __________importar animação do player a dançar up_______________
    player_dance_dir = os.path.join(game_design_dir, 'Game_Design', 'Animations', 'animation_dance_move_up_new')
    player_dance_up = []
    # Carrega cada quadro da animação de forma isolada
    for i in range(4):
        frame_path = os.path.join(player_dance_dir, f'tile00{i}.png')
        frame = pygame.image.load(frame_path).convert_alpha()
        frame_w = frame.get_width()
        frame_h = frame.get_height()
        frame = pygame.transform.scale(frame, (frame.get_width() * 5, frame.get_height() * 5))
        player_dance_up.append(frame)

    # __________importar animação do player a dançar down_______________
    player_dance_dir = os.path.join(game_design_dir, 'Game_Design', 'Animations', 'animation_dance_move_down')
    player_dance_down = []
    # Carrega cada quadro da animação de forma isolada
    for i in range(4):
        frame_path = os.path.join(player_dance_dir, f'tile00{i}.png')
        frame = pygame.image.load(frame_path).convert_alpha()
        frame_w = frame.get_width()
        frame_h = frame.get_height()
        frame = pygame.transform.scale(frame, (frame.get_width() * 5, frame.get_height() * 5))
        player_dance_down.append(frame)

    # __________importar animação do player a dançar left_______________
    player_dance_dir = os.path.join(game_design_dir, 'Game_Design', 'Animations', 'animation_dance_move_left')
    player_dance_left = []
    # Carrega cada quadro da animação de forma isolada
    for i in range(4):
        frame_path = os.path.join(player_dance_dir, f'tile00{i}.png')
        frame = pygame.image.load(frame_path).convert_alpha()
        frame_w = frame.get_width()
        frame_h = frame.get_height()
        frame = pygame.transform.scale(frame, (frame.get_width() * 5, frame.get_height() * 5))
        player_dance_left.append(frame)

    # __________importar animação do player a dançar right_______________
    player_dance_dir = os.path.join(game_design_dir, 'Game_Design', 'Animations', 'animation_dance_move_right')
    player_dance_right = []
    # Carrega cada quadro da animação de forma isolada
    for i in range(4):
        frame_path = os.path.join(player_dance_dir, f'tile00{i}.png')
        frame = pygame.image.load(frame_path).convert_alpha()
        frame_w = frame.get_width()
        frame_h = frame.get_height()
        frame = pygame.transform.scale(frame, (frame.get_width() * 5, frame.get_height() * 5))
        player_dance_right.append(frame)

    frame_index_player_dance = 0

    # ________importar silhuetas__________
    sil_up = os.path.join(game_design_dir, 'Game_Design', 'Sprites', 'silhouette')
    sil_up_path = os.path.join(sil_up, f'up_move_silhouette_new.png')
    sil_up = pygame.image.load(sil_up_path).convert_alpha()
    sil_up = pygame.transform.scale(sil_up, (sil_up.get_width() * 3.5, sil_up.get_height() * 3.5))

    sil_down = os.path.join(game_design_dir, 'Game_Design', 'Sprites', 'silhouette')
    sil_down_path = os.path.join(sil_down, f'down_move_silhouette.png')
    sil_down = pygame.image.load(sil_down_path).convert_alpha()
    sil_down = pygame.transform.scale(sil_down, (sil_down.get_width() * 3.5, sil_down.get_height() * 3.5))

    sil_left = os.path.join(game_design_dir, 'Game_Design', 'Sprites', 'silhouette')
    sil_left_path = os.path.join(sil_left, f'left_move_silhouette.png')
    sil_left = pygame.image.load(sil_left_path).convert_alpha()
    sil_left = pygame.transform.scale(sil_left, (sil_left.get_width() * 3.5, sil_left.get_height() * 3.5))

    sil_right = os.path.join(game_design_dir, 'Game_Design', 'Sprites', 'silhouette')
    sil_right_path = os.path.join(sil_right, f'right_move_silhouette.png')
    sil_right = pygame.image.load(sil_right_path).convert_alpha()
    sil_right = pygame.transform.scale(sil_right, (sil_right.get_width() * 3.5, sil_right.get_height() * 3.5))

    # ________importacao do judge___________
    judge_2 = os.path.join(game_design_dir, 'Game_Design', 'Sprites', 'judges')
    judge_2_path = os.path.join(judge_2, f'minos.png')
    judge_2 = pygame.image.load(judge_2_path).convert_alpha()
    judge_2 = pygame.transform.scale(judge_2, (judge_2.get_width() * 3.3, judge_2.get_height() * 3.3))
    judge_2 = pygame.transform.flip(judge_2, True, False)

    # ________importacao do judge a agitar a cauda___________
    judge_evaluate_dir = os.path.join(game_design_dir, 'Game_Design', 'Animations', 'minos_tail_animation')
    judge_cauda_move = []
    for i in range(4):
        frame_path = os.path.join(judge_evaluate_dir, f'tile00{i}.png')
        frame = pygame.image.load(frame_path).convert_alpha()
        frame_w = frame.get_width()
        frame_h = frame.get_height()
        frame = pygame.transform.scale(frame, (frame.get_width() * 3.3, frame.get_height() * 3.3))
        frame = pygame.transform.flip(frame, True, False)
        judge_cauda_move.append(frame)
    frame_index_judge_cauda_move = 0

    # _______importacao balao judge 1_________
    balao_judge_1 = os.path.join(game_design_dir, 'Game_Design', 'Sprites', 'limbo_lines_new')
    balao_judge_1_path = os.path.join(balao_judge_1, f'limbo_judge_line_1_new.png')
    balao_judge_1 = pygame.image.load(balao_judge_1_path).convert_alpha()
    balao_judge_1 = pygame.transform.scale(balao_judge_1,
                                           (balao_judge_1.get_width() * 0.4, balao_judge_1.get_height() * 0.4))

    # _______importacao balao judge 2_________
    balao_judge_2 = os.path.join(game_design_dir, 'Game_Design', 'Sprites', 'limbo_lines_new')
    balao_judge_2_path = os.path.join(balao_judge_2, f'limbo_judge_line_2_new_space.png')
    balao_judge_2 = pygame.image.load(balao_judge_2_path).convert_alpha()
    balao_judge_2 = pygame.transform.scale(balao_judge_2,
                                           (balao_judge_2.get_width() * 0.4, balao_judge_2.get_height() * 0.4))

    # __________importar tutorial de jogo_______________
    tutorial = os.path.join(game_design_dir, 'Game_Design', 'Sprites', 'background')
    tutorial_path = os.path.join(tutorial, f'controls_panel_complete.png')
    tutorial = pygame.image.load(tutorial_path).convert_alpha()
    tutorial = pygame.transform.scale(tutorial, (tutorial.get_width() * 0.8, tutorial.get_height() * 0.8))

    # Define o fator de zoom
    zoom_factor = 4

    # Redimensiona o mapa original com o fator de zoom
    mapa_l2 = pygame.transform.scale(mapa_l2_original, (
    mapa_l2_original.get_width() * zoom_factor, mapa_l2_original.get_height() * zoom_factor))

    # Define a posição inicial do mapa na tela (centro da tela)
    mapa_x = -570
    mapa_y = -600

    # _________deslocação do player_______________
    desl_player = 15
    player_x = (screen_w - player_walk[0].get_width()) // 2
    # player_y = (screen_h - player_walk[0].get_height()) // 2
    player_y = 250

    # ________posicao incial do npc1________
    npc1_x = 600
    npc1_y = 2250

    # ________posicao incial do vortice________
    vortice_x = 1900
    vortice_y = 0

    # ________posicao incial do intro mapa________
    intro_map_x = 0
    intro_map_y = -80

    # ________posicao incial do judge________
    judge_x = 3290
    judge_y = 2800

    # ________transparencia das silhuetas_________
    alpha = 0  # Nível de transparência inicial
    alpha2 = 255
    delta_alpha = [4, 6, 5, 8, 8, 6, 8, 6, 6, 8,
                    8, 8, 8, 6, 8, 8, 8, 6, 8, 6]  # Incremento/decremento na opacidade
    #delta_alpha = [6] * 20

    # _______sequencia de danca_________
    sequence = 0
    lista_teclas = ["down", "left", "right", "down", "right", "left", "down", "left", "right", "right",
                    "up", "up", "left", "right", "left", "right", "left", "right", "left", "up"]
    # lista_teclas = ["down"]*20
    count_acertos = 0
    count_erro_tecla = 0

    # _________import da musica da danca_______
    # Caminho para o diretório do script atual
    sound_1_file = os.path.join(game_design_dir, 'Game_Design', 'Music', 'music_level_2_2.mp3')
    sound_1 = pygame.mixer.Sound(sound_1_file)
    sound_1_play = True

    # Carregar e reproduzir a música de fundo
    background_music_file = os.path.join(game_design_dir, 'Game_Design', 'Music', 'lust_background_music.mp3')
    pygame.mixer.music.load(background_music_file)
    pygame.mixer.music.set_volume(get_mmpv()*0.2)
    pygame.mixer.music.play(-1,0,2000)  # o valor -1 indica que a música será reproduzida em loop

    # _________import do som do vortice_______
    # Caminho para o diretório do script atual
    sound_vortice_file = os.path.join(game_design_dir, 'Game_Design', 'Sound', 'souls_moaning_pain.mp3')
    sound_vortice = pygame.mixer.Sound(sound_vortice_file)
    sound_vortice_play = True

    # _________import do som de sussurro de npc______
    # Caminho para o diretório do script atual
    sound_sussurro_file = os.path.join(game_design_dir, 'Game_Design', 'Sound', 'sussurros_npc_efeito.mp3')
    sound_sussurro = pygame.mixer.Sound(sound_sussurro_file)
    sound_sussurro_play = True

    # _________import do som de acertar a tecla______
    # Caminho para o diretório do script atual
    sound_achievement_file = os.path.join(game_design_dir, 'Game_Design', 'Sound', 'achievement_sound_1.mp3')
    sound_achievement = pygame.mixer.Sound(sound_achievement_file)
    # sound_achievement_play = True


    # _________import do som de errar a tecla______
    # Caminho para o diretório do script atual
    sound_loser_file = os.path.join(game_design_dir, 'Game_Design', 'Sound', 'loser_sound_1.mp3')
    sound_loser = pygame.mixer.Sound(sound_loser_file)
    # sound_loser_play = True

    sound_space_file = os.path.join(game_design_dir, 'Game_Design', 'Sound', 'selection_sound_2.wav')
    sound_space = pygame.mixer.Sound(sound_space_file)

    clock = pygame.time.Clock()
    set_judge = False
    danca = False
    danca_init = False
    comeca_a_danca = False
    passar_nivel = False
    check_npc1 = False
    intro = False
    intro_fail_bool = False
    mostratutorial = False
    acertou_tecla_up = False
    acertou_tecla_left = False
    acertou_tecla_right = False
    acertou_tecla_down = False
    errou_na_tecla = False
    jogou_uma_vez = False
    run = True
    while run:
        pygame.mouse.set_visible(False)
        if pygame.mouse.get_rel() != (0, 0):
            pygame.mouse.set_visible(True)

        #colocar o volume de musica do mapa
        sound_1.set_volume(get_mmpv()*0.4)
        sound_achievement.set_volume(get_sev() * 0.15)
        sound_loser.set_volume(get_sev() * 0.15)
        sound_vortice.set_volume(get_sev() * 0.2)
        sound_sussurro.set_volume(get_sev() * 0.1)
        sound_space.set_volume(get_sev() * 0.10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Verifica se o clique do mouse foi dentro do botão "Sair"
                if button_rect.collidepoint(event.pos):
                    sound_space.play()
                    run = False
                    pygame.mixer.fadeout(500)
                    pygame.mouse.set_visible(True)
                    menu.init_main_menu()
            elif event.type == pygame.KEYDOWN:
                # Verifica se a tecla pressionada foi a tecla "Esc"
                if event.key == pygame.K_ESCAPE:
                    if danca == True:
                        sound_space.play()
                        sound_1.fadeout(1000)
                        pygame.mixer.music.play(1, 0, 1000)
                        sound_loser.fadeout(1000)
                        sound_achievement.fadeout(1000)
                        danca = False
                        danca_init = False
                        comeca_a_danca = False
                        sound_1_play = True
                        sequence = 0
                        count_acertos = 0
                        count_erro_tecla = 0
                        acertou_tecla = False
                        alpha = 0
                        alpha2 = 255
                        errou_na_tecla = False
                        jogou_uma_vez = False
                        if set_judge == True:
                            if not passar_nivel:
                                judge_x -= 470
                                judge_y += 350
                                set_judge = False
                elif event.key == pygame.K_i:
                    if danca == False:
                        sound_space.play()
                        if mostratutorial == True:
                            mostratutorial = False
                        else:
                            mostratutorial = True

        # _________________deslocaao do player_______________
        # Obtém as teclas pressionadas
        keys = pygame.key.get_pressed()
        if player_y != (screen_h - player_walk[0].get_height()) // 2:
            player_y += 5
            mostratutorial = False
        elif danca == False:
            if keys[pygame.K_w] or keys[pygame.K_UP]:
                if not (mapa_x > -1260 and mapa_y > -600):
                    mapa_y += desl_player
                    npc1_y += desl_player
                    vortice_y += desl_player
                    intro_map_y += desl_player
                    judge_y += desl_player
            if keys[pygame.K_s] or keys[pygame.K_DOWN]:
                mapa_y -= desl_player
                npc1_y -= desl_player
                vortice_y -= desl_player
                intro_map_y -= desl_player
                judge_y -= desl_player
            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                if not (mapa_x > -1275 and mapa_y > -580):
                    mapa_x += desl_player
                    npc1_x += desl_player
                    vortice_x += desl_player
                    intro_map_x += desl_player
                    judge_x += desl_player
            if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                mapa_x -= desl_player
                npc1_x -= desl_player
                vortice_x -= desl_player
                intro_map_x -= desl_player
                judge_x -= desl_player
            if danca == False and mapa_x > -100:
                mapa_x -= desl_player
                npc1_x -= desl_player
                vortice_x -= desl_player
                intro_map_x -= desl_player
                judge_x -= desl_player
            if danca == False and mapa_x < -3730:
                mapa_x += desl_player
                npc1_x += desl_player
                vortice_x += desl_player
                intro_map_x += desl_player
                judge_x += desl_player
            if danca == False and mapa_y > 2:
                mapa_y -= desl_player
                npc1_y -= desl_player
                vortice_y -= desl_player
                intro_map_y -= desl_player
                judge_y -= desl_player
            if danca == False and mapa_y < -3400:
                mapa_y += desl_player
                npc1_y += desl_player
                vortice_y += desl_player
                intro_map_y += desl_player
                judge_y += desl_player

        # ________verifica se chegou a zona de danca_________
        if passar_nivel == False:
            if danca == False and mapa_x <= -2825 and mapa_x >= -3125 and mapa_y <= -2805 and mapa_y >= -3150:
                if check_npc1 == True:
                    danca = True
                    pygame.mixer.music.fadeout(1000)
                    #pygame.mixer.music.pause()
                    if set_judge == False:
                        judge_x += 470
                        judge_y -= 350
                        set_judge = True

        # _______posiciona o player na zona de danca__________
        if danca == True:
            if ((mapa_x >= -3020) or (mapa_y <= -2650)):
                if (mapa_x >= -3020):
                    mapa_x -= 10
                    judge_x -= 10
                    npc1_x -= 10
                    vortice_x -= 10
                if (mapa_x < -3021):
                    mapa_x += 10
                    judge_x += 10
                    npc1_x += 10
                    vortice_x += 10
                if (mapa_y <= -2650):
                    mapa_y += 10
                    judge_y += 10
                    npc1_y += 10
                    vortice_y += 10
                if (mapa_y <= -2650 and mapa_x < -3021 or mapa_x >= -3020):
                    danca_init = True

        #print(mapa_x, mapa_y)

        screen.fill(BROWN_MAP)

        # Desenha o mapa na posição correta
        screen.blit(mapa_l2, (mapa_x, mapa_y))

        # ____________desenhar npc1_________________________
        # Desenha o npc1 na posição correta
        frame_index_npc1 += 0.25
        if frame_index_npc1 >= len(npc1_walk):
            frame_index_npc1 = 0
        screen.blit(npc1_walk[int(frame_index_npc1)], (npc1_x, npc1_y))

        # __________desenhar balao npc 1__________________
        if mapa_x > -620 and mapa_x < -100 and mapa_y > -2715 and mapa_y < -2100:
            check_npc1 = True
            if sound_sussurro_play == True:
                sound_sussurro.play(0,0,100)
                sound_sussurro_play = False
            screen.blit(balao_npc1, (npc1_x - 140, npc1_y - 300))
        else:
            sound_sussurro.fadeout(100)
            sound_sussurro_play = True

        # ____________desenhar vortice_________________________
        frame_index_vortice += 0.25
        if frame_index_vortice >= len(vortice):
            frame_index_vortice = 0
        screen.blit(vortice[int(frame_index_vortice)], (vortice_x, vortice_y))

        # __________desenhar judge__________________
        if comeca_a_danca == False:
            screen.blit(judge_2, (judge_x, judge_y))

        # __________desenhar balao judge 1__________________
        # if mapa_x > -474 and mapa_x < -60 and mapa_y > -3000 and mapa_y < -2595:
        if passar_nivel == False and danca == False:
            screen.blit(balao_judge_1, (judge_x - 110, judge_y - 140))

        # ____________desenhar jogador_________________________
        if mapa_x < -1980 and mapa_x > -3360 and mapa_y < -400 and mapa_y > -1440:
            frame_index_player_rotate += 0.2
            if frame_index_player_rotate >= len(player_rotate):
                frame_index_player_rotate = 0
            if comeca_a_danca == False:
                screen.blit(player_rotate[int(frame_index_player_rotate)], (player_x, player_y))
            if sound_vortice_play == False:
                sound_vortice.play(0,0,1000)
                sound_vortice_play = True
        else:
            frame_index_player += 0.25
            if frame_index_player >= len(player_walk):
                frame_index_player = 0
            if comeca_a_danca == False:
                screen.blit(player_walk[int(frame_index_player)], (player_x, player_y))
            if sound_vortice_play == True:
                sound_vortice.fadeout(1000)
                sound_vortice_play = False

        # ________apresentar intro do mapa__________
        if player_y == (screen_h - player_walk[0].get_height()) // 2:
            intro_map.set_alpha(alpha_intro_map)
            if intro == False:
                alpha_intro_map += 5
            if alpha_intro_map > 255 or intro == True:
                if alpha_intro_map > 0:
                    alpha_intro_map -= 5
                intro = True
            screen.blit(intro_map, (intro_map_x, intro_map_y))

        # ________confirmação de inicio__________
        if danca_init == True:
            if keys[pygame.K_SPACE]:
                if comeca_a_danca == False:
                    sound_space.play()
                comeca_a_danca = True
                #pygame.mixer.music.pause()
            # imprimir pergunta do judge para começar a dançar
            if comeca_a_danca == False:
                screen.blit(balao_judge_2, (judge_x - 110, judge_y - 140))

        # ____________desenhar barras pretas de battle_________________________
        if danca == True:
            pygame.draw.rect(screen, BLACK, rect_battle1)
            pygame.draw.rect(screen, BLACK, rect_battle2)

        # _______botao para o tutorial________________
        if player_y == (screen_h - player_walk[0].get_height()) // 2 and danca == False and intro == True and alpha_intro_map==0 and mostratutorial==False:
            # Cria uma superfície temporária com o mesmo tamanho do botão e com canal alfa
            button_surface = pygame.Surface(button_rect2.size, pygame.SRCALPHA)
            # Preenche a superfície temporária com a cor preta e o valor alfa
            button_surface.fill((0, 0, 0, 0))
            # Blita a superfície temporária na tela
            # screen.blit(button_surface, button_rect2.topleft)
            # Desenha o retângulo com cantos arredondados na superfície temporária
            pygame.draw.rect(button_surface, (*BLACK, button_alpha), button_surface.get_rect(), 0, 10, 0, 15, 0, 15)
            # Blita a superfície temporária na tela
            screen.blit(button_surface, button_rect2.topleft)

            text_surface = text_font.render("Tutorial [press i]", True, WHITE)
            text_rect = text_surface.get_rect(center=button_rect2.center)
            screen.blit(text_surface, text_rect)

        # ____________desenhar tutorial do jogo_________________________
        if danca == True:
            mostratutorial = False
        if mostratutorial == True:
            screen.blit(tutorial, ((screen_w - tutorial.get_width()) // 2, (screen_h - tutorial.get_height()) // 2))

        # ___________sequencia de dança__________________

        if comeca_a_danca == True:
            if sound_1_play == True:
                sound_1.play(0,0,7000)
                sound_1_play = False

            # animação judge a agitar a cauda
            screen.blit(judge_cauda_move[int(frame_index_judge_cauda_move)], (judge_x, judge_y))
            frame_index_judge_cauda_move += 0.15
            if frame_index_judge_cauda_move >= len(judge_cauda_move):
                frame_index_judge_cauda_move = 0

            if alpha <= 255:
                # imprime as silhuetas para a sequencia
                if lista_teclas[sequence] == "up":
                    sil_up.set_alpha(alpha)
                    screen.blit(sil_up, (judge_x - 45 - alpha * 1.3, judge_y + 60))

                if lista_teclas[sequence] == "left":
                    sil_left.set_alpha(alpha)
                    screen.blit(sil_left, (judge_x - 45 - alpha * 1.3, judge_y + 60))

                if lista_teclas[sequence] == "right":
                    sil_right.set_alpha(alpha)
                    screen.blit(sil_right, (judge_x - 45 - alpha * 1.3, judge_y + 60))

                if lista_teclas[sequence] == "down":
                    sil_down.set_alpha(alpha)
                    screen.blit(sil_down, (judge_x - 45 - alpha * 1.3, judge_y + 60))

                alpha += delta_alpha[sequence]

            # verifica se a tecla pressionada é a correta
            if lista_teclas[sequence] == "up" and (keys[pygame.K_w] or keys[pygame.K_UP]) and jogou_uma_vez == False:
                if acertou_tecla_up == False:
                    count_acertos += 1
                    acertou_tecla_up = True
                    frame_index_player_dance_good = 0

            if lista_teclas[sequence] == "left" and (
                    keys[pygame.K_a] or keys[pygame.K_LEFT]) and jogou_uma_vez == False:
                if acertou_tecla_left == False:
                    count_acertos += 1
                    acertou_tecla_left = True
                    frame_index_player_dance_good = 0

            if lista_teclas[sequence] == "right" and (
                    keys[pygame.K_d] or keys[pygame.K_RIGHT]) and jogou_uma_vez == False:
                if acertou_tecla_right == False:
                    count_acertos += 1
                    acertou_tecla_right = True
                    frame_index_player_dance_good = 0

            if lista_teclas[sequence] == "down" and (
                    keys[pygame.K_s] or keys[pygame.K_DOWN]) and jogou_uma_vez == False:
                if acertou_tecla_down == False:
                    count_acertos += 1
                    acertou_tecla_down = True
                    frame_index_player_dance_good = 0

            if alpha > 255:
                # imprime as silhuetas para a sequencia
                if lista_teclas[sequence] == "up":
                    sil_up.set_alpha(alpha2)
                    screen.blit(sil_up, (judge_x - 45 - alpha * 1.3, judge_y + 60))

                if lista_teclas[sequence] == "left":
                    sil_left.set_alpha(alpha2)
                    screen.blit(sil_left, (judge_x - 45 - alpha * 1.3, judge_y + 60))

                if lista_teclas[sequence] == "right":
                    sil_right.set_alpha(alpha2)
                    screen.blit(sil_right, (judge_x - 45 - alpha * 1.3, judge_y + 60))

                if lista_teclas[sequence] == "down":
                    sil_down.set_alpha(alpha2)
                    screen.blit(sil_down, (judge_x - 45 - alpha * 1.3, judge_y + 60))

                alpha2 -= delta_alpha[sequence]
                alpha += delta_alpha[sequence]
                if alpha2 <= 0:
                    alpha = 0
                    alpha2 = 255
                    sequence += 1
                    sound_achievement.fadeout(1000)
                    sound_loser.fadeout(1000)
                    jogou_uma_vez = False
                if sequence == 20:
                    if count_acertos >= 15:
                        danca = False
                        danca_init = False
                        passar_nivel = True
                        comeca_a_danca = False
                        sound_1.fadeout(3000)
                        pygame.mixer.music.play(1,0,1000)
                    else:
                        intro_fail_bool = True
                        sound_1.fadeout(1000)
                        pygame.mixer.music.play(1, 0, 1000)
                        sound_loser.fadeout(1000)
                        sound_achievement.fadeout(1000)
                        danca = False
                        danca_init = False
                        comeca_a_danca = False
                        sound_1_play = True
                        sequence = 0
                        count_acertos = 0
                        count_erro_tecla = 0
                        acertou_tecla = False
                        alpha = 0
                        alpha2 = 255
                        errou_na_tecla = False
                        jogou_uma_vez = False
                        if set_judge == True:
                            if not passar_nivel:
                                judge_x -= 470
                                judge_y += 350
                                set_judge = False

            if sequence < 20:
                # se o jogador clicar na tecla errada
                if (lista_teclas[sequence] != "up" and (keys[pygame.K_w] or keys[pygame.K_UP])) or (
                        lista_teclas[sequence] != "left" and (keys[pygame.K_a] or keys[pygame.K_LEFT])) or (
                        lista_teclas[sequence] != "right" and (keys[pygame.K_d] or keys[pygame.K_RIGHT]) or (
                        lista_teclas[sequence] != "down" and (keys[pygame.K_s] or keys[pygame.K_DOWN]))):
                    if errou_na_tecla == False and jogou_uma_vez == False:
                        count_erro_tecla += 1
                        errou_na_tecla = True
                print(count_erro_tecla)

                # se a tecla for a correta faz a ação de dança correspodente
                if acertou_tecla_up == True or acertou_tecla_left == True or acertou_tecla_right == True or acertou_tecla_down == True:
                    if acertou_tecla_up == True:
                        # Desenha o jogador a dançar
                        # rect_ocultar_player = pygame.Rect(player_x, player_y, (player_walk[0].get_width() / 2),
                        #                                  player_walk[0].get_height())
                        # pygame.draw.rect(screen, GREEN_MAP, rect_ocultar_player)

                        screen.blit(player_dance_up[int(frame_index_player_dance)], (player_x, player_y))
                        frame_index_player_dance += 0.25
                        if frame_index_player_dance >= len(player_dance_up):
                            acertou_tecla_up = False
                            frame_index_player_dance = 0

                    if acertou_tecla_left == True:
                        # Desenha o jogador a dançar
                        # rect_ocultar_player = pygame.Rect(player_x, player_y, (player_walk[0].get_width() / 2),
                        #                                  player_walk[0].get_height())
                        # pygame.draw.rect(screen, GREEN_MAP, rect_ocultar_player)
                        screen.blit(player_dance_left[int(frame_index_player_dance)], (player_x, player_y))
                        frame_index_player_dance += 0.25
                        if frame_index_player_dance >= len(player_dance_left):
                            acertou_tecla_left = False
                            frame_index_player_dance = 0

                    if acertou_tecla_right == True:
                        # Desenha o jogador a dançar
                        # rect_ocultar_player = pygame.Rect(player_x, player_y, (player_walk[0].get_width() / 2),
                        #                                  player_walk[0].get_height())
                        # pygame.draw.rect(screen, GREEN_MAP, rect_ocultar_player)
                        screen.blit(player_dance_right[int(frame_index_player_dance)], (player_x, player_y))
                        frame_index_player_dance += 0.25
                        if frame_index_player_dance >= len(player_dance_right):
                            acertou_tecla_right = False
                            frame_index_player_dance = 0

                    if acertou_tecla_down == True:
                        # Desenha o jogador a dançar
                        # rect_ocultar_player = pygame.Rect(player_x, player_y, (player_walk[0].get_width() / 2),
                        #                                  player_walk[0].get_height())
                        # pygame.draw.rect(screen, GREEN_MAP, rect_ocultar_player)
                        screen.blit(player_dance_down[int(frame_index_player_dance)], (player_x, player_y + 15))
                        frame_index_player_dance += 0.25
                        if frame_index_player_dance >= len(player_dance_down):
                            acertou_tecla_down = False
                            frame_index_player_dance = 0

                    # imprime os blilhos de acertar na tecla alem da animação da danca
                    if frame_index_player_dance_good < len(player_dance_good):
                        sound_achievement.play()
                        screen.blit(player_dance_good[int(frame_index_player_dance_good)],
                                    (player_x - 20, player_y - 30))
                        frame_index_player_dance_good += 0.25

                # se nao for clicada nenhuma tecla ou for errada imprime o player na animação normal
                else:
                    # rect_ocultar_player = pygame.Rect(player_x, player_y, (player_walk[0].get_width()/2),
                    #                                                      player_walk[0].get_height())
                    # pygame.draw.rect(screen, GREEN_MAP, rect_ocultar_player)
                    screen.blit(player_walk[int(frame_index_player)], (player_x, player_y))
                    # se errou na tecla imprime a nuvem no mc
                    if frame_index_player_dance_bad < len(player_dance_bad) and errou_na_tecla == True:
                        screen.blit(player_dance_bad[int(frame_index_player_dance_bad)], (player_x - 20, player_y - 30))
                        frame_index_player_dance_bad += 0.25
                        sound_loser.play()
                        if frame_index_player_dance_bad >= len(player_dance_bad):
                            errou_na_tecla = False
                            frame_index_player_dance_bad = 0

                if keys[pygame.K_w] or keys[pygame.K_UP] or keys[pygame.K_d] or keys[pygame.K_RIGHT] or keys[
                    pygame.K_a] or keys[pygame.K_LEFT] or keys[pygame.K_s] or keys[pygame.K_DOWN]:
                    jogou_uma_vez = True

            print(count_acertos)

        # _______imprime opcao para fazer restart________
        if danca == True:
            text_surface = text_font.render("Restart [press Esc]", True, WHITE)
            text_rect = text_surface.get_rect(center=button_rect3.center)
            screen.blit(text_surface, text_rect)

        # ________apresentar intro de fail__________
        if intro_fail_bool == True:
            intro_fail.set_alpha(alpha_intro_fail)
            screen.blit(intro_fail,
                        ((screen_w - intro_fail.get_width()) // 2, (screen_h - intro_fail.get_height()) // 2))
            alpha_intro_fail += 5
            if alpha_intro_fail > 555:
                intro_fail_bool = False
        if intro_fail_bool == False:
            if alpha_intro_fail > 0:
                intro_fail.set_alpha(alpha_intro_fail)
                screen.blit(intro_fail,
                            ((screen_w - intro_fail.get_width()) // 2, (screen_h - intro_fail.get_height()) // 2))
                alpha_intro_fail -= 5

        # _________depois de passar o nivel sai do jogo pelas escadas_______
        if passar_nivel == True:
            if danca == False and mapa_x <= -3480 and mapa_y <= -2915 and mapa_x > -3585 and mapa_y > -3120:
                run = False
                pygame.mixer.music.fadeout(1000)
                #pygame.mouse.set_visible(True)
                lv3.play()

        # ____________botao de sair_____________________________
        # Desenha o botão "Sair"
        pygame.draw.rect(screen, RED, button_rect,0,10,0,0,15,0)

        # Adiciona texto ao botão "Sair"
        text_surface = text2_font.render("x", True, WHITE)
        text_rect = text_surface.get_rect(center=button_rect.center)
        text_rect.centery -= 10
        screen.blit(text_surface, text_rect)

        pygame.display.update()

        clock.tick(30)