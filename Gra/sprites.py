import pygame

# tajemniczy mysi sprzęt <3
class sprite_sheet():
    def __init__(self, image):
        self.sheet = image
    
    def get_sprite(self, frame, sprite_width, sprite_height, placement_width, placement_height, scale, sprite_colour):
        image = pygame.Surface((sprite_width, sprite_height)).convert_alpha()
        image.blit(self.sheet, (placement_width, placement_height), (frame * sprite_width, 0, sprite_width, sprite_height))
        image = pygame.transform.scale(image, (sprite_width * scale, sprite_height * scale))
        image.set_colorkey(sprite_colour)
        
        return image