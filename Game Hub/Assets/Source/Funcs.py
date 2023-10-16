import pygame
import Main

def Render_Text(text,pos,color,font,size):
    textbase = pygame.font.SysFont(font,size)
    textTBD = textbase.render(text,1,color)
    Main.screen.blit(textTBD,pos)

def Render_Rect(pos,color,size):
    Surface = pygame.Surface(size)
    Surface.fill(color)
    Main.screen.blit(Surface,pos)