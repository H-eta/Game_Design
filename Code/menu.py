import pygame
import os
import sys
import pyautogui
import button
import slider
from func import *
import narrative
import lv1 
import lv2

pygame.init()

#Criar janela de jogo
screen_w, screen_h = pyautogui.size()
screen = pygame.display.set_mode((screen_w, screen_h), pygame.FULLSCREEN)
pygame.display.set_caption("Main Menu")

script_dir = os.path.dirname(__file__)
game_design_dir = os.path.dirname(os.path.dirname(script_dir))
picture = os.path.join(game_design_dir, 'Game_Design', 'Sprites', 'background')
picture_path = os.path.join(picture, f'sound_menu.png')
picture = pygame.image.load(picture_path).convert_alpha()
picture = pygame.transform.scale(picture, (1920, 1080))



TEXT_COL = (255, 255, 255)


#load button images
"""resume_img = os.path.join(game_design_dir, 'Game_Design', 'Code', 'images')
resume_img_path = os.path.join(resume_img, f'button_resume.png')
resume_img = pygame.image.load(resume_img_path).convert_alpha()

options_img = os.path.join(game_design_dir, 'Game_Design', 'Code', 'images')
options_img_path = os.path.join(options_img, f'button_options.png')
options_img = pygame.image.load(options_img_path).convert_alpha()

quit_img = os.path.join(game_design_dir, 'Game_Design', 'Code', 'images')
quit_img_path = os.path.join(quit_img, f'button_quit.png')
quit_img = pygame.image.load(quit_img_path).convert_alpha()

back_img = os.path.join(game_design_dir, 'Game_Design', 'Code', 'images')
back_img_path = os.path.join(back_img, f'button_quit.png')
back_img = pygame.image.load(back_img_path).convert_alpha()"""

resume_img = os.path.join(game_design_dir, 'Game_Design', 'Sprites', 'buttons')
resume_img_path = os.path.join(resume_img, f'button_play_2.png')
resume_img = pygame.image.load(resume_img_path).convert_alpha()

options_img = os.path.join(game_design_dir, 'Game_Design', 'Sprites', 'buttons')
options_img_path = os.path.join(options_img, f'button_sound_2.png')
options_img = pygame.image.load(options_img_path).convert_alpha()

quit_img = os.path.join(game_design_dir, 'Game_Design', 'Sprites', 'buttons')
quit_img_path = os.path.join(quit_img, f'button_exit_2.png')
quit_img = pygame.image.load(quit_img_path).convert_alpha()

back_img = os.path.join(game_design_dir, 'Game_Design', 'Sprites', 'buttons')
back_img_path = os.path.join(back_img, f'button_exit_2.png')
back_img = pygame.image.load(back_img_path).convert_alpha()

#create slider instances
center = (screen.get_size()[0]//2, screen.get_size()[1]//2)

#create button instances
resume_button = button.Button((center[0] - 90 - resume_img.get_width() // 2), 360, resume_img, 1.5)
options_button = button.Button((center[0] - 70 - options_img.get_width() // 2), 585, options_img, 1.5)
quit_button = button.Button((center[0] - 57 - quit_img.get_width() // 2), 760, quit_img, 1.5)
back_button = button.Button((center[0] - 57 - back_img.get_width() // 2), 860, back_img, 1.5)



menu_music_vol = slider.Slider((center[0], center[1] - 165), (550,40), 0.5, 0, 100)
#map_music_vol = slider.Slider((center[0]+ 150, center[1] - 10), (550,40), 0.5, 0, 100)
#dance_music_vol = slider.Slider((center[0]+ 150, center[1] + 140), (550,40), 0.5, 0, 100)
#sound_effect_vol = slider.Slider((center[0]+ 150, center[1] + 290), (550,40), 0.5, 0, 100)
sound_effect_vol = slider.Slider((center[0], center[1] - 15), (550,40), 0.5, 0, 100)

#sliderArr = [menu_music_vol, map_music_vol, dance_music_vol, sound_effect_vol]
sliderArr = [menu_music_vol, sound_effect_vol]

#__________importar animação do player_______________
player_walk_dir = os.path.join(game_design_dir, 'Game_Design', 'Animations', 'animation_chris_walking_front_pov_fixed_2')
player_walk = []

#__________importar animação do bg_______________
bg_menu_dir = os.path.join(game_design_dir, 'Game_Design', 'Animations', 'background_main_animation_new')
bg_menu = []



def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x - img.get_width()//2, y))


clock = pygame.time.Clock()

def init_main_menu():

    background_music_file = os.path.join(game_design_dir, 'Game_Design', 'Music', 'music_menu_2.mp3')
    pygame.mixer.music.load(background_music_file)
    pygame.mixer.music.play(-1,0,1000)  # o valor -1 indica que a música será reproduzida em loop

    lenha_arder_file = os.path.join(game_design_dir, 'Game_Design', 'Music', 'lenha_arder_2.mp3')
    lenha_arder = pygame.mixer.Sound(lenha_arder_file)
    lenha_arder.play(-1, 0, 1000)  # o valor -1 indica que a música será reproduzida em loop

    sound_space_file = os.path.join(game_design_dir, 'Game_Design', 'Sound', 'selection_sound_2.wav')
    sound_space = pygame.mixer.Sound(sound_space_file)

    print(" menu iniciado\n")
    menu_state = "main"

    # Carrega cada quadro da animação de forma isolada
    for i in range(4):
        frame_path = os.path.join(player_walk_dir, f'tile00{i}.png')
        frame = pygame.image.load(frame_path).convert_alpha()
        frame_w = frame.get_width()
        frame_h = frame.get_height()
        frame = pygame.transform.scale(frame, (frame.get_width() * 9, frame.get_height() * 9))
        player_walk.append(frame)
        frame_index_player = 0

    # __________importar titulo de jogo_______________
    titulo = os.path.join(game_design_dir, 'Game_Design', 'Sprites', 'background')
    titulo_path = os.path.join(titulo, f'main_menu_title_2.png')
    titulo = pygame.image.load(titulo_path).convert_alpha()
    titulo = pygame.transform.scale(titulo, (titulo.get_width() * 0.6, titulo.get_height() * 0.6))

        # Carrega cada quadro da animação de forma isolada
    for j in range(9):
        bg_frame_path = os.path.join(bg_menu_dir, f'tile00{j}.png')
        bg_frame = pygame.image.load(bg_frame_path).convert_alpha()
        bg_frame_w = bg_frame.get_width()
        bg_frame_h = bg_frame.get_height()
        bg_frame = pygame.transform.scale(bg_frame, (1920, 1080))
        bg_menu.append(bg_frame)
        frame_index_bg = 0    

    run = True
    while run:

        pygame.mixer.music.set_volume(get_mmv())
        lenha_arder.set_volume(get_sev())
        sound_space.set_volume(get_sev() * 0.10)

        pos = pygame.mouse.get_pos()
        mouse = pygame.mouse.get_pressed()

        screen.fill((52, 78, 91))

        #check menu state
        if menu_state == "main":            
            # Desenha o bg
            frame_index_bg += 0.25
            if frame_index_bg >= len(bg_menu):
                frame_index_bg = 0
            screen.blit(bg_menu[int(frame_index_bg)], (0, 0))

            screen.blit(titulo, ((screen_w - titulo.get_width()) // 2, ((screen_h - titulo.get_height()) // 2) -50))

            #draw_text("SHALL WE DANCE?", getTitleFont(), TEXT_COL, center[0], 200)

            # Desenha o jogador
            #frame_index_player += 0.2
            #if frame_index_player >= len(player_walk):
            #    frame_index_player = 0
            #screen.blit(player_walk[int(frame_index_player)], (screen.get_size()[0] - screen.get_size()[0]//4, center[1] - player_walk[int(frame_index_player)].get_height ()//2))

            #draw pause screen buttons
            if resume_button.draw(screen):
                menu_state = "dance"
                sound_space.play()
            if options_button.draw(screen):
                menu_state = "options"
                sound_space.play()
            if quit_button.draw(screen):
                sound_space.play()
                pygame.quit()

        #check if the options menu is open
        if menu_state == "options":
            screen.blit(picture, (0, 0))

            draw_text("Audio Settings", getTitleFont(), TEXT_COL, center[0], 200)

            # Desenha o jogador 
            #frame_index_player += 0.25
            #if frame_index_player >= len(player_walk):
            #    frame_index_player = 0
            #screen.blit(player_walk[int(frame_index_player)], (screen.get_size()[0] - screen.get_size()[0]//4, center[1] - player_walk[int(frame_index_player)].get_height ()//2))
            
            #draw the different options buttons
            draw_text("Music", getTextFont(), TEXT_COL, center[0] - 550, center[1]- 180)
            #draw_text("Map Music Volume", getTextFont(), TEXT_COL, center[0] - 550, center[1] - 30)
            #draw_text("Dance Music Volume", getTextFont(), TEXT_COL, center[0] - 550, center[1] + 120)
            #draw_text("Sound Effects Volume", getTextFont(), TEXT_COL, center[0] - 550, center[1] + 270)
            draw_text("Sound Effects", getTextFont(), TEXT_COL, center[0] - 550, center[1] - 30)

            draw_text(str(menu_music_vol.get_value())+"%", getTextFont(), TEXT_COL, center[0] + 400, center[1] - 180)
            set_mmv(float(menu_music_vol.get_value())/100)
            #draw_text(str(map_music_vol.get_value())+"%", getTextFont(), TEXT_COL, center[0] + 500, center[1] - 30)
            #set_mmpv(float(map_music_vol.get_value())/100)
            #draw_text(str(dance_music_vol.get_value())+"%", getTextFont(), TEXT_COL, center[0] + 500, center[1] + 120)
            #set_mdv(float(dance_music_vol.get_value())/100)
            #draw_text(str(sound_effect_vol.get_value()) + "%", getTextFont(), TEXT_COL, center[0] + 500, center[1] + 270)
            #set_mdv(float(sound_effect_vol.get_value()) / 100)
            draw_text(str(sound_effect_vol.get_value()) + "%", getTextFont(), TEXT_COL, center[0] + 400, center[1] - 30)
            set_sev(float(sound_effect_vol.get_value()) / 100)

            for slider in sliderArr:
                if slider.container_rect.collidepoint(pos):
                    if mouse[0]:
                        slider.grabbed = True
                if not mouse[0]:
                    slider.grabbed = False
                if slider.button_rect.collidepoint(pos):  
                    slider.hover()
                if slider.grabbed:
                    slider.move_slider(pos)
                    slider.hover()
                else:
                    slider.hovered = False
                slider.render(screen)

            if back_button.draw(screen):
                sound_space.play()
                menu_state = "main"

        
        if menu_state == "dance":
            print("Iniciar\n")
            #run = False
            pygame.mixer.music.fadeout(100)
            lenha_arder.fadeout(100)
            narrative.narrate()

        #event handler
        for event in pygame.event.get():
            #if event.type == pygame.KEYDOWN:
                #if event.key == pygame.K_SPACE:
                    #game_paused = True
            if event.type == pygame.QUIT:
                run = False


        pygame.display.update()

        clock.tick(30)



    