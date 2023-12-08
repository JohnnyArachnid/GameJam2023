#w dobrych zawodach wystapilem, czy bieg ukoncze zobaczym, wiare stracilem na samym poczatku

import pygame
import sprites
import settings

pygame.init()

window_width = int(settings.config["window_width"])
window_height = int(settings.config["window_height"])

#most scuffed sprite reading function ever created
def anime(animation_steps, animation_list, loaded_sheet):
    step_counter = 0
    for nesting in animation_steps:
        temp_sprites = []
        for _ in range(nesting):
            temp_sprites.append(loaded_sheet.get_sprite(step_counter, 24, 24, 0, 0, 5, (0,0,0)))
            step_counter += 1
        animation_list.append(temp_sprites)
        
#player sheet
player_image = pygame.image.load('./sprites/Player.png').convert_alpha()
player_sheet = sprites.sprite_sheet(player_image)
player_animation_list = []
player_animation_steps = [4, 4, 4, 4]
player_cooldown = 75
player_move = True
player_direction = 0

#energy sheet
energy_image = pygame.image.load('./sprites/energy.png').convert_alpha()
energy_sheet = sprites.sprite_sheet(energy_image)
energy_animation_list = []
energy_animation_steps = [5]
energy_cooldown = 50

#student sheet
student_image = pygame.image.load('./sprites/student.png').convert_alpha()
student_sheet = sprites.sprite_sheet(student_image)
student_animation_list = []
student_animation_steps = [3, 3, 3, 3, 3, 3, 3, 3, 3]
student_cooldown = 150

anime(player_animation_steps, player_animation_list, player_sheet)
anime(energy_animation_steps, energy_animation_list, energy_sheet)
anime(student_animation_steps, student_animation_list, student_sheet)

#wonderful debugging tool

#print(player_animation_list)
#print(student_animation_list)
#print(energy_animation_list)

# chciałem zrobić kobiete a zrobiłem odwróconą choinkę
# no patrzcie wyszła *kurcze* choinka

previous_swap = [pygame.time.get_ticks(),pygame.time.get_ticks(),pygame.time.get_ticks()]
frame = [0,0,0]

anime(player_animation_steps, player_animation_list, player_sheet)

def draw_anime(animation_list, cooldown, active, animation_set, screen, placement_width, placement_height, frame_):
    
    global previous_swap, frame

    current_time = pygame.time.get_ticks()
    if active == False:
        frame[frame_] = 0
    if current_time - previous_swap[frame_] >= cooldown and active:
        frame[frame_] += 1
        previous_swap[frame_] = current_time
        if frame[frame_] >= len(animation_list[animation_set]):
            frame[frame_] = 0

    screen.blit(animation_list[animation_set][frame[frame_]], (placement_width, placement_height))