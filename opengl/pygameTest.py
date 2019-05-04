import pygame
import time

class carGame():

    width = 800
    height = 800
    carWidth = 145
    carHeight = 250

    black = (0,0,0)
    white = (255,255,255)
    red   = (255,0,0)
    green = (0,255,0)
    blue  = (0,0,255)


# ####################################################
# ### SKRIV KOD HÄR ##################################
# ####################################################

    # ################################################
    # Returnera förändring i x led
    # ################################################
    def leftPressed(self):
        print("<----- left")
        return 0

    # ################################################
    # Returnera förändring i x led
    # ################################################
    def rightPressed(self):
        print("-----> right")
        return 0

    # ################################################
    # returnera förändring i x led
    # ################################################
    def nothingPressed(self):
        print("------ nothing")
        return 0


# ####################################################
# ### SLUT KOD HÄR ###################################
# ####################################################


    def __init__(self):

        pygame.init()
        self.eventCallbacks = {}

        self.gameDisplay = pygame.display.set_mode((carGame.width,carGame.height))
        pygame.display.set_caption("Racing!")
        self.clock = pygame.time.Clock()

        self.carImg = pygame.image.load("top-car-view-png-34861.png")
        self.carImg = pygame.transform.scale(self.carImg, (carGame.carHeight, carGame.carWidth))
        self.carImg = pygame.transform.rotate(self.carImg, 90)


    # ################################################
    # ...
    # ################################################
    def car(self, x,y):
        self.gameDisplay.blit(self.carImg, (x, y))

    def text_objects(self, text, font, color=red):
        textSurface = font.render(text, True, color)
        return textSurface, textSurface.get_rect()

    def message_display(self, text):
        largeText = pygame.font.Font("freesansbold.ttf", 115)
        TextSurf, TextRect = self.text_objects(text, largeText)
        TextRect.center = ((carGame.width / 2, carGame.height / 2))
        self.gameDisplay.blit(TextSurf, TextRect)
        pygame.display.update()
        time.sleep(2)

    # ################################################
    # ...
    # ################################################
    def crash(self):
        self.message_display("You crashed")


    # ################################################
    # pappas loop
    # ################################################
    def gameLoop(self):

        x = (carGame.width * 0.45)
        y = (carGame.height * 0.65)

        x_change = 0

        gameExit = False

        while not gameExit:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("Exit :-(")
                    gameExit = True
                if event.type == pygame.KEYUP:
                    # Cancel keypress only if we still are going in the direction of the key-up event
                    if (event.key == pygame.K_LEFT and x_change < 0) or \
                            (event.key == pygame.K_RIGHT and x_change > 0):
                        x_change = self.nothingPressed()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x_change = self.leftPressed()
                        break
                    if event.key == pygame.K_RIGHT:
                        x_change = self.rightPressed()
                        break

            x += x_change

            self.gameDisplay.fill(carGame.white)
            self.car(x + x_change, y)

            if x > (carGame.width - carGame.carWidth * 0.5) or x < (carGame.carWidth * -0.3):
                self.crash()

            pygame.display.update()
            self.clock.tick(60)

        pygame.quit()
        exit(0)

if __name__ == "__main__":
    myGame = carGame()
    myGame.gameLoop()



