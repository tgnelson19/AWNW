import pygame

class Variables:


    def __init__(self):

        pygame.init()  # Initializes a window
        pygame.display.set_caption("AWNW")

        self.infoObject = pygame.display.Info() # Gets info about native monitor res
        self.sW, self.sH = (self.infoObject.current_w, self.infoObject.current_h)

        pygame.display.set_mode((self.infoObject.current_w, self.infoObject.current_h))
        self.screen = pygame.display.set_mode([self.sW, self.sH], pygame.FULLSCREEN)  # Makes a screen that's that wide

        self.clock = pygame.time.Clock()  # Main time keeper
        self.done = False  # Determines if the game is over or not

        self.fontSize = 30
        self.font = pygame.font.Font("media/coolveticarg.otf", self.fontSize)

        self.mouseDown = False
        self.mouseX, self.mouseY = 0,0


    def eventHandler(self):
        self.clock.tick(60)  # Keeps program to only 30 frames per second
        self.mouseX, self.mouseY = pygame.mouse.get_pos() # Saves current mouse position

        for event in pygame.event.get():  # Main event handler
            if event.type == pygame.QUIT:
                self.done = True  # Close the entire program

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.done = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mouseDown = True
            if event.type == pygame.MOUSEBUTTONUP:
                self.mouseDown = False



    def finishPaint(self):
        pygame.display.flip()  # Displays currently drawn frame
        self.screen.fill(pygame.Color(0, 0, 0))  # Clears screen with a black color



    def doAnUpdate(self):

        self.eventHandler()  # Updates with any potential user interaction

        self.bugCheckerOnMousePos() # Helps determine mouse position

        self.finishPaint()  # Paints whatever is desired from last frame on the screen



    def bugCheckerOnMousePos(self):
        textRender = self.font.render(str(self.mouseX) + ", " + str(self.mouseY), True, (255,255,255))
        textRect = textRender.get_rect(topleft = (10,10))
        self.screen.blit(textRender, textRect)