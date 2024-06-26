import pygame
import os
import pyautogui
import menu
from menu import *

pygame.init()

screen_w, screen_h = pyautogui.size()
screen = pygame.display.set_mode((screen_w, screen_h), pygame.FULLSCREEN)
pygame.display.set_caption("Lv3")

def play():
    set_curr_lvl(2)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    BLACK = (0, 0, 0)
    GREEN_MAP = (66, 82, 34)
    BROWN_MAP = (46, 27, 21)
    BLUE_MAP = (34, 164, 234)
    button_alpha = 150  # Valor de alfa (0-255)

    button_rect = pygame.Rect(screen_w - 70, 0, 70, 60)
    button_rect2 = pygame.Rect(0, -10, 270, 80)
    button_rect3 = pygame.Rect(0, 0, 300, 80)
    rect_battle1 = pygame.Rect(0, 0, screen_w, 160)
    rect_battle2 = pygame.Rect(0, screen_h - 160, screen_w, 160)
    font = pygame.font.Font(None, 36)

    script_dir = os.path.dirname(__file__)
    game_design_dir = os.path.dirname(os.path.dirname(script_dir))

    text_font = pygame.font.Font('pixelplay.ttf', 40)
    text2_font = pygame.font.Font('pixelplay.ttf', 60)

    # __________importar mapa de jogo nivel 3_____________
    mapa_l3 = os.path.join(game_design_dir, 'Game_Design', 'Sprites', 'maps')
    mapa_l3_path = os.path.join(mapa_l3, f'threachery_map_option_3.png')
    mapa_l3_original = pygame.image.load(mapa_l3_path).convert_alpha()

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

    # __________importar intro do mapa_______________
    intro_map = os.path.join(game_design_dir, 'Game_Design', 'Sprites', 'map_intro')
    intro_map_path = os.path.join(intro_map, f'treachery_intro.png')
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
    judge = os.path.join(game_design_dir, 'Game_Design', 'Sprites', 'judges')
    judge_path = os.path.join(judge, f'judge.png')
    judge = pygame.image.load(judge_path).convert_alpha()
    judge = pygame.transform.scale(judge, (judge.get_width() * 1.3, judge.get_height() * 1.3))

    # ________importacao do judge a agitar a cauda___________
    judge_evaluate_dir = os.path.join(game_design_dir, 'Game_Design', 'Animations', 'judge_tail_animation')
    judge_cauda_move = []
    for i in range(8):
        frame_path = os.path.join(judge_evaluate_dir, f'tile00{i}.png')
        frame = pygame.image.load(frame_path).convert_alpha()
        frame_w = frame.get_width()
        frame_h = frame.get_height()
        frame = pygame.transform.scale(frame, (frame.get_width() * 6.5, frame.get_height() * 6.5))
        judge_cauda_move.append(frame)
    frame_index_judge_cauda_move = 0

    # _______importacao balao judge 1_________
    balao_judge_1 = os.path.join(game_design_dir, 'Game_Design', 'Sprites')
    balao_judge_1_path = os.path.join(balao_judge_1, f'Judge_line.png')
    balao_judge_1 = pygame.image.load(balao_judge_1_path).convert_alpha()
    balao_judge_1 = pygame.transform.scale(balao_judge_1,
                                           (balao_judge_1.get_width() * 0.4,
                                            balao_judge_1.get_height() * 0.4))

    # _______importacao balao judge 4_________
    balao_judge_4 = os.path.join(game_design_dir, 'Game_Design', 'Sprites', 'limbo_lines_new')
    balao_judge_4_path = os.path.join(balao_judge_4, f'limbo_judge_line_3_new_space_1.png')
    balao_judge_4 = pygame.image.load(balao_judge_4_path).convert_alpha()
    balao_judge_4 = pygame.transform.scale(balao_judge_4,
                                           (balao_judge_4.get_width() * 0.4, balao_judge_4.get_height() * 0.4))

    # ________importacao do diabo___________
    diabo = os.path.join(game_design_dir, 'Game_Design', 'Sprites', 'judges')
    diabo_path = os.path.join(diabo, f'devil.png')
    diabo = pygame.image.load(diabo_path).convert_alpha()
    diabo = pygame.transform.scale(diabo, (diabo.get_width() * 5, diabo.get_height() * 5))

    # ________importacao do diabo com bola a girar___________
    diabo_evaluate_dir = os.path.join(game_design_dir, 'Game_Design', 'Animations', 'devil_spinning_ball_animation')
    diabo_bola_move = []
    for i in range(8):
        frame_path = os.path.join(diabo_evaluate_dir, f'tile00{i}.png')
        frame = pygame.image.load(frame_path).convert_alpha()
        frame_w = frame.get_width()
        frame_h = frame.get_height()
        frame = pygame.transform.scale(frame, (frame.get_width() * 5, frame.get_height() * 5))
        diabo_bola_move.append(frame)
    frame_index_diabo_bola_move = 0

    # _______importacao balao diabo start_________
    balao_diabo_start = os.path.join(game_design_dir, 'Game_Design', 'Sprites', 'limbo_lines_new')
    balao_diabo_start_path = os.path.join(balao_diabo_start, f'limbo_judge_line_2_new_space.png')
    balao_diabo_start = pygame.image.load(balao_diabo_start_path).convert_alpha()
    balao_diabo_start = pygame.transform.scale(balao_diabo_start,
                                           (balao_diabo_start.get_width() * 0.4, balao_diabo_start.get_height() * 0.4))

    # _______importacao balao diabo 1_________
    balao_diabo_1 = os.path.join(game_design_dir, 'Game_Design', 'Sprites')
    balao_diabo_1_path = os.path.join(balao_diabo_1, f'Devil_line.png')
    balao_diabo_1 = pygame.image.load(balao_diabo_1_path).convert_alpha()
    balao_diabo_1 = pygame.transform.scale(balao_diabo_1,
                                               (balao_diabo_1.get_width() * 0.4,
                                                balao_diabo_1.get_height() * 0.4))

    # __________importar tutorial de jogo_______________
    tutorial = os.path.join(game_design_dir, 'Game_Design', 'Sprites', 'background')
    tutorial_path = os.path.join(tutorial, f'controls_panel_complete_2.png')
    tutorial = pygame.image.load(tutorial_path).convert_alpha()
    tutorial = pygame.transform.scale(tutorial, (tutorial.get_width() * 0.8, tutorial.get_height() * 0.8))

    #________cutscenes finais___________
    final_cutscene_dir = os.path.join(game_design_dir, 'Game_Design', 'Sprites', 'Narrative')
    final_cutscene = []
    for i in range(4):
        frame_path = os.path.join(final_cutscene_dir, f'{i+1+11}.png')
        frame = pygame.image.load(frame_path).convert_alpha()
        frame_w = frame.get_width()
        frame_h = frame.get_height()
        frame = pygame.transform.scale(frame, (1920, 1080))
        final_cutscene.append(frame)
    frame_index_narr = 0

    # Define o fator de zoom
    zoom_factor = 4

    # Redimensiona o mapa original com o fator de zoom
    mapa_l3 = pygame.transform.scale(mapa_l3_original, (
    mapa_l3_original.get_width() * zoom_factor, mapa_l3_original.get_height() * zoom_factor))

    # Define a posição inicial do mapa na tela (centro da tela)
    mapa_x = -80
    mapa_y = -380

    # _________deslocação do player_______________
    desl_player = 15
    player_x = (screen_w - player_walk[0].get_width()) // 2
    #player_y = (screen_h - player_walk[0].get_height()) // 2
    player_y = 200

    # ________posicao incial do intro mapa________
    intro_map_x = 0
    intro_map_y = -30

    # ________posicao incial do judge________
    judge_x = 2300
    judge_y = 2150

    # ________posicao incial do diabo________
    diabo_x = 1300
    diabo_y = 2100

    # ________transparencia das silhuetas_________
    alpha = 0  # Nível de transparência inicial
    alpha2 = 255
    delta_alpha = [6, 8, 10, 8, 10, 12, 10, 10, 10, 12,
                    10, 10, 12, 10, 10, 8, 10, 10, 12, 10,
                    10, 10, 12, 10, 10, 10, 10, 8, 6, 6]  # Incremento/decremento na opacidade
    #delta_alpha = [10] * 30

    # _______sequencia de danca_________
    sequence = 0
    lista_teclas = ["down", "left", "right", "down", "right", "left", "down", "left", "right", "down",
                    "up", "left", "right", "down", "right", "left", "down", "left", "right", "down",
                    "up", "left", "left", "right", "up", "down", "left", "right", "left", "up"]
    # lista_teclas = ["down"]*20
    count_acertos = 0
    count_erro_tecla = 0

    # _________import da musica da danca_______
    # Caminho para o diretório do script atual
    sound_1_file = os.path.join(game_design_dir, 'Game_Design', 'Music', 'danca_level_3_2.mp3')
    sound_1 = pygame.mixer.Sound(sound_1_file)
    sound_1_play = True

    # Carregar e reproduzir a música de fundo
    background_music_file = os.path.join(game_design_dir, 'Game_Design', 'Music', 'treachery_background_music_2.mp3')
    background_music = pygame.mixer.Sound(background_music_file)
    # pygame.mixer.music.set_volume(get_mmpv() * 0.2)
    background_music.play(-1, 0, 2000)  # o valor -1 indica que a música será reproduzida em loop

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

    #__________textos para cutscene____
    TEXT_COL = (0, 0, 0)
    space = "[SPACE]"
    text01 = "Christopher conquers the challenge, reclaiming his life and"
    text02 = "leaving the Devil fuming."
    text11 = "Christopher's comeback to the living world brought a fresh"
    text12 = "vibe - now, every move he makes is uniquely his own."

    clock = pygame.time.Clock()
    set_judge = False
    danca = False
    danca_init = False
    comeca_a_danca = False
    passar_nivel = False
    intro = False
    intro_fail_bool = False
    mostratutorial = False
    acertou_tecla_up = False
    acertou_tecla_left = False
    acertou_tecla_right = False
    acertou_tecla_down = False
    errou_na_tecla = False
    jogou_uma_vez = False
    conversa_terminada=False
    conversa=1
    run = True
    while run:
        pygame.mouse.set_visible(False)
        if pygame.mouse.get_rel() != (0, 0):
            pygame.mouse.set_visible(True)

        # colocar o volume de musica do mapa
        background_music.set_volume(get_mmv() * 0.4)
        sound_1.set_volume(get_mmv()*0.3)
        sound_achievement.set_volume(get_sev()*0.15)
        sound_loser.set_volume(get_sev()*0.15)
        sound_space.set_volume(get_sev() * 0.10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Verifica se o clique do mouse foi dentro do botão "Sair"
                if button_rect.collidepoint(event.pos) and mostratutorial == False:
                    sound_space.play()
                    run = False
                    background_music.fadeout(100)
                    sound_1.fadeout(100)
                    pygame.mouse.set_visible(True)
                    menu.init_main_menu()
            elif event.type == pygame.KEYDOWN:
                # Verifica se a tecla pressionada foi a tecla "Esc"
                if event.key == pygame.K_ESCAPE:
                    if danca == True:
                        sound_space.play()
                        conversa = 1
                        conversa_terminada = False
                        sound_1.fadeout(1000)
                        background_music.play(1, 0, 1000)
                        sound_loser.fadeout(1000)
                        sound_achievement.fadeout(1000)
                        danca = False
                        danca_init = False
                        comeca_a_danca = False
                        sound_1_play = True
                        sequence = 0
                        count_acertos = 0
                        count_erro_tecla = 0
                        acertou_tecla_up = False
                        acertou_tecla_left = False
                        acertou_tecla_right = False
                        acertou_tecla_down = False
                        frame_index_player_dance_good = 0
                        frame_index_player_dance_bad = 0
                        frame_index_player_dance = 0
                        alpha = 0
                        alpha2 = 255
                        errou_na_tecla = False
                        jogou_uma_vez = False
                        if set_judge == True:
                            if not passar_nivel:
                                #judge_x -= 470
                                #judge_y += 350
                                set_judge = False
                elif event.key == pygame.K_i:
                    if danca == False and passar_nivel == False:
                        sound_space.play()
                        if mostratutorial == True:
                            mostratutorial = False
                        else:
                            mostratutorial = True
                elif event.key == pygame.K_SPACE:
                    if danca_init == True and conversa_terminada == False:
                        sound_space.play()
                        if conversa == 1:
                            conversa=2
                        elif conversa == 2:
                            conversa=3
                        elif conversa == 3:
                            conversa_terminada = True
                    if passar_nivel == True:
                        if frame_index_narr==0:
                            sound_space.play()
                            frame_index_narr = frame_index_narr + 1
                        elif frame_index_narr==1:
                            sound_space.play()
                            frame_index_narr = frame_index_narr + 1
                        elif frame_index_narr==2:
                            sound_space.play()
                            frame_index_narr = frame_index_narr + 1
                        elif frame_index_narr==3:
                            sound_space.play()
                            frame_index_narr = frame_index_narr + 1
                        elif frame_index_narr==4:
                            sound_space.play()
                            run = False
                            background_music.fadeout(1000)
                            pygame.mouse.set_visible(True)
                            menu.init_main_menu()

        # _________________deslocaao do player_______________
        # Obtém as teclas pressionadas
        keys = pygame.key.get_pressed()
        if player_y != (screen_h - player_walk[0].get_height()) // 2:
            player_y += 5
            mostratutorial = False
        elif danca == False and passar_nivel == False:
            if keys[pygame.K_w] or keys[pygame.K_UP]:
                mapa_y += desl_player
                intro_map_y += desl_player
                judge_y += desl_player
                diabo_y += desl_player
            if keys[pygame.K_s] or keys[pygame.K_DOWN]:
                mapa_y -= desl_player
                intro_map_y -= desl_player
                judge_y -= desl_player
                diabo_y -= desl_player
            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                mapa_x += desl_player
                intro_map_x += desl_player
                judge_x += desl_player
                diabo_x += desl_player
            if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                mapa_x -= desl_player
                intro_map_x -= desl_player
                judge_x -= desl_player
                diabo_x -= desl_player
            if danca == False and mapa_x > -50:
                mapa_x -= desl_player
                intro_map_x -= desl_player
                judge_x -= desl_player
                diabo_x -= desl_player
            if danca == False and mapa_x < -1835:
                mapa_x += desl_player
                intro_map_x += desl_player
                judge_x += desl_player
                diabo_x += desl_player
            if danca == False and mapa_y > -380:
                mapa_y -= desl_player
                intro_map_y -= desl_player
                judge_y -= desl_player
                diabo_y -= desl_player
            if danca == False and mapa_y < -1685:
                mapa_y += desl_player
                intro_map_y += desl_player
                judge_y += desl_player
                diabo_y += desl_player

        # ________verifica se chegou a zona de danca_________
        if passar_nivel == False:
            if danca == False and mapa_x <= -980 and mapa_x >= -1020 and mapa_y <= -1670 and mapa_y >= -1755:
                danca = True
                background_music.fadeout(1000)
                if set_judge == False:
                    judge_x += 0
                    judge_y -= 0
                    set_judge = True

        # _______posiciona o player na zona de danca__________
        if danca == True:
            if ((mapa_x >= -1080) or (mapa_y >= -2110)):
                if (mapa_x >= -1080):
                    mapa_x -= 10
                    judge_x -= 10
                    diabo_x -= 10
                if (mapa_x < -1081):
                    mapa_x += 10
                    judge_x += 10
                    diabo_x += 10
                if (mapa_y >= -2110):
                    mapa_y -= 15
                    judge_y -= 15
                    diabo_y -= 15
                if (mapa_y <= -2100):
                    danca_init = True

        #print(mapa_x, mapa_y)

        screen.fill(BLUE_MAP)

        # Desenha o mapa na posição correta
        screen.blit(mapa_l3, (mapa_x, mapa_y))

        # __________desenhar judge__________________
        if comeca_a_danca == False:
            screen.blit(judge, (judge_x, judge_y))

        # __________desenhar judge__________________
        if comeca_a_danca == False:
            screen.blit(diabo, (diabo_x, diabo_y))

        # ____________desenhar jogador_________________________
        frame_index_player += 0.25
        if frame_index_player >= len(player_walk):
            frame_index_player = 0
        if comeca_a_danca == False:
            screen.blit(player_walk[int(frame_index_player)], (player_x, player_y))

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
            if conversa_terminada == True:
                comeca_a_danca = True
                #pygame.mixer.music.pause()
            # imprimir pergunta do judge para começar a dançar
            else:
                if conversa == 1:
                    screen.blit(balao_diabo_1, (diabo_x - 80, diabo_y - 160))
                if conversa == 2:
                    screen.blit(balao_judge_1, (judge_x - 80, judge_y - 140))
                if conversa == 3:
                    screen.blit(balao_diabo_start, (diabo_x - 80, diabo_y - 140))

        # ____________desenhar barras pretas de battle_________________________
        if danca == True:
            pygame.draw.rect(screen, BLACK, rect_battle1)
            pygame.draw.rect(screen, BLACK, rect_battle2)

        # ____________desenhar tutorial do jogo_________________________
        if danca == True:
            mostratutorial = False
        if mostratutorial == True:
            screen.blit(tutorial, ((screen_w - tutorial.get_width()) // 2, (screen_h - tutorial.get_height()) // 2))

        # ____________desenhar tutorial do jogo_________________________
        if danca == True:
            mostratutorial = False
        if mostratutorial == True:
            screen.blit(tutorial, ((screen_w - tutorial.get_width()) // 2, (screen_h - tutorial.get_height()) // 2))

        # _______botao para o tutorial________________
        if player_y == (screen_h - player_walk[0].get_height()) // 2 and danca == False and intro == True and alpha_intro_map == 0:
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

        # ___________sequencia de dança__________________

        if comeca_a_danca == True:
            if sound_1_play == True:
                sound_1.play(0,0,10000)
                sound_1_play = False

            #animação judge a agitar a cauda
            screen.blit(judge_cauda_move[int(frame_index_judge_cauda_move)], (judge_x, judge_y))
            frame_index_judge_cauda_move += 0.20
            if frame_index_judge_cauda_move >= len(judge_cauda_move):
                frame_index_judge_cauda_move = 0

            #animação diabo com bola a girar
            screen.blit(diabo_bola_move[int(frame_index_diabo_bola_move)], (diabo_x, diabo_y))
            frame_index_diabo_bola_move += 0.20
            if frame_index_diabo_bola_move >= len(diabo_bola_move):
                frame_index_diabo_bola_move = 0

            if alpha <= 255:
                # imprime as silhuetas para a sequencia
                # imprime as do diabo
                if (sequence % 2) == 0:
                    if lista_teclas[sequence] == "up":
                        sil_up.set_alpha(alpha)
                        screen.blit(sil_up, (diabo_x + 250 + alpha * 1.3, diabo_y + 110))

                    if lista_teclas[sequence] == "left":
                        sil_left.set_alpha(alpha)
                        screen.blit(sil_left, (diabo_x + 250 + alpha * 1.3, diabo_y + 110))

                    if lista_teclas[sequence] == "right":
                        sil_right.set_alpha(alpha)
                        screen.blit(sil_right, (diabo_x + 250 + alpha * 1.3, diabo_y + 110))

                    if lista_teclas[sequence] == "down":
                        sil_down.set_alpha(alpha)
                        screen.blit(sil_down, (diabo_x + 250 + alpha * 1.3, diabo_y + 110))

                # imprime as do judge
                if (sequence % 2) != 0:
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
                # imprime as do diabo
                if (sequence % 2) == 0:
                    if lista_teclas[sequence] == "up":
                        sil_up.set_alpha(alpha2)
                        screen.blit(sil_up, (diabo_x + 250 + alpha * 1.3, diabo_y + 110))

                    if lista_teclas[sequence] == "left":
                        sil_left.set_alpha(alpha2)
                        screen.blit(sil_left, (diabo_x + 250 + alpha * 1.3, diabo_y + 110))

                    if lista_teclas[sequence] == "right":
                        sil_right.set_alpha(alpha2)
                        screen.blit(sil_right, (diabo_x + 250 + alpha * 1.3, diabo_y + 110))

                    if lista_teclas[sequence] == "down":
                        sil_down.set_alpha(alpha2)
                        screen.blit(sil_down, (diabo_x + 250 + alpha * 1.3, diabo_y + 110))

                #imprime as do judge
                if (sequence % 2) != 0:
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
                if sequence == 30:
                    if count_acertos >= 25:
                        danca = False
                        danca_init = False
                        passar_nivel = True
                        comeca_a_danca = False
                        sound_1.fadeout(2000)
                        background_music.play(1, 0, 1000)
                        sound_loser.fadeout(1000)
                        sound_achievement.fadeout(1000)
                    else:
                        intro_fail_bool = True
                        conversa = 1
                        conversa_terminada = False
                        sound_1.fadeout(1000)
                        background_music.play(1, 0, 1000)
                        sound_loser.fadeout(1000)
                        sound_achievement.fadeout(1000)
                        danca = False
                        danca_init = False
                        comeca_a_danca = False
                        sound_1_play = True
                        sequence = 0
                        count_acertos = 0
                        count_erro_tecla = 0
                        acertou_tecla_up = False
                        acertou_tecla_left = False
                        acertou_tecla_right = False
                        acertou_tecla_down = False
                        frame_index_player_dance_good = 0
                        frame_index_player_dance_bad = 0
                        frame_index_player_dance = 0
                        alpha = 0
                        alpha2 = 255
                        errou_na_tecla = False
                        jogou_uma_vez = False
                        if set_judge == True:
                            if not passar_nivel:
                                # judge_x -= 470
                                # judge_y += 350
                                set_judge = False

            if sequence < 30:
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
                    # imprime os blilhos de acertar na tecla alem da animação da danca
                    if frame_index_player_dance_good < len(player_dance_good):
                        if frame_index_player_dance_good == 0:
                            sound_achievement.play()
                        screen.blit(player_dance_good[int(frame_index_player_dance_good)],
                                    (player_x - 20, player_y - 30))
                        frame_index_player_dance_good += 0.25

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

                # se nao for clicada nenhuma tecla ou for errada imprime o player na animação normal
                else:
                    # rect_ocultar_player = pygame.Rect(player_x, player_y, (player_walk[0].get_width()/2),
                    #                                                      player_walk[0].get_height())
                    # pygame.draw.rect(screen, GREEN_MAP, rect_ocultar_player)
                    screen.blit(player_walk[int(frame_index_player)], (player_x, player_y))
                    # se errou na tecla imprime a nuvem no mc
                    if frame_index_player_dance_bad < len(player_dance_bad) and errou_na_tecla == True:
                        if frame_index_player_dance_bad == 0:
                            sound_loser.play()
                        screen.blit(player_dance_bad[int(frame_index_player_dance_bad)], (player_x - 20, player_y - 30))
                        frame_index_player_dance_bad += 0.25
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
            screen.blit(intro_fail, ((screen_w - intro_fail.get_width()) // 2, (screen_h - intro_fail.get_height()) // 2))
            alpha_intro_fail += 5
            if alpha_intro_fail > 225:
                intro_fail_bool = False
        if intro_fail_bool == False:
            if alpha_intro_fail > 0:
                intro_fail.set_alpha(alpha_intro_fail)
                screen.blit(intro_fail, ((screen_w - intro_fail.get_width()) // 2, (screen_h - intro_fail.get_height()) // 2))
                alpha_intro_fail -= 5

        # _________depois de passar o nivel sai do jogo pelas escadas_______
        if passar_nivel == True:
            if frame_index_narr == 0:
                screen.blit(balao_judge_4, (diabo_x - 80, diabo_y - 140))
            if frame_index_narr == 1:
                screen.blit(final_cutscene[int(frame_index_narr-1)], (0, 0))
                screen.blit(getTextFont().render(text01, True, TEXT_COL), (screen_w / 2 - 580, screen_h / 2 + 290))
                screen.blit(getTextFont().render(text02, True, TEXT_COL), (screen_w / 2 - 580, screen_h / 2 + 350))
                screen.blit(getTextFont().render(space, True, TEXT_COL), (screen_w / 2 + 460, screen_h / 2 + 420))
            if frame_index_narr == 2:
                screen.blit(final_cutscene[int(frame_index_narr-1)], (0, 0))
                screen.blit(getTextFont().render(text11, True, TEXT_COL), (screen_w / 2 - 580, screen_h / 2 + 290))
                screen.blit(getTextFont().render(text12, True, TEXT_COL), (screen_w / 2 - 580, screen_h / 2 + 350))
                screen.blit(getTextFont().render(space, True, TEXT_COL), (screen_w / 2 + 460, screen_h / 2 + 420))
            if frame_index_narr == 3:
                screen.blit(final_cutscene[int(frame_index_narr-1)], (0, 0))
            if frame_index_narr == 4:
                screen.blit(final_cutscene[int(frame_index_narr-1)], (0, 0))


        # ____________botao de sair_____________________________
        # Desenha o botão "Sair"
        if mostratutorial == False:
            pygame.draw.rect(screen, RED, button_rect,0,10,0,0,15,0)

            # Adiciona texto ao botão "Sair"
            text_surface = text2_font.render("x", True, WHITE)
            text_rect = text_surface.get_rect(center=button_rect.center)
            text_rect.centery -= 10
            screen.blit(text_surface, text_rect)

        pygame.display.update()

        clock.tick(30)