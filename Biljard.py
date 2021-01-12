import pygame
import Funkcije
import getopt
import sys
import csv
import UporabniskoOkno as uo


cmdArgumenti = sys.argv
argumentiSeznam = cmdArgumenti[1:]
kratkaOblika = "f:g:t:u:k:n:m"
dolgaOblika = ["File=", "gravitacija=", "kTrenja=", "kUpor=", "gravKonst=", "steviloDelcev", "mavrica"]
File = None
nakljucnaBarva = 0
try:
    argumenti, vrednosti = getopt.getopt(argumentiSeznam, kratkaOblika, dolgaOblika)
except getopt.error as err:
    # Output error, and return with an error code
    print (str(err))
    sys.exit(6)
for arg, vrednost in argumenti:
    if arg in ("-f", "--File"):
        File = str(vrednost.strip("="))
    elif arg in ("-g", "--gravitacija"):
        uo.gravitacija.vel = float(vrednost.strip("="))
    elif arg in ("-t=", "--kTrenja"):
        uo.kTrenja.vel = float(vrednost.strip("="))
    elif arg in ("-u", "--kUpor"):
        uo.kUpor.vel = float(vrednost.strip("="))
    elif arg in ("-k", "--gravKonst"):
        uo.gravKonst.vel = float(vrednost.strip("="))
    elif arg in ("-n", "--steviloDelcev"):
        steviloDelcev = float(vrednost.strip("="))
    elif arg in ("-m", "--nakljucnaBarva"):
        nakljucnaBarva = 1

pygame.init()

"""Definicija simulacije in dimenzije okna"""
simulacija = Funkcije.Okolje(uo.sirina, uo.visina)# gravitacija=0, gravKonst=0, kTrenja=0.001, kUpor=0.001) 

ekran = uo.ekran #pygame.display.set_mode((sirina, visina2))
pygame.display.set_caption("Projekt-Biljard")

#Delci
if File:
    with open(File) as csv_file:
        csvBeri = csv.reader(csv_file, delimiter=',')
        next(csvBeri, None)
        for row in csvBeri:
            simulacija.dodajDelec(1, m=float(row[0]), x=float(row[1]), y=float(row[2]),
                                    v=float(row[3]),kot=float(row[4]), radij=int(row[5]),
                                    barva=(int(row[6]),int(row[7]),int(row[8])), mavrica=int(row[9]))


else:
    simulacija.dodajDelec(100, mavrica=nakljucnaBarva)

#Požene program ter čaka na zaprtje
running = True
izbranDelec = None
pavza = False

simulacija.gravitacija = uo.gravitacija.vel
simulacija.kTrenja = uo.kTrenja.vel
simulacija.kUpor = uo.kUpor.vel
simulacija.gravKonst = uo.gravKonst.vel

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