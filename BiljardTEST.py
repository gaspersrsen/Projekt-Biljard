import pygame
import Funkcije


#Nastavitve okna za program
simulacija = Funkcije.Okolje(1600, 900) #Definicija simulacije in dimenzije okna
ekran = pygame.display.set_mode((simulacija.sirina, simulacija.visina))
pygame.display.set_caption("Projekt-Biljard")

#Delci
simulacija.dodajDelec(30)

#Požene program ter čaka na zaprtje
running = True
izbranDelec = None

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  #Izhod iz simulacije
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:  #Pritisk miške
            izbranDelec = simulacija.znotrajDelca(pygame.mouse.get_pos())
        elif event.type == pygame.MOUSEBUTTONUP:
            izbranDelec = None

    ekran.fill(simulacija.barva)  #Počistimo ekran
    if izbranDelec:  #Ročni premik delca
        izbranDelec.premikMiska(pygame.mouse.get_pos())
    
    simulacija.simuliraj()
    for delec in simulacija.delci:
        pygame.draw.circle(ekran, delec.barva, (delec.x, delec.y), delec.radij, delec.debelina)
    
    pygame.display.flip()