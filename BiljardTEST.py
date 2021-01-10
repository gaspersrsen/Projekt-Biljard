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

"""Spremenljivke simulacije"""
casovniKorak = 0.1
gravitacija = 0.99 * casovniKorak
kTrenja = 0.0001 * casovniKorak
kUpor = 0.0001 * casovniKorak

#Konstruktor objektov
class Objekt:
    def __init__(self, m, x, y, v, kot, radij):
        self.m = m  #Masa
        self.x = x  #Pozicija
        self.y = y
        self.v = v  #Hitrost
        self.kot = kot
        self.radij = radij  #radij
        self.barva = (255, 255, 255)  #Barva
        self.debelina = 2  #Debelina

    def __repr__(self):
        return "Objekt(m={0.m}, x={0.x}, y={0.y}, v={0.v}, kot={0.kot}, r={0.radij})".format(self)

    def kineticnaEnergija(self):  #Kinetična energija delca
        return self.m *0.5 * (self.v * self.v)

    def potencialnaEnergija(self): #Potencialna energija delca
        return self.m * gravitacija * (visina - self.y)

    def pospesek(self, vektor): #Pospešek delca
        (self.kot, self.v) = sestejVektorja(self.kot, self.v, vektor[0], vektor[1])

    def premik(self, dt):  #Premik delca za nek čas dt
        (self.kot, self.v) = sestejVektorja(self.kot, self.v, math.pi, gravitacija)
        (self.kot, self.v) = sestejVektorja(self.kot, self.v, self.kot, -kTrenja - kUpor * self.v * self.v)
        self.x += self.v * dt * math.sin(self.kot)
        self.y -= self.v * dt * math.cos(self.kot)  #y je definiran navzdol

    def premikMiska(self, kazalec):
        razx = kazalec[0] - self.x
        razy =  kazalec[1] - self.y
        self.kot = math.pi / 2 + math.atan2(razy, razx)
        self.v = math.sqrt(razx **2 + razy ** 2) * 0.1
       
    def prikaz(self):  #Prikaz delca na ekranu
        pygame.draw.circle(ekran, self.barva, (self.x, self.y), self.radij, self.debelina)

    def odbojStena(self):  #Interakcija delca s steno
        if self.x >= sirina - self.radij:
            self.kot = -self.kot
            self.x = sirina - self.radij
        elif self.x <= self.radij:
            self.kot = -self.kot
            self.x = self.radij
        if self.y >= visina - self.radij:
            self.kot = math.pi - self.kot
            self.y = visina - self.radij
        elif self.y <= self.radij:
            self.kot = math.pi -self.kot
            self.y = self.radij

def sestejVektorja(kot1, dolzina1, kot2, dolzina2): #Seštevek dveh vekotjev
    x = math.sin(kot1) * dolzina1 + math.sin(kot2) * dolzina2
    y = math.cos(kot1) * dolzina1 + math.cos(kot2) * dolzina2
    kot  = 0.5 * math.pi - math.atan2(y, x) #Pazi ker je y definiran navzdol
    dolzina = math.sqrt(x ** 2 + y ** 2)
    return (kot, dolzina)

def razdalja(d1, d2): #Razdalja med dvema delcema
    razx = d1.x - d2.x
    razy =  d1.y - d2.y
    return math.sqrt(razx ** 2 + razy ** 2)

def znotrajDelca(Delci, x, y):  #Ali je naša pozicija znotraj kakšnega delca
    for d in Delci:
        if math.sqrt((d.x - x) ** 2 + (d.y - y) ** 2) <= d.radij:
            return d


def odboj(d1, d2):
    razx = d1.x - d2.x
    razy =  d1.y - d2.y
    sestm = d1.m + d2.m
    razm = d1.m - d2.m
    r2 = d2.radij + d1.radij
    odmik = razdalja(d1, d2)
    kinPred = d1.kineticnaEnergija() + d2.kineticnaEnergija()
    if (odmik < r2):
        kotOdboja = math.atan2(razy, razx) + math.pi / 2
        (d1.kot, d1.v) = sestejVektorja(d1.kot, d1.v * razm / sestm, kotOdboja, 2 * d2.v * d2.m / sestm)
        (d2.kot, d2.v) = sestejVektorja(d2.kot, d2.v * (-razm) / sestm, kotOdboja + math.pi, 2 * d1.v * d1.m / sestm)
        kinPo = d1.kineticnaEnergija() + d2.kineticnaEnergija()
        popravekKin = 1
        if (kinPo != 0):
            popravekKin = math.sqrt(kinPred / kinPo)
            
        d1.v *= popravekKin
        d2.v *= popravekKin 


        prekrivanje = 0.6 * (r2 - razdalja(d1, d2) + 1)
        d1.x += math.sin(kotOdboja) * prekrivanje
        d1.y -= math.cos(kotOdboja) * prekrivanje
        d2.x -= math.sin(kotOdboja) * prekrivanje
        d2.y += math.cos(kotOdboja) * prekrivanje

"""TEST"""
steviloDelcev=100
mojiDelci=[]
for i in range(steviloDelcev):
    m = random.randint(1, 10)
    radij = random.randint(10, 50)
    x = random.randint(radij, int(sirina - radij))
    y = random.randint(radij, int(visina - radij))
    v = random.randint(-3, 3)
    kot = random.uniform(-math.pi, math.pi)
    mojiDelci.append(Objekt(m, x, y, v, kot, radij))
"""TEST"""
#Požene program ter čaka na zaprtje
running = True
izbranDelec = None

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  #Izhod iz simulacije
            running = False
            print(errors)
        if event.type == pygame.MOUSEBUTTONDOWN:  #Pritisk miške
            (kazalecX, kazalecY) = pygame.mouse.get_pos()
            izbranDelec = znotrajDelca(mojiDelci, kazalecX, kazalecY)
        elif event.type == pygame.MOUSEBUTTONUP:
            izbranDelec = None

    ekran.fill(barvaOzadja)  #Simulacija
    En = 0
    if izbranDelec:  #Ročni premik delca
        izbranDelec.premikMiska(pygame.mouse.get_pos())
    for i, delec in enumerate(mojiDelci):
        delec.premik(casovniKorak)
        delec.odbojStena()
        for delec2 in mojiDelci[i+1:]:
            odboj(delec, delec2)
        delec.prikaz()
        En += delec.kineticnaEnergija() + delec.potencialnaEnergija()
    print(En)
    pygame.display.flip()