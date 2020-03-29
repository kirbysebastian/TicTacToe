import pygame

class GUI:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((400, 400))
        pygame.display.set_caption("TIC TAC TOE")

    def start(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #pygame.display.quit()
                pygame.quit()
