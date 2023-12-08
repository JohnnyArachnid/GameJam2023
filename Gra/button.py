import pygame

# pygame Rect class documentation link
# https://www.pygame.org/docs/ref/rect.html

# list of pygame font classes, among them is SysFont and pygame.font.render
# https://www.pygame.org/docs/ref/font.html#pygame.font.SysFont

class Button:
    text = ""
    text_pos = (0,0)
    clicked = False
    bg_color = (0,0,0)
    
    def __init__(self, x_min_, y_min_, width_, height_, image, text_, font_size_ = 16):
        if width_ <= 0:
            print("error: in button width <= 0")
        if height_ <= 0:
            print("error: in button height <= 0")
        
        # creates empty paragraph with font loaded from system fonts
        self.paragraph = pygame.font.Font("./assets/Early_GameBoy.ttf", font_size_)

        # creates rectangle 
        self.rectangle = pygame.Rect(x_min_, y_min_, width_, height_)
        self.rectangle.normalize() # corrects possible negative width and height
        
        # rectangles background color
        self.image = image
        
        self.text = text_
        # centering text inside rectangle
        self.text_pos = (int( x_min_ + width_ / 2 - self.paragraph.size(self.text)[0]/2 ), int( y_min_ + height_ / 2 - self.paragraph.size(self.text)[1] / 2) )
    
    def draw(self, surface, mouse_pos):
        action = False # perform or not perform the action after clicking button
        
        surface.blit(self.image,(self.rectangle.left, self.rectangle.top))

        
        # check if mouse position is colliding with button
        if self.rectangle.collidepoint(mouse_pos):
            # [0] first element is left button mouse click
            if pygame.mouse.get_pressed()[0] and not self.clicked:
                self.clicked = True # used to disallow infinite clicking button
                action = True
        
        if not pygame.mouse.get_pressed()[0] and self.clicked : # allow again clicking
            self.clicked = False
                
        # render text inside rectangle
        surface.blit(self.paragraph.render(self.text, True, (255,255,255)), self.text_pos)
        
        return action