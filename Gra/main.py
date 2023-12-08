import os
# wyświetl okno w pozycji danej poniżej
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (20,30)

import pygame

# pygame modules init
pygame.init()

# importing files after pygame modules are initialized
import settings
import game
import menu
import timer

# display settings
pygame.display.set_caption("MS Thursday Pov UJ Edition")

# clock
clock = pygame.time.Clock()
max_fps = int( settings.config["max_fps"] )

count_down_text = pygame.font.Font("./assets/Early_GameBoy.ttf", 200)

# game loop
while settings.main_loop_running:
    
    # limit max fps to fixed number
    dt = clock.tick(max_fps)
    # for any movement to be independent of max_fps has to be multiplied by dt
    # e.g. player.position.x += player.xSpeed * dt
    
    # check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            settings.main_loop_running = False

        # check for keyboard input
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: # if escape is pressed then toggle menu
                if menu.is_showing == False:
                    game.gameObj.is_started = True
                    menu.count_down = False
                    menu.is_showing = True
                    game.gameObj.gra_muzyka.stop()
                    menu.menu_music.play(-1)
                else:
                    menu.menu_music.stop()
                    menu.is_showing = False
                    game.gameObj.is_started = False
                    menu.count_down = True
                    game.gameObj.gra_muzyka.play(-1)
                    menu.last = pygame.time.get_ticks()


    # mouse position on screen
    mouse_pos = pygame.mouse.get_pos()

    if not menu.is_showing and game.gameObj.is_started:
        game.gameObj.update_game_screen(mouse_pos)
    else:
        if game.gameObj.is_started == False and menu.is_showing == False and menu.count_down == False :
            menu.menu_music.play(-1)
            menu.is_showing = True
        menu.update_menu_screen(mouse_pos)
    
    # countdown after closing menu
    # pygame.time.get_ticks() returns number of miliseconds that passed from pygame.init()
    # 1000 miliseconds is 1 second
    if menu.count_down:
        now = pygame.time.get_ticks()
        menu.screen.fill((1, 1, 1))
        if now - menu.last < 1000 :
            menu.screen.blit(count_down_text.render("3", True, (255,255,255)), (450, 300))
        elif now - menu.last >= 1000 and now - menu.last < 2000 :
            menu.screen.blit(count_down_text.render("2", True, (255,255,255)), (450, 300))
        elif now - menu.last >= 2000 and now - menu.last < 3000 :
            menu.screen.blit(count_down_text.render("1", True, (255,255,255)), (450, 300))
        else:
            game.gameObj.is_started = True
            menu.count_down = False
            timer.timer.start_game_time = pygame.time.get_ticks() - timer.timer.minuty*60000 - timer.timer.sekundy*1000

    
    # update/refresh window
    pygame.display.update()
    

# uninit pygame modules
pygame.quit()