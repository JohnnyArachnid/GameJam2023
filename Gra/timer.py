import pygame
import map

class Timer:
    current_time = 0
    start_game_time = 0
    time_passed = 0
    modifier = 1

    time_display_x = 60
    time_display_y = 648
    time_display_rect = pygame.Rect(40, 648, 200, 50)
    
    minuty = 0
    sekundy = 0
    
    pucha_time = 0
    
    paragraph = pygame.font.Font("./assets/Early_GameBoy.ttf", 25)

    def update_time(self):
        self.current_time = pygame.time.get_ticks()
    
    def display_time(self, screen):
        self.update_time()
        self.time_passed = self.current_time - self.start_game_time
        self.minuty = int(self.time_passed/60000 )
        self.time_passed -= self.minuty*60000
        self.sekundy = int(self.time_passed/1000)
        time_text = str(self.minuty) + ":" + str(self.sekundy)
        text_to_display = self.paragraph.render(time_text, True, (255,255,255))
        screen.blit(text_to_display, self.time_display_rect)

        
    def reset_timer(self) :
        self.modifier = 1
        self.time_passed = 0
        self.start_game_time = 0



timer = Timer()