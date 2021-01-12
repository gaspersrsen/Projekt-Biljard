import pygame
import Funkcije
import UporabniskoOkno as uo

pygame.init()

"""Definicija simulacije in dimenzije okna"""
simulacija = Funkcije.Okolje(uo.sirina, uo.visina)# gravitacija=0, gravKonst=0, kTrenja=0.001, kUpor=0.001) 

ekran = uo.ekran #pygame.display.set_mode((sirina, visina2))
pygame.display.set_caption("Projekt-Biljard")

#Delci
simulacija.dodajDelec(100, mavrica=True)

#Požene program ter čaka na zaprtje
running = True
izbranDelec = None
pavza = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  #Izhod iz simulacije
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pavza = not pavza
                
        elif event.type == pygame.MOUSEBUTTONDOWN:  #Pritisk miške
            izbranDelec = simulacija.znotrajDelca(pygame.mouse.get_pos())
            for s in uo.drsniki:
                if s.button_rect.collidepoint(pygame.mouse.get_pos()):
                    s.pritisk = True
        elif event.type == pygame.MOUSEBUTTONUP:
            izbranDelec = None
            for s in uo.drsniki:
                s.pritisk = False
            simulacija.gravitacija = uo.gravitacija.vel
            simulacija.kTrenja = uo.kTrenja.vel
            simulacija.kUpor = uo.kUpor.vel
            simulacija.gravKonst = uo.gravKonst.vel
        
    if pavza:
        continue

    ekran.fill(simulacija.barva)  #Počistimo ekran
    if izbranDelec:  #Ročni premik delca
        izbranDelec.premikMiska(pygame.mouse.get_pos())
    
    simulacija.simuliraj()
    for delec in simulacija.delci: #Narišemo delce ter njihovo obrobo
        pygame.draw.circle(ekran, delec.barva, (delec.x, delec.y), delec.radij, delec.debelina)
        pygame.draw.circle(ekran, (255,255,255), (delec.x, delec.y), delec.radij, 2)

    for s in uo.drsniki:
        if s.pritisk:
            s.move()
        s.draw()
    
    pygame.display.flip()