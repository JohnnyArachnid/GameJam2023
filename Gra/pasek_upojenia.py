import pygame
import timer
import math

class Pasek_upojenia:
    pasek_width = 600
    pasek_height = 50
    pasek_x = 212
    pasek_y = 688
    
    # przez co przegrano, to istnieje by wyświetlać różne wiadomości w zależności od końca gry
    left = False
    right = False
    
    pasek_wskaznik_x = 510
    pasek_wskaznik_y = 684
    pasek_wskaznik_width = 4
    pasek_wskaznik_height = 58
    pasek_wskaznik_score = 300
    pasek_modifier = 0.5
    
    pasek_image = ""
    pasek_wskaznik_image = ""
    
    last_wskaznik_movement = pygame.time.get_ticks()
    
    def __init__(self, granica_bottom, granica_top) :
        self.pasek_image = pygame.image.load("./assets/pasek_upojenia.png").convert()
                
        self.pasek_wskaznik_image = pygame.Surface((self.pasek_wskaznik_width, self.pasek_wskaznik_height)).convert()
        
        self.granica_bottom = granica_bottom
        self.granica_top = granica_top
        
    def update_pasek(self, screen) :
        action = False
                
        screen.blit(self.pasek_image, (self.pasek_x,self.pasek_y))
        
        screen.blit(self.pasek_wskaznik_image, (self.pasek_wskaznik_x, self.pasek_wskaznik_y))
        
        self.update_wskaznik()
        
        if self.pasek_wskaznik_score <= self.granica_bottom :
            action = True
            self.left = True
        elif self.pasek_wskaznik_score >= 600 - self.granica_top :
            action = True
            self.right = True
        
        return action

    def update_wskaznik(self) :
        now = pygame.time.get_ticks()
        if now - self.last_wskaznik_movement >= 1000 :
            self.pasek_wskaznik_score -= math.floor(6*timer.timer.modifier)
            self.pasek_wskaznik_x -= math.floor(6*timer.timer.modifier)
            self.pasek_modifier = math.ceil((self.pasek_wskaznik_score - 3)/10)
            self.last_wskaznik_movement = now
    
    def reset_variables(self) :
        # przez co przegrano, to istnieje by wyświetlać różne wiadomości w zależności od końca gry
        self.left = False
        self.right = False
        
        self.pasek_wskaznik_x = 510
        self.pasek_wskaznik_score = 300
        # im mniejszy modifier tym szybciej wskaznik przesuwa sie w lewo
        self.wskaznik_modifier = 0.5
            