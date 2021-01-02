import pygame


#Nastavitve okna za program
(width, height) = (300, 200)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Projekt-Biljard")
background_colour = (0,0,0)
screen.fill(background_colour)

#Konstruktor objektov
class Objekt:
    def __init__(self, m, x, y, vx, vy, r):
        self.m = m #masa
        self.x = x #pozicija
        self.y = y
        self.vx = vx #hitrost
        self.vy = vy
        self.r = r #radij
        self.colour = (0, 0, 0) #barva
        self.thickness = 1 #debelina
    
    def __repr__(self):
        return "Objekt(m={0.m}, x={0.x}, y={0.y}, vx={0.vx}, vy={0.vy}, r={0.r})".format(self)
    
    def kineticnaEnergija(self): #kinetična energija delca
        return self.m *0.5 * (self.vx * self.vx + self.vy * self.vy)

    def premik(self, dt, ax, ay): #premik delca pod vplivom pospeška za določen čas
        self.x= self.x + self.vx * dt + 0.5 * ax * dt * dt
        self.y= self.y + self.vy * dt + 0.5 * ay * dt * dt
        self.vx= self.vx + ax * dt
        self.vy= self.vy + ay * dt




#Požene program ter čaka na zaprtje
pygame.display.flip()
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
pygame.display.set_caption("Projekt-Biljard")