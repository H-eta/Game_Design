import pygame
import os
import pyautogui
import menu
from func import *
import lv1


pygame.init()

screen_w, screen_h = pyautogui.size()
screen = pygame.display.set_mode((screen_w, screen_h), pygame.FULLSCREEN)
#surface + pygame.surface((1920, 1080), pygame.SRCALPHA)
pygame.display.set_caption("Story Time")

#__________importar narrativa_______________
narrativa_dir = os.path.join(game_design_dir, 'Game_Design', 'Sprites', 'Narrative')
narrativa = []




def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x - img.get_width()//2, y))
  
def narrate():
    screen.fill("black")

    # Carrega cada quadro da animação de forma isolada
    for i in range(11):
        narr_frame_path = os.path.join(narrativa_dir, f'{i+1}.png')
        narr_frame = pygame.image.load(narr_frame_path).convert_alpha()
        narr_frame_w =narr_frame.get_width()
        narr__h = narr_frame.get_height()
        narr_ = pygame.transform.scale(narr_frame, (1920, 1080))
        narrativa.append(narr_frame)
        frame_index_narr = 0

    run = True
    while run:
        # Desenha o jogador 
        frame_index_narr += 0.001

        if frame_index_narr >= len(narrativa):
            run = False
            lv1.play()

        screen.blit(narrativa[int(frame_index_narr)], (0,0))

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    frame_index_narr += 1
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()