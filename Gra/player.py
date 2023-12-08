import pygame
import settings
import timer

window_width = int( settings.config["window_width"] )
window_height = int( settings.config["window_height"] )
print(window_width, window_height)

player_width = 62
player_height = 62
player_rect = pygame.Rect(int(window_width/2 - player_width/2),int(window_height/2-player_height/2), player_width, player_height)

speed = int(10*timer.timer.modifier)