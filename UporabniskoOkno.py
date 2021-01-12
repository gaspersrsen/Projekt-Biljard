import math
import pygame

pygame.init()

sirina = 1600
visina= 700
X = 1200  #Širina ekrana
Y = visina + 300  #Visina ekrana



class Slider():
    def __init__(self, ime, vel, max, min, posy):
        self.vel = vel  #Začetna vrednost
        self.max = max  #Rob desno
        self.min = min  #Rob levo
        self.posx = 50  #Pozicija na ekranu
        self.posy = posy
        self.surf = pygame.surface.Surface((sirina-100, 60))
        self.pritisk = False  #Pritisk na gumb
 
        self.txt_surf = font.render(ime, 1, (0, 0, 0))
        self.txt_rect = self.txt_surf.get_rect(center=((sirina-100)/2 , 15))
 
        #Risanje ozadja
        self.surf.fill((100, 100, 100))
        pygame.draw.rect(self.surf, (255, 255, 255), [50, 40, sirina - 200, 15], 0)
        self.surf.blit(self.txt_surf, self.txt_rect)  #blit "zapeče" na ekran
 
        #Risanje krogca
        self.button_surf = pygame.surface.Surface((40, 80))
        self.button_surf.fill((1,1,1))
        self.button_surf.set_colorkey((1,1,1))
        pygame.draw.circle(self.button_surf, (0,0,0), (10, 10), 10, 6)
        pygame.draw.circle(self.button_surf, (255,0,0), (10, 10), 5, 0)

        
 
    def draw(self):
        """Risanje pravokotnika"""
        surf = self.surf.copy()

        pos = (60+int((self.vel-self.min)/(self.max-self.min)*(sirina - 200)), 77)  #Risanje krogca glede na kazalec
        self.button_rect = self.button_surf.get_rect(center=pos)
        surf.blit(self.button_surf, self.button_rect)
        self.button_rect.move_ip(self.posx, self.posy)  #Premik drsnika na pravo mesto

        self.surf2 = pygame.surface.Surface((120, 30))  #Izpisovanje vrednosti na ekran
        self.txt_surf2 = font.render(str(self.vel), 1, (255,0,0))
        self.txt_rect2 = self.txt_surf.get_rect(topleft=(sirina - 250, 5))
        self.surf.blit(self.surf2, self.txt_rect2)
        self.surf.blit(self.txt_surf2, self.txt_rect2)
 
        #Ekran
        ekran.blit(surf, (self.posx, self.posy))
 
    def move(self):
        """Spreminjanje vrednosti glede na krogec"""
        self.vel = round((pygame.mouse.get_pos()[0] - self.posx - 50) / (sirina - 200) * (self.max - self.min) + self.min , 6)
        if self.vel < self.min:
            self.vel = self.min
        if self.vel > self.max:
            self.vel = self.max


ekran = pygame.display.set_mode((sirina, Y))
font = pygame.font.SysFont("Times New Roman", 24)

gravitacija = Slider("Gravitacija", 0, 0.5, 0, visina + 0)
kTrenja = Slider("Koeficient Trenja", 0, 0.05, 0, visina + 80)
kUpor = Slider("Koeficent Upora", 0, 0.001, 0, visina + 160)
gravKonst = Slider("Gravitacijska Konstanta", 0, 0.1, -0.1, visina + 240)
drsniki = [gravitacija, kTrenja, kUpor, gravKonst]
"""
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for s in drsniki:
                if s.button_rect.collidepoint(pos):
                    s.pritisk = True
        elif event.type == pygame.MOUSEBUTTONUP:
            for s in drsniki:
                s.pritisk = False
    #Premik drsnikov
    for s in drsniki:
        if s.pritisk:
            s.move()
 
    #Pripravi ekran na novo sliko
    screen.fill((0,0,0))
 
    for s in drsniki:
        s.draw()
    pygame.display.flip()"""
