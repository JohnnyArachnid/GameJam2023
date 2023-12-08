import pygame
import settings
import button
import game
import assets

width = int( settings.config["window_width"] )
height = int( settings.config["window_height"] )

last = 0
count_down = False
is_showing = True
how_to_play = False

# menu screen init
screen = pygame.display.set_mode((width, height))

# buttons
start_game_button = button.Button(400, 100, 200, 50, assets.button_image , "Start game")
resume_game_button = button.Button(400, 100, 200, 50, assets.button_image , "Resume game")
#how_to_play_button = button.Button(400, 200, 200, 50, assets.button_image , "How to play")
plus_sound_volume_button = button.Button(425, 200, 50, 50, assets.plus_button_image , "")
minus_sound_volume_button = button.Button(525, 200, 50, 50, assets.minus_button_image , "")
exit_game_button = button.Button(400, 300, 200, 50, assets.button_image , "Exit game")

# font
sound_volume_text = pygame.font.Font("./assets/Early_GameBoy.ttf", 50)

# menu music
menu_music = pygame.mixer.Sound("./audio/Menu.mp3")
sound_volume = int(settings.config["sound_volume"])
menu_music.set_volume(sound_volume/10)
game.gameObj.piwo_sound.set_volume(sound_volume/10)
game.gameObj.gra_muzyka.set_volume(sound_volume/10)
menu_music.play(-1)

def update_menu_screen(mouse_pos):
    global last
    global is_showing
    global count_down
    global sound_volume

    screen.blit(assets.menu_background, (0,0))
    
    # if game is started show button resume game instead of start game in a menu
    if not game.gameObj.is_started:
        # start game
        if start_game_button.draw(screen, mouse_pos) :
            is_showing = False
            menu_music.stop()
            game.gameObj.is_started = True
            game.gameObj.gra_muzyka.play(-1)
    else:
        # resume game
        if resume_game_button.draw(screen, mouse_pos) :
            game.gameObj.is_started = False
            is_showing = False
            count_down = True
            menu_music.stop()
            game.gameObj.gra_muzyka.play(-1)
            last = pygame.time.get_ticks()

    # if how_to_play button clicked shows graphic presenting how to play
    #if how_to_play_button.draw(screen, mouse_pos) :
        # TODO show image how to play either by moving to another screen or by showing image with button to close it
       # pass
    
    # if plus_button clicked add +1 to sound_volume than save it to config file
    if plus_sound_volume_button.draw(screen, mouse_pos) :
        if sound_volume < 10 :
            sound_volume += 1
            menu_music.set_volume(sound_volume/10)
            game.gameObj.piwo_sound.set_volume(sound_volume/10)
            game.gameObj.gra_muzyka.set_volume(sound_volume/10)
            settings.config["sound_volume"] = str( sound_volume )
            settings.save_data(settings.config)
    
    # render sound_volume number as text
    screen.blit(sound_volume_text.render(settings.config["sound_volume"], True, (255,255,255)),(478,200))
    
    # if minus button clicked add -1 to sound_volume than save it to config file
    if minus_sound_volume_button.draw(screen, mouse_pos) :
        if sound_volume > 0 :
            print(sound_volume)
            sound_volume -= 1
            menu_music.set_volume(sound_volume/10)
            game.gameObj.piwo_sound.set_volume(sound_volume/10)
            game.gameObj.gra_muzyka.set_volume(sound_volume/10)
            settings.config["sound_volume"] = str( sound_volume )
            settings.save_data(settings.config)
    
    # if exit button clicked break main game loop
    if exit_game_button.draw(screen, mouse_pos) :
        settings.main_loop_running = False
    