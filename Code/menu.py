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

picture = pygame.image.load('Sprites/background/sound_menu.png')
picture = pygame.transform.scale(picture, (1920, 1080))

script_dir = os.path.dirname(__file__)
game_design_dir = os.path.dirname(os.path.dirname(script_dir))

TEXT_COL = (255, 255, 255)

#Music
pygame.mixer.music.load("Music/7_teste.mp3")
pygame.mixer.music.play(loops=-1)


#load button images
resume_img = pygame.image.load("Code/images/button_resume.png").convert_alpha()
options_img = pygame.image.load("Code/images/button_options.png").convert_alpha()
quit_img = pygame.image.load("Code/images/button_quit.png").convert_alpha()
back_img = pygame.image.load('Code/images/button_back.png').convert_alpha()

#create button instances
resume_button = button.Button(screen.get_size()[0]//3, 400, resume_img, 1)
options_button = button.Button(screen.get_size()[0]//3, 550, options_img, 1)
quit_button = button.Button(screen.get_size()[0]//3, 700, quit_img, 1)
back_button = button.Button(screen.get_size()[0]//3, 850, back_img, 1)

#create slider instances
center = (screen.get_size()[0]//2, screen.get_size()[1]//2)

menu_music_vol = slider.Slider((center[0], center[1]- 50), (550,40), 0.5, 0, 100)
map_music_vol = slider.Slider((center[0], center[1] + 100), (550,40), 0.5, 0, 100)
dance_music_vol = slider.Slider((center[0], center[1]+250), (550,40), 0.5, 0, 100)

sliderArr = [menu_music_vol, map_music_vol, dance_music_vol]

#__________importar animação do player_______________
player_walk_dir = os.path.join(game_design_dir, 'Game_Design', 'Animations', 'animation_chris_walking_front_pov_fixed_2')
player_walk = []

#__________importar animação do bg_______________
bg_menu_dir = os.path.join(game_design_dir, 'Game_Design', 'Animations', 'background_main_animation')
bg_menu = []


def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x - img.get_width()//2, y))
  



def init_main_menu():


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

        pos = pygame.mouse.get_pos()
        mouse = pygame.mouse.get_pressed()



        screen.fill((52, 78, 91))


        #check menu state
        if menu_state == "main":            
            # Desenha o bg 
            frame_index_bg += 0.025
            if frame_index_bg >= len(bg_menu):
                frame_index_bg = 0
            screen.blit(bg_menu[int(frame_index_bg)], (0, 0))
           
            

            draw_text("SHALL WE DANCE?", getTitleFont(), TEXT_COL, center[0], 200)

            # Desenha o jogador 
            frame_index_player += 0.025
            if frame_index_player >= len(player_walk):
                frame_index_player = 0
            screen.blit(player_walk[int(frame_index_player)], (screen.get_size()[0] - screen.get_size()[0]//4, center[1] - player_walk[int(frame_index_player)].get_height ()//2))

            #draw pause screen buttons
            if resume_button.draw(screen):
                menu_state = "dance"
            if options_button.draw(screen):
                menu_state = "options"
            if quit_button.draw(screen):
                pygame.quit()
        #check if the options menu is open
        if menu_state == "options":
            screen.blit(picture, (0, 0))

            draw_text("Audio Settings", getTitleFont(), TEXT_COL, center[0], 200)

            # Desenha o jogador 
            frame_index_player += 0.25
            if frame_index_player >= len(player_walk):
                frame_index_player = 0
            screen.blit(player_walk[int(frame_index_player)], (screen.get_size()[0] - screen.get_size()[0]//4, center[1] - player_walk[int(frame_index_player)].get_height ()//2))
            
            #draw the different options buttons
            draw_text("Menu Music Volume", getTextFont(), TEXT_COL, center[0] - 700, center[1]- 75)
            draw_text("Map Music Volume", getTextFont(), TEXT_COL, center[0] - 700, center[1] + 75)
            draw_text("Dance Music Volume", getTextFont(), TEXT_COL, center[0] - 700, center[1] + 225)

            draw_text(str(menu_music_vol.get_value())+"%", getTextFont(), TEXT_COL, center[0] + 350, center[1] - 75)
            set_mmv(float(menu_music_vol.get_value())/100)
            draw_text(str(map_music_vol.get_value())+"%", getTextFont(), TEXT_COL, center[0] + 350, center[1] + 75)
            set_mmpv(float(map_music_vol.get_value())/100)
            draw_text(str(dance_music_vol.get_value())+"%", getTextFont(), TEXT_COL, center[0] + 350, center[1] + 225)
            set_mdv(float(dance_music_vol.get_value())/100)

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
                menu_state = "main"

        
        if menu_state == "dance":
            print("Iniciar\n")
            run = False
            pygame.mixer.music.stop()
            narrative.narrate()
            lv1.play()

        #event handler
        for event in pygame.event.get():
            #if event.type == pygame.KEYDOWN:
                #if event.key == pygame.K_SPACE:
                    #game_paused = True
            if event.type == pygame.QUIT:
                run = False


        pygame.display.update()



    