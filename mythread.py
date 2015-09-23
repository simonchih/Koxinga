import threading
import pygame

screen_width = 1599
screen_height = 860

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Koxinga')

player_num = 6

piece0_image = 'Image/pawn2.gif'
piece1_image = 'Image/pawn3.gif'
piece2_image = 'Image/pawn4.gif'
piece3_image = 'Image/pawn5.gif'
piece4_image = 'Image/pawn6.gif'
piece5_image = 'Image/pawn8.gif'

piece0 = pygame.image.load(piece0_image).convert()
piece1 = pygame.image.load(piece1_image).convert()
piece2 = pygame.image.load(piece2_image).convert()
piece3 = pygame.image.load(piece3_image).convert()
piece4 = pygame.image.load(piece4_image).convert()
piece5 = pygame.image.load(piece5_image).convert()

def player_id_to_image(pid):
    if 0 == pid:
        return piece0
    elif 1 == pid:
        return piece1
    elif 2 == pid:
        return piece2
    elif 3 == pid:
        return piece3
    elif 4 == pid:
        return piece4
    elif 5 == pid:
        return piece5

class myThread (threading.Thread):
    def __init__(self, threadID, surface, player_data):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.surface = surface
        self.player_data = player_data
    def run(self):
        for p in range(0, player_num):
            if 0 == self.player_data[p].mode:
                b_id = self.player_data[p].b_id
                self.surface.blit(player_id_to_image(p), self.player_data[p].loc[b_id])