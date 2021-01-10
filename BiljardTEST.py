import pygame
import math
import random
import numpy


#Nastavitve okna za program
sirina = 1600  #px
visina = 900  #px
ekran = pygame.display.set_mode((sirina, visina))
pygame.display.set_caption("Projekt-Biljard")
barvaOzadja = (0,0,0)
ekran.fill(barvaOzadja)

gravitacija = 0.01
casovniKorak = 0.5
kTrenja = 0.005
kUpor = 0.01


#Konstruktor objektov
class Objekt:
    def __init__(self, m, x, y, vx, vy, radij):
        self.m = m  #Masa
        self.x = x  #Pozicija
        self.y = y
        self.vx = vx  #Hitrost
        self.vy = vy
        self.radij = radij  #radij
        self.barva = (255, 255, 255)  #Barva
        self.debelina = 2  #Debelina

    def __repr__(self):
        return "Objekt(m={0.m}, x={0.x}, y={0.y}, vx={0.vx}, vy={0.vy}, r={0.r})".format(self)
    
    def kineticnaEnergija(self):  #Kinetična energija delca
        return self.m *0.5 * (self.vx * self.vx + self.vy * self.vy)

    def premik(self, dt):  #Premik delca pod vplivom pospeška za določen čas
        kot = math.atan2(self.vx, self.vy)
        ax = (-kTrenja - kUpor / self.m / self.m * delec.kineticnaEnergija()) * math.sin(kot) 
        ay = (-kTrenja - kUpor / self.m / self.m * delec.kineticnaEnergija()) * math.cos(kot) + gravitacija
        self.x= self.x + self.vx * dt + 0.5 * ax * dt * dt
        self.y= self.y + self.vy * dt + 0.5 * ay * dt * dt
        self.vx= self.vx + ax * dt
        self.vy= self.vy + ay * dt
       
    def prikaz(self):  #Prikaz delca na ekranu
        pygame.draw.circle(ekran, self.barva, (self.x, self.y), self.radij, self.debelina)

    def odbojStena(self):  #Interakcija delca s steno
        if ((self.x >= sirina - self.radij - self.vx*casovniKorak/2) or (self.x <= self.radij - self.vx*casovniKorak/2)):
            self.vx= -self.vx
        if ((self.y >= visina - self.radij - self.vy*casovniKorak/2) or (self.y <= self.radij - self.vy*casovniKorak/2)):
            self.vy= -self.vy


def znotrajDelca(Delci, x, y):  #Ali je naša pozicija znotraj kakšnega delca
    for d in Delci:
        if math.sqrt((d.x - x) * (d.x - x) + (d.y - y) * (d.y - y)) <= d.radij:
            return d

"""TEST"""
steviloDelcev=3
mojiDelci=[]
for i in range(steviloDelcev):
    m = random.randint(1, 10)
    radij = 30#random.randint(10, 50)
    x = random.randint(radij, int(sirina - radij))
    y = random.randint(radij, int(visina - radij))
    vx = random.randint(-3, 3)
    vy = random.randint(-3, 3)
    mojiDelci.append(Objekt(m, x, y, vx, vy, radij))

"""TEST"""
#Požene program ter čaka na zaprtje
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  #Izhod iz simulacije
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:  #Pritisk miške
            (kazalecX, kazalecY) = pygame.mouse.get_pos()
            izbranDelec = znotrajDelca(mojiDelci, kazalecX, kazalecY)
    ekran.fill(barvaOzadja)
    for delec in mojiDelci:
        if delec != izbranDelec:
            delec.odbojStena()
            delec.premik(casovniKorak)
        delec.prikaz()
    pygame.display.flip()