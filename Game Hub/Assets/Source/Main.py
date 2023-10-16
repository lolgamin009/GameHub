import Vars
import Start
import pygame

def init():
    pygame.init()
    global screen
    screen = pygame.display.set_mode(Vars.windowsize)
    pygame.display.set_caption(Vars.title)
    print("Screen initialized!")

def Mainloop():
    while Vars.Running == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Vars.Running = False
        screen.fill(Vars.Windowcolor)
        Start.Render()
        pygame.display.flip()
        Vars.clock.tick(Vars.FPS)
    pygame.quit()
