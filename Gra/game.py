import pygame
import math
import settings
import map
import player
import pasek_upojenia
import assets
import pop_up_window
import sprites_anim
import timer

class Game :
    # width and height of a window
    width = int( settings.config["window_width"] )
    height = int( settings.config["window_height"] )

    # game screen init
    screen = pygame.display.set_mode((width, height))

    # is game started
    is_started = False

    # pop_up windows
    start_pop_up_window = pop_up_window.Pop_up_window(200, 100, 600, 600, "", 20, (19, 86, 121))
    end_game_left_border_pop_up_window = pop_up_window.Pop_up_window(200, 100, 600, 600, "You fell aslep \ xx:xx", 20, (19, 86, 121))
    end_game_right_border_pop_up_window = pop_up_window.Pop_up_window(200, 100, 600, 600, "Cardiac arrest \ xx:xx", 20, (19, 86, 121))

    show_pop_up_window = True
    current_pop_up_window = start_pop_up_window

    # background variables
    tile_width = 120
    tile_height = 120
    # tiles are displayed based on center piece
    center_tile_x_cord = int( width/2 - tile_width ) # window size is 4*256 x 3*256 so correction is needed
    center_tile_y_cord = int( height/2 )

    # number of tiles displayed on screen
    number_of_tiles_in_row = math.ceil( width / tile_width )
    number_of_tiles_in_column = math.ceil( height / tile_height ) + 1
    
    # how much background is scrolled
    map_center_tile_x_cord = map.player_pos_x_on_map * tile_width
    map_center_tile_y_cord = map.player_pos_y_on_map * tile_height

    scroll_x = int( map_center_tile_x_cord + tile_width/2 )
    scroll_y = int( map_center_tile_y_cord )

    scroll_x_delta = scroll_x % tile_width
    scroll_y_delta = scroll_y % tile_height

    map.player_pos_x_on_map = map.map_width - int( scroll_x / tile_width )
    map.player_pos_y_on_map = map.map_height - int( scroll_y / tile_height )

    # pasek upojenia
    pasek = pasek_upojenia.Pasek_upojenia(0, 0)

    # collision
    collision_tolerance = int((player.speed+2)*timer.timer.modifier*2)
    wall_rect_to_collide = []
    collision_top = False
    collision_bottom = False
    collision_left = False
    collision_right = False

    # animation
    student_to_be_animated = []
    piwo_to_be_animated = []
    
    # piwo
    piwo_score = int(20*timer.timer.modifier)
    piwo_sound = pygame.mixer.Sound("./audio/Otwieranie_Puchy.mp3")


    gra_muzyka = pygame.mixer.Sound("./audio/Gra.mp3")

    # kto pozwolił mi napisać ten syf 

    def check_piwo_collision(self):
        for rect in self.piwo_to_be_animated :
            if player.player_rect.colliderect(rect[0]) :
                map.structure_map[rect[1][0]][rect[1][1]] = 0
                self.piwo_sound.play()
                self.pasek.pasek_wskaznik_score += self.piwo_score
                self.pasek.pasek_wskaznik_x += self.piwo_score


    def check_for_collisions(self) :
        self.collision_bottom = False
        self.collision_top = False
        self.collision_right = False
        self.collision_left = False

        for rect in self.wall_rect_to_collide :
            if player.player_rect.colliderect(rect) :
                if abs(rect.top - player.player_rect.bottom) < self.collision_tolerance :
                    self.collision_bottom = True
                    self.collision_top = False
                    self.scroll_y += abs(rect.top - player.player_rect.bottom)
                if abs(rect.bottom - player.player_rect.top) < self.collision_tolerance :
                    self.collision_top = True
                    self.collision_bottom = False
                    self.scroll_y -= abs(rect.bottom - player.player_rect.top)
                if abs(rect.left - player.player_rect.right) < self.collision_tolerance :
                    self.collision_right = True
                    self.collision_left = False
                    self.scroll_x += abs(rect.left - player.player_rect.right)
                if abs(rect.right - player.player_rect.left) < self.collision_tolerance :
                    self.collision_left = True
                    self.collision_right = False
                    self.scroll_x -= abs(rect.right - player.player_rect.left)            



    def reset_game_variables(self):
        self.gra_muzyka.stop()
        self.show_pop_up_window = True
        self.current_pop_up_window = self.start_pop_up_window

        self.scroll_x = int( self.map_center_tile_x_cord + self.tile_width/2 )
        self.scroll_y = int( self.map_center_tile_y_cord + self.tile_height/2 )

        self.scroll_x_delta = self.scroll_x % self.tile_width
        self.scroll_y_delta = self.scroll_y % self.tile_height

        map.player_pos_x_on_map = map.map_width - int( self.scroll_x / self.tile_width )
        map.player_pos_y_on_map = map.map_height - int( self.scroll_y / self.tile_height)
        
        self.pasek.reset_variables()
        timer.timer.reset_timer()
        map.structure_map = map.structure_map_without_students.copy()
        map.new_map(map.structure_map)

    def change_pop_up_window(self, val):
        self.show_pop_up_window = True
        match val :
            case 0:
                self.current_pop_up_window = self.end_game_left_border_pop_up_window
                self.current_pop_up_window.text = "You fell aslep \ " + str(timer.timer.minuty) + ":" + str(timer.timer.sekundy)
            case 1:
                self.current_pop_up_window = self.end_game_right_border_pop_up_window
                self.current_pop_up_window.text = "Cardiac arrest \ " + str(timer.timer.minuty) + ":" + str(timer.timer.sekundy)



    def update_game_screen(self, mouse_pos):
        
        self.screen.fill((255, 111, 255))
        
        # here update background but not player, enemies etc.

        self.wall_rect_to_collide = []
        self.student_to_be_animated = []
        self.piwo_to_be_animated = []
        # drawing background
        for i in range( -self.number_of_tiles_in_row + 1, self.number_of_tiles_in_row ) :
            for j in range( -self.number_of_tiles_in_column + 1, self.number_of_tiles_in_column ) :
                # display texture based on number in map
                texture_num = map.map[map.player_pos_x_on_map + i][map.player_pos_y_on_map + j] # get texture number
                # blit texture
                self.screen.blit(assets.bacground_tiles[texture_num], (self.center_tile_x_cord + self.tile_width*i + self.scroll_x_delta, self.center_tile_y_cord + self.tile_height*j + self.scroll_y_delta))
                
                # blit structure
                structure_num = map.structure_map[map.player_pos_x_on_map + i][map.player_pos_y_on_map + j]
                if structure_num == -1 :
                    # self.screen.blit(assets.structure_tiles[-1], (self.center_tile_x_cord + self.tile_width*i + self.scroll_x_delta, self.center_tile_y_cord + self.tile_height*j + self.scroll_y_delta))
                    rect = pygame.Rect(self.center_tile_x_cord + self.tile_width*i + self.scroll_x_delta,self.center_tile_y_cord + self.tile_height*j + self.scroll_y_delta,120,120)
                    self.student_to_be_animated.append((rect,(map.player_pos_x_on_map + i,map.player_pos_y_on_map + j)))
                    self.wall_rect_to_collide.append(rect)
                if structure_num != -1 and structure_num != 1 and structure_num != 0:
                    self.screen.blit(assets.structure_tiles[structure_num], (self.center_tile_x_cord + self.tile_width*i + self.scroll_x_delta, self.center_tile_y_cord + self.tile_height*j + self.scroll_y_delta))
                    rect = assets.structure_tiles[structure_num].get_rect()
                    rect.left = self.center_tile_x_cord + self.tile_width*i + self.scroll_x_delta
                    rect.top = self.center_tile_y_cord + self.tile_height*j + self.scroll_y_delta
                    self.wall_rect_to_collide.append(rect)
                if structure_num == 1:
                    rect = pygame.Rect(self.center_tile_x_cord + self.tile_width*i + self.scroll_x_delta,self.center_tile_y_cord + self.tile_height*j + self.scroll_y_delta,self.tile_width,self.tile_height)
                    self.piwo_to_be_animated.append((rect, (map.player_pos_x_on_map + i,map.player_pos_y_on_map + j)))

        # animating player
        sprites_anim.draw_anime(sprites_anim.player_animation_list, sprites_anim.player_cooldown, sprites_anim.player_move, sprites_anim.player_direction, self.screen, self.width/2-12*5, self.height/2-12*5, 0)
        
        # animating rest
        for rect in self.student_to_be_animated :
            direction = map.studenciaki_biedaki[str(rect[1][0]) + "_" + str(rect[1][1])]
            sprites_anim.draw_anime(sprites_anim.student_animation_list, sprites_anim.student_cooldown, True, direction, self.screen, rect[0].left, rect[0].top, 1)
        for rect in self.piwo_to_be_animated :
            sprites_anim.draw_anime(sprites_anim.energy_animation_list, sprites_anim.energy_cooldown, True, 0, self.screen, rect[0].left, rect[0].top, 2)
        
        if self.show_pop_up_window :
            if self.current_pop_up_window.draw(self.screen, mouse_pos) :
                self.show_pop_up_window = False
                timer.timer.start_game_time = pygame.time.get_ticks()
                if self.current_pop_up_window == self.end_game_left_border_pop_up_window or self.current_pop_up_window == self.end_game_right_border_pop_up_window :
                    self.is_started = False
                    self.reset_game_variables()
        else:            
            # get keypresses
            key = pygame.key.get_pressed()
            sprites_anim.player_move = False
            if key[pygame.K_a] and self.collision_left == False : # left movement
                sprites_anim.player_move = True
                sprites_anim.player_direction = 3
                self.scroll_x += player.speed
            if key[pygame.K_d] and self.collision_right == False : # right movement
                sprites_anim.player_move = True
                sprites_anim.player_direction = 2
                self.scroll_x -= player.speed
            if key[pygame.K_w] and self.collision_top == False : # up movement
                sprites_anim.player_move = True
                sprites_anim.player_direction = 1
                self.scroll_y += player.speed
            if key[pygame.K_s] and self.collision_bottom == False : # down movement
                sprites_anim.player_move = True
                sprites_anim.player_direction = 0
                self.scroll_y -= player.speed
                            
            # update texture change
            self.scroll_x_delta = self.scroll_x % self.tile_width
            self.scroll_y_delta = self.scroll_y % self.tile_height

            # update player position on map
            map.player_pos_x_on_map = map.map_width - int( self.scroll_x / self.tile_width )
            map.player_pos_y_on_map = map.map_height - int( self.scroll_y / self.tile_height)
        
            self.check_for_collisions()
            self.check_piwo_collision()

        
            pygame.draw.rect(self.screen, (50,50,50), (0, 628, 1024, 768))
            # if thats true end game
            if self.pasek.update_pasek(self.screen) :
                if self.pasek.left :
                    self.change_pop_up_window(0)
                else :
                    self.change_pop_up_window(1)

            if timer.timer.current_time - timer.timer.pucha_time > 1000:
                timer.timer.modifier += 0.05
                timer.timer.pucha_time = timer.timer.current_time
                for i in range(3 + int(timer.timer.time_passed/30000)):
                    map.add_pucha(map.structure_map, map.map_width, map.map_height, map.player_pos_x_on_map, map.player_pos_y_on_map, self.number_of_tiles_in_row, self.number_of_tiles_in_column)

            timer.timer.display_time(self.screen)
            self.screen.blit(assets.cien, (0,0))
          

# game class object
gameObj = Game()