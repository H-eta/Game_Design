import pygame, sys
from button import Button
from main import rungame

from sound import *
SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("SHALL WE DANCE")

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        PLAY_TEXT = get_font(30).render("This is the PLAY screen.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Purple")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    pygame.quit()
                    

        pygame.display.update()
    