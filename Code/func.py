import pygame
import os

pygame.init()

script_dir = os.path.dirname(__file__)
game_design_dir = os.path.dirname(os.path.dirname(script_dir))
title_font = pygame.font.Font(os.path.join(game_design_dir, 'Game_Design/Font/titles/Alkhemikal.ttf'), 80)
text_font = pygame.font.Font(os.path.join(game_design_dir, 'Game_Design/Font/text/pixelplay.ttf'), 50)

def getTitleFont():
    return title_font

def getTextFont():
    return text_font    

#nivel atual
curr_lvl = "lv2"

def set_curr_lvl(i):
    global curr_lvl
    curr_lvl = i

def get_curr_lvl():
    return curr_lvl

#estado de jogo
game_paused = True

def game_paused_t():
    global game_paused
    game_paused = True

def game_paused_f():
    global game_paused
    game_paused = False   

def get_pause_state():
    return game_paused

#define volume
menu_music_vol = 0.5
map_music_vol = 0.5
dance_music_vol = 0.5

def set_mmv(f):
    global menu_music_vol
    menu_music_vol = f
def set_mmpv(f):
    global map_music_vol
    map_music_vol = f
def set_mdv(f):
    global dance_music_vol
    dance_music_vol = f
    
def get_mmv():
    return menu_music_vol
def get_mmpv():
    return map_music_vol
def get_mdv():
    return dance_music_vol






