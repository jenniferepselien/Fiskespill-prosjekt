import pygame # Importerer spillet
from sys import exit # Gjør sånn at du kan gå ut av pygame 
import random

pygame.display.set_caption('FISKESPILL') # Navnt til spillet 

# 1. Oppsett 
pygame.init() # Importerer alle pygame funksjonene
klokke = pygame.time.Clock() # Deffinerer tiden

HOYDE = 600 
BREDDE = 720
vindu = pygame.display.set_mode((BREDDE, HOYDE)) # Lager et vindu med de definerte konstante variablene 


# Bilder 
spiller_bilde = [
                pygame.transform.scale_by(pygame.image.load("bilder/spiller.png").convert_alpha(), 0.15),
                pygame.transform.scale_by(pygame.image.load("bilder/spiller-ned.png").convert_alpha(), 0.15),
                pygame.transform.scale_by(pygame.image.load("bilder/spiller-opp.png").convert_alpha(), 0.15)]
hai_bilde = pygame.transform.scale_by(pygame.image.load("bilder/hai.png").convert_alpha(), 0.25)
sand_bilde = pygame.image.load("bilder/sand.png")
havet_bilde = pygame.image.load("bilder/havet.png")
gress_bilde = pygame.transform.scale_by(pygame.image.load("bilder/gress.png").convert_alpha(), 0.25)

# spill variabler 

bakke_fart = 1 # hvor for bakken kommer til å bevege seg og hindrene kommer til å komme 
fisk_start_pos = (100, 250)
poeng = 0 
font = pygame.font.SysFont('Areal', 26)

class Hinder(pygame.sprite.Sprite):
    # ...

    def update(self):
        # beveger hindre 
        self.rect.x -= bakke_fart
        if self.rect.x <= - BREDDE:
            self.kill()

        # Poeng 
        global poeng
        if self.hinder_typ == 'gress':
            if fisk_start_pos[0] > self.rect.bottomleft[0] and not self.passed:
                self.enter = True
            if fisk_start_pos[0] > self.rect.bottomright[0] and not self.passed:
                self.exit = True
            if self.enter and self.exit and not self.passed: 
                self.passed = True
                poeng += 1

        
    # Poeng 
        global poeng
        if self.hinder_typ == 'gress':
            if fisk_start_pos[0] > self.rect.bottomleft[0] and not self.passed:
                self.enter = True
            if fisk_start_pos[0] > self.rect.bottomright[0] and not self.passed:
                self.exit = True
            if self.enter and self.exit and not self.passed: 
                self.passed = True
                poeng += 1

class Fisk(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = spiller_bilde[0]
        self.rect = self.image.get_rect()
        #self.image = pygame.transform.scale(self.image, (10, 10))
        # self.image = pygame.transform.scale_by(spiller_bilde, 0.4)
       #  self.image = pygame.transform.scale(origin al_image, (spiller_x, spiller_y))
        self.rect.center = fisk_start_pos
        self.image_index = 0
        self.vel = 0 
        self.flap = False
        self.alive = True

    def update(self, user_input):
        # animate fish
        if self.alive:
            self.image_index += 1 
        if self.image_index >= 30:
            self.image_index = 0 
        # self.image = spiller_bilde[self.image_index // 10]
        self.image = spiller_bilde[self.image_index // 10]
        # self.image = pygame.transform.scale_by(self.bilde, 0.2)

        # self.scaled_image = pygame.transform.scale(self.image, (10, 10)) # Ny

    # gravity and flap 
        self.vel += 0.5
        if self.vel > 7:
            self.vel = 7
        if self.rect.y < 500: 
            self.rect.y += int(self.vel)
        if self.vel == 0:
            self.flap = False
        

        # rotate fisk 
        self.image = pygame.transform.rotate(self.image, self.vel * -7)

        # user input 
        if user_input[pygame.K_SPACE] and not self.flap and self.rect.y > 0 and self.alive:
            self.flap = True
            self.vel = -7 

class Bakke (pygame.sprite.Sprite): 
    def __init__(self, x, y): #  koordinater for den nedre delen av bilde 
        pygame.sprite.Sprite.__init__(self)
        self.image = sand_bilde 
        self.rect = self.image.get_rect() #gir oss en rectangel rundt bakken
        self.rect.x, self.rect.y = x, y

    def update(self):
        # Beveger på bakken
        self.rect.x -= bakke_fart 
        if self.rect.x <= -BREDDE:
            self.kill()

# 1. Oppsett

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
    global poeng

    # Instaniate fisk
    fisk = pygame.sprite.GroupSingle()
    fisk.add(Fisk())

    # Hindringer 
    hinder_tid = 0
    hinder = pygame.sprite.Group()

    # Instantiate Initial Ground 
    x_pos_bakke, y_pos_bakke = 0, 360
    bakke = pygame.sprite.Group()
    bakke.add(Bakke(x_pos_bakke, y_pos_bakke))


    start = True
    while start:
        # Quit
        quit_game() # Lar oss avslutte spillet
# 4. Tegne 
        # Reset Frame
        vindu.fill((0, 0, 0)) # Setter bagrunnsfargen i form av RGB values som er Rød Grønn og Blå

       

        # User input 
        user_input = pygame.key.get_pressed()

        # Tegne bakgrunn
        vindu.blit(havet_bilde, (0, 0)) # bruker et bilde som bakgrunn, andre agrum entet er hvor på skjermen jeg ønsker vinduet 
        # vindu.blit(spiller_bilde, (spiller_x, spiller_y))
        # Spawn Ground

        if len(bakke) <= 2:
            bakke.add(Bakke(BREDDE, y_pos_bakke))

        # Draw - Pipes, ground and bird 
        bakke.draw(vindu)
        fisk.draw(vindu)
        hinder.draw(vindu)

        poeng_text = font.render('Poeng: ' + str(poeng), True, pygame.Color(255, 255, 255))
        vindu.blit(poeng_text, (20, 20))

        #Uptate- piper, grounds and bird
        if fisk.sprite.alive:    
            bakke.update()
            hinder.update()
        fisk.update(user_input)
        # def draw(self, surface):
            # surface.blit(self.image, self.rect)

        # Hinder spawn 
        if hinder_tid <= 0 and fisk.sprite.alive:
            x_top, x_bottom = BREDDE, BREDDE  # Endret x-posisjonene til høyre kant av vinduet
            y_top = random.randint(10, 300)  # Justert området for tilfeldig vertikal posisjon
            y_bottom = y_top + random.randint(90, 130) + gress_bilde.get_height()

            # Sjekker om hindret går utenfor skjermen og justerer i så fall posisjonen
            if y_bottom > HOYDE:
                y_bottom = HOYDE - gress_bilde.get_height()

            hinder.add(Hinder(x_top, y_top, hai_bilde, "oppe"))
            hinder.add(Hinder(x_bottom, y_bottom, gress_bilde, "nede"))
            hinder_tid = random.randint(180, 250)


        # spawn ground 

        #if len(bakke) <= 2: 
            #bakke.add(Bakke(BREDDE, y_pos_bakke))

        klokke.tick(60) # hvor mange ruter spillet skal bevege seg i pr sek, limmiterer til 60 "frams"pr sekund
        pygame.display.update() # Hvis stemmer opptatere vindet
main()