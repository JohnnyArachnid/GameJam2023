import pygame
import button
import assets

class Pop_up_window:
    text = ""
    text_pos = (0,0)
    bg_color = (0,0,0)
    x_min = 0
    y_min = 0
    def __init__(self, x_min_, y_min_, width_, height_, text_, text_font_size_ = 25, bg_color_ = (50,50,50)):
        # create rectangle to draw
        self.rect = pygame.Rect(x_min_, y_min_, width_, height_)
        self.bg_color = bg_color_

        self.x_min = x_min_
        self.y_min = y_min_

        # pygame does not support multiline text so in order to make multiple lines of text
        # text has to be split into table and rendered in loop
        
        # create text inside pop_up window
        self.text = text_
        self.paragraph = pygame.font.Font("./assets/Early_GameBoy.ttf",text_font_size_)
        # text centered
        self.text_pos = (x_min_ + width_/2 - self.paragraph.size(text_)[0]/2, y_min_ + 20)
        
        # create button to draw
        button_x_min = int( x_min_ + width_ / 2 - 100 )
        button_y_min = int( y_min_ + height_ - 10 - 50 ) # 25 is a standard button font_size
        self.button = button.Button( button_x_min, button_y_min, 200, 50, assets.button_image, "Close" )
        
    
    def draw(self, surface, mouse_pos):
        # draw rectangle window
        if self.text == "":
            surface.blit(assets.how_to_play, (self.x_min, self.y_min))
        else: 
            surface.blit(assets.end_screen, (self.x_min, self.y_min))
        
        # capture button on click
        action = self.button.draw(surface, mouse_pos)
        
        # render text inside rectangle
        surface.blit(self.paragraph.render(self.text, True, (255,255,255)), self.text_pos)
        
        return action