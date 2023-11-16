import pygame # Importerer spillet
from sys import exit # Gjør sånn at du kan gå ut av pygame 

# Bilder 
spiller_bilde = pygame.image.load("bilder/spiller.png")
hai_bilde = pygame.image.load("bilder/hai.png")
sand_bilde = pygame.image.load("bilder/sand.png")
havet_bilde = pygame.image.load("bilder/havet.png")
gress_bilde = pygame.image.load("bilder/gress.png")

# spill variabler 

bakke_fart = 1 # hvor for bakken kommer til å bevege seg og hindrene kommer til å komme 

class Bakke (pygame.sprite.Sprite): 
    def __init__(self, *groups: _Group) -> None:
        super().__init__(*groups)

# 1. Oppsett
pygame.init() # Importerer alle pygame funksjonene
klokke = pygame.time.Clock() # Deffinerer tiden

HOYDE = 600 
BREDDE = 720

vindu = pygame.display.set_mode((BREDDE, HOYDE)) # Lager et vindu med de definerte konstante variablene 

pygame.display.set_caption('FISKESPILL') # Navnt til spillet 
# 2. Håndere input 
def quit_game(): # Funksjon som gjør det mulig å avslutte spillet, med å trykke på den røde knappen
    # Exit game 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


# 3.  Opptatere spill
# Game main method 
def main(): 
    start = True
    while start:
        # Quit
        quit_game() # Lar oss avslutte spillet





# 4. Tegne 
        # Reset Frame
        vindu.fill((0, 0, 0)) # Setter bagrunnsfargen i form av RGB values som er Rød Grønn og Blå

        # Tegne bakgrunn
        vindu.blit(havet_bilde, (0, 0)) # bruker et bilde som bakgrunn, andre agrum entet er hvor på skjermen jeg ønsker vinduet 

        klokke.tick(60) # hvor mange ruter spillet skal bevege seg i pr sek, limmiterer til 60 "frams"pr sekund
        pygame.display.update() # Hvis stemmer opptatere vindet

main()