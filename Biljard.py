import pygame


#Nastavitve okna za program
(width, height) = (300, 200)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Projekt-Biljard")
background_colour = (0,0,0)
screen.fill(background_colour)

pygame.display.flip()
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
pygame.display.set_caption("Projekt-Biljard")