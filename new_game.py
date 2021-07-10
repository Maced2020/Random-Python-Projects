import pygame
import random
import math
# started jan/30/2021
# developed by maced2020

# global variables
BACKGROUND_COLOR = (135,206,235) # light Blue
WINDOW = 1000,1000 #(game window size)
GAME_WINDOW = pygame.display.set_mode(WINDOW)


pygame.init()


pygame.display.flip()




def quit_game():
    run_game = True
    while run_game:
        for event in pygame.event.get():
            if event.type == pygame.quit:
                run_game = False
                pygame.quit
quit_game()