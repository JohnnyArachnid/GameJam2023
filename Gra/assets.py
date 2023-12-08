import pygame

# screen variable is here only to allow convert and convert_alpha
screen = pygame.display.set_mode()

#buttony

button_image = pygame.image.load("./assets/pucha_button.png").convert_alpha()
button_image = pygame.transform.scale(button_image, (200,50))
plus_button_image = pygame.image.load("./assets/plus_button.png").convert_alpha()
minus_button_image = pygame.image.load("./assets/minus_button.png").convert_alpha()

# background
how_to_play = pygame.image.load("./assets/how_to_play.png").convert()
end_screen = pygame.image.load("./assets/end_screen.png").convert()

menu_background = pygame.image.load("./assets/Mapa.png").convert()
menu_background = pygame.transform.scale(menu_background,(1024,768))

grass_1 = pygame.image.load("./assets/Trawa1.png").convert()
grass_1 = pygame.transform.scale(grass_1,(120,120))

grass_2 = pygame.image.load("./assets/Trawa2.png").convert()
grass_2 = pygame.transform.scale(grass_2,(120,120))

# default invisible background tile 256x256 pixels
beton = pygame.image.load("./assets/Droga_Jedna_Srodek_Ukos.png").convert()
beton = pygame.transform.scale(beton,(120,120))

dach = pygame.image.load("./assets/Dach.png").convert()
dach = pygame.transform.scale(dach,(120,120))
budynek_1 = pygame.image.load("./assets/Dach1.png").convert()
budynek_1 = pygame.transform.scale(budynek_1,(120,120))
budynek_2 = pygame.image.load("./assets/Dach2.png").convert()
budynek_2 = pygame.transform.scale(budynek_2,(120,120))


budynek_3 = pygame.image.load("./assets/Dach2.png").convert()
budynek_4 = pygame.image.load("./assets/invis.png").convert()

beton_kraw_1 = pygame.image.load("./assets/Droga_Jedna_Ukos_Lewy_Ukos.png").convert()
beton_kraw_1 = pygame.transform.scale(beton_kraw_1,(120,120))
beton_kraw_2 = pygame.image.load("./assets/Droga_Jedna_Ukos_Prawy_Ukos.png").convert()
beton_kraw_2 = pygame.transform.scale(beton_kraw_2,(120,120))

cien = pygame.image.load("./assets/cien.png").convert_alpha()
cien = pygame.transform.scale(cien, (1024,628))
# structures

bacground_tiles = dict([
    (0, beton),
    (1, grass_1),
    (2, grass_2),
    (3, beton),
    (4, dach),
    (5, budynek_1),
    (6, budynek_2),
    (7, beton_kraw_1),
    (8, beton_kraw_2),
])



# corner
# wall
invis = pygame.image.load("./assets/invis.png").convert_alpha()
siatka_1 = pygame.image.load("./assets/Siatka_Lewo.png").convert_alpha()
siatka_1 = pygame.transform.scale(siatka_1,(120,120))
siatka_2 = pygame.image.load("./assets/Siatka_Prawo.png").convert_alpha()
siatka_2 = pygame.transform.scale(siatka_2,(120,120))

kosz = pygame.image.load("./assets/Kosz_Pusty.png").convert_alpha()
kosz = pygame.transform.scale(kosz,(120,120))

kosz_pelny = pygame.image.load("./assets/Kosz_Pelny.png").convert_alpha()
kosz_pelny = pygame.transform.scale(kosz_pelny,(120,120))

toi_toi = pygame.image.load("./assets/Toaleta Prawo.png").convert_alpha()
toi_toi = pygame.transform.scale(toi_toi,(120,120))

lawka_lewy = pygame.image.load("./assets/Lawka_lewo.png").convert_alpha()
lawka_lewy = pygame.transform.scale(lawka_lewy,(120,120))
lawka_prawy = pygame.image.load("./assets/Lawka_Prawo.png").convert_alpha()
lawka_prawy = pygame.transform.scale(lawka_prawy,(120,120))

lawka_top_1 = pygame.image.load("./assets/Lawka_Gora1.png").convert_alpha()
lawka_top_1 = pygame.transform.scale(lawka_top_1,(120,120))
lawka_top_2 = pygame.image.load("./assets/Lawka_Gora2.png").convert_alpha()
lawka_top_2 = pygame.transform.scale(lawka_top_2,(120,120))

lawka_bottom_1 = pygame.image.load("./assets/Lawka_Dol1.png").convert_alpha()
lawka_bottom_1 = pygame.transform.scale(lawka_bottom_1,(120,120))
lawka_bottom_2 = pygame.image.load("./assets/Lawka_Dol2.png").convert_alpha()
lawka_bottom_2 = pygame.transform.scale(lawka_bottom_2,(120,120))

iglak_gora_left = pygame.image.load("./assets/Iglaste1.png").convert_alpha()
iglak_gora_left = pygame.transform.scale(iglak_gora_left,(120,120))
iglak_dol_left = pygame.image.load("./assets/Iglaste2.png").convert_alpha()
iglak_dol_left = pygame.transform.scale(iglak_dol_left,(120,120))
iglak_gora_right = pygame.image.load("./assets/Iglaste3.png").convert_alpha()
iglak_gora_right = pygame.transform.scale(iglak_gora_right,(120,120))
iglak_dol_right = pygame.image.load("./assets/Iglaste4.png").convert_alpha()
iglak_dol_right = pygame.transform.scale(iglak_dol_right,(120,120))

structure_tiles = dict([
    (-2, siatka_1),
    (-3, siatka_2),
    (2, invis),
    (3, kosz),
    (4, kosz_pelny),
    (5, toi_toi),
    (6, lawka_prawy),
    (7, lawka_lewy),
    (8, lawka_bottom_1),
    (9, lawka_bottom_2),
    (10, lawka_top_1),
    (11, lawka_top_2),
    (12, iglak_gora_left),
    (13, iglak_dol_left),
    (14, iglak_gora_right),
    (15, iglak_dol_right),
])