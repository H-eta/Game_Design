import pygame
import os
from menu import *
from func import *

pygame.init()



#Game variables
curr_lvl = get_curr_lvl()
print(curr_lvl)


run = True
while run:

    #check if game is paused
    if get_pause_state()== True:
        print("\niniciar menu\n")
        init_main_menu()     

    pygame.display.update()

pygame.quit()   

