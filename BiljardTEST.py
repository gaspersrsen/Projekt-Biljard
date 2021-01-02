import pygame
import math
import random


#Nastavitve okna za program
sirina = 1600  #px
visina = 900  #px
ekran = pygame.display.set_mode((sirina, visina))
pygame.display.set_caption("Projekt-Biljard")
barvaOzadja = (0,0,0)
ekran.fill(barvaOzadja)

#Konstruktor objektov
class Objekt:
    def __init__(self, m, x, y, vx, vy, radij):
        self.m = m  #masa
        self.x = x  #pozicija
        self.y = y
        self.vx = vx  #hitrost
        self.vy = vy
        self.radij = radij  #radij
        self.barva = (255, 255, 255)  #barva
        self.debelina = 2  #debelina
    
    def __repr__(self):
        return "Objekt(m={0.m}, x={0.x}, y={0.y}, vx={0.vx}, vy={0.vy}, r={0.r})".format(self)
    
    def kineticnaEnergija(self):  #kinetična energija delca
        return self.m *0.5 * (self.vx * self.vx + self.vy * self.vy)

    def premik(self, dt, ax=0, ay=0):  #premik delca pod vplivom pospeška za določen čas
        self.x= self.x + self.vx * dt + 0.5 * ax * dt * dt
        self.y= self.y + self.vy * dt + 0.5 * ay * dt * dt
        self.vx= self.vx + ax * dt
        self.vy= self.vy + ay * dt
       
    def prikaz(self):
        pygame.draw.circle(ekran, self.barva, (self.x, self.y), self.radij, self.debelina)

    def odbojStena(self):
        if self.x >= sirina - self.radij:
            self.vx= -self.vx
        if self.y >= visina - self.radij:
            self.vy= -self.vy


"""TEST"""
steviloDelcev=5
mojiDelci=[]
for i in range(steviloDelcev):
    m = random.randint(1, 10)
    radij = random.randint(10, 50)
    x = random.randint(radij, int(sirina - radij))
    y = random.randint(radij, int(visina - radij))
    vx = random.randint(10, 30)
    vy = random.randint(10, 30)
    mojiDelci.append(Objekt(m, x, y, vx, vy, radij))


for delec in mojiDelci:
    delec.prikaz()

for i in range(1000):
    for delec in mojiDelci:
        delec.premik(1)
        delec.odbojStena()
        delec.prikaz()
"""TEST"""

#Požene program ter čaka na zaprtje
pygame.display.flip()
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
pygame.display.set_caption("Projekt-Biljard")