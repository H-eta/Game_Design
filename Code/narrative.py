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
script_dir = os.path.dirname(__file__)
game_design_dir = os.path.dirname(os.path.dirname(script_dir))
narrativa_dir = os.path.join(game_design_dir, 'Game_Design', 'Sprites', 'Narrative')
narrativa = []


background_music_file = os.path.join(game_design_dir, 'Game_Design', 'Music', 'narrative_sound.mp3')
pygame.mixer.music.load(background_music_file)

sound_space_file = os.path.join(game_design_dir, 'Game_Design', 'Sound', 'selection_sound_2.wav')
sound_space = pygame.mixer.Sound(sound_space_file)

TEXT_COL = (0, 0, 0)
center = (screen.get_size()[0]//2, screen.get_size()[1]//2)

def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x - img.get_width()//2, y))
  
def narrate():
    background_music_file = os.path.join(game_design_dir, 'Game_Design', 'Music', 'narrative_sound.mp3')
    pygame.mixer.music.load(background_music_file)
    pygame.mixer.music.play(-1, 1, 1000)  # o valor -1 indica que a música será reproduzida em loop


    screen.fill("black")
    frame_index_narr = 0
    narrativa.clear() ###remover as narrativas anteriores
    # Carrega cada quadro da animação de forma isolada
    for i in range(11):
        narr_frame_path = os.path.join(narrativa_dir, f'{i+1}.png')
        narr_frame = pygame.image.load(narr_frame_path).convert_alpha()
        narr_frame_w =narr_frame.get_width()
        narr__h = narr_frame.get_height()
        narr_ = pygame.transform.scale(narr_frame, (1920, 1080))
        narrativa.append(narr_frame)
        frame_index_narr = 0

    space = "[SPACE]"
    text01 = "This is Christopher. Christopher aspires to be the best hip-hop"
    text02 = "dancer in the world."
    text11 = "However, he remembers quite well what happened on the last"
    text12 = "time he tried to dance... he can even feel it."
    text21 = "To end the misery in his life, Christopher decided to sign a"
    text22 = "contract proposed by the Devil himself."
    text31 = "He didn't even read it. The only thing that mattered was the"
    text32 = "promise of becoming the best hip-hop dancer without having"
    text33 = "to work for it."
    text41 = "As promised, with the help of the Devil, Christopher was a"
    text42 = "huge success on every stage and everyone loved him..."
    text51 = "Until the contract's end date arrived. The Devil told Christopher"
    text52 = "that his soul belongs to him."
    text61 = "Christopher is in shock. How could he get out of this"
    text62 = "situation?"
    text71 = "He notices that the contract is ripped, missing some of the"
    text72 = "contents. Could that be a clue to save himself?"
    text81 = "Christopher's journey into the unknown starts. Will he be able"
    text82 = "to get out of this situation and make things got back to"
    text83 = "normal?"

    pygame.mouse.set_visible(False)
    run = True
    while run:

        pygame.mixer.music.set_volume(get_mmv())
        sound_space.set_volume(get_sev() * 0.02)
        # Desenha o jogador 
        #frame_index_narr += 0.001

        if frame_index_narr >= len(narrativa):
            run = False
            pygame.mixer.fadeout(100)
            sound_space.play()
            lv1.play()

        screen.blit(narrativa[int(frame_index_narr)], (0,0))


        if frame_index_narr == 0:
            # Desenhar o texto com a posição ajustada
            screen.blit(getTextFont().render(text01, True, TEXT_COL), (screen_w / 2 - 580, screen_h / 2 + 290))
            screen.blit(getTextFont().render(text02, True, TEXT_COL), (screen_w / 2 - 580, screen_h / 2 + 350))
            screen.blit(getTextFont().render(space, True, TEXT_COL), (screen_w / 2 + 460, screen_h / 2 + 420))

        if frame_index_narr == 1:
            # Desenhar o texto com a posição ajustada
            screen.blit(getTextFont().render(text11, True, TEXT_COL), (screen_w / 2 - 580, screen_h / 2 + 290))
            screen.blit(getTextFont().render(text12, True, TEXT_COL), (screen_w / 2 - 580, screen_h / 2 + 350))
            screen.blit(getTextFont().render(space, True, TEXT_COL), (screen_w / 2 + 460, screen_h / 2 + 420))

        if frame_index_narr == 2:
            # Desenhar o texto com a posição ajustada
            screen.blit(getTextFont().render(text21, True, TEXT_COL), (screen_w / 2 - 580, screen_h / 2 + 290))
            screen.blit(getTextFont().render(text22, True, TEXT_COL), (screen_w / 2 - 580, screen_h / 2 + 350))
            screen.blit(getTextFont().render(space, True, TEXT_COL), (screen_w / 2 + 460, screen_h / 2 + 420))

        if frame_index_narr == 3:
            # Desenhar o texto com a posição ajustada
            screen.blit(getTextFont().render(text31, True, TEXT_COL), (screen_w / 2 - 580, screen_h / 2 + 290))
            screen.blit(getTextFont().render(text32, True, TEXT_COL), (screen_w / 2 - 580, screen_h / 2 + 350))
            screen.blit(getTextFont().render(text33, True, TEXT_COL), (screen_w / 2 - 580, screen_h / 2 + 410))
            screen.blit(getTextFont().render(space, True, TEXT_COL), (screen_w / 2 + 460, screen_h / 2 + 420))


        if frame_index_narr == 4:
            # Desenhar o texto com a posição ajustada
            screen.blit(getTextFont().render(space, True, TEXT_COL), (screen_w / 2 + 460, screen_h / 2 + 420))

        if frame_index_narr == 5:
            # Desenhar o texto com a posição ajustada
            screen.blit(getTextFont().render(text41, True, TEXT_COL), (screen_w / 2 - 580, screen_h / 2 + 290))
            screen.blit(getTextFont().render(text42, True, TEXT_COL), (screen_w / 2 - 580, screen_h / 2 + 350))
            screen.blit(getTextFont().render(space, True, TEXT_COL), (screen_w / 2 + 460, screen_h / 2 + 420))

        if frame_index_narr == 6:
            # Desenhar o texto com a posição ajustada
            screen.blit(getTextFont().render(text51, True, TEXT_COL), (screen_w / 2 - 580, screen_h / 2 + 290))
            screen.blit(getTextFont().render(text52, True, TEXT_COL), (screen_w / 2 - 580, screen_h / 2 + 350))
            screen.blit(getTextFont().render(space, True, TEXT_COL), (screen_w / 2 + 460, screen_h / 2 + 420))

        if frame_index_narr == 7:
            # Desenhar o texto com a posição ajustada
            screen.blit(getTextFont().render(text61, True, TEXT_COL), (screen_w / 2 - 580, screen_h / 2 + 290))
            screen.blit(getTextFont().render(text62, True, TEXT_COL), (screen_w / 2 - 580, screen_h / 2 + 350))
            screen.blit(getTextFont().render(space, True, TEXT_COL), (screen_w / 2 + 460, screen_h / 2 + 420))

        if frame_index_narr == 8:
            # Desenhar o texto com a posição ajustada
            screen.blit(getTextFont().render(text71, True, TEXT_COL), (screen_w / 2 - 580, screen_h / 2 + 290))
            screen.blit(getTextFont().render(text72, True, TEXT_COL), (screen_w / 2 - 580, screen_h / 2 + 350))
            screen.blit(getTextFont().render(space, True, TEXT_COL), (screen_w / 2 + 460, screen_h / 2 + 420))

        if frame_index_narr == 9:
            # Desenhar o texto com a posição ajustada
            screen.blit(getTextFont().render(text81, True, TEXT_COL), (screen_w / 2 - 580, screen_h / 2 + 290))
            screen.blit(getTextFont().render(text82, True, TEXT_COL), (screen_w / 2 - 580, screen_h / 2 + 350))
            screen.blit(getTextFont().render(text83, True, TEXT_COL), (screen_w / 2 - 580, screen_h / 2 + 410))
            screen.blit(getTextFont().render(space, True, TEXT_COL), (screen_w / 2 + 460, screen_h / 2 + 420))

        if frame_index_narr == 10:
            # Desenhar o texto com a posição ajustada
            screen.blit(getTextFont().render(space, True, TEXT_COL), (screen_w / 2 + 460, screen_h / 2 + 420))

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    sound_space.play()
                    frame_index_narr += 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sound_space.play()
                    run = False
                    pygame.mouse.set_visible(True)
                    menu.init_main_menu()

        pygame.display.update()