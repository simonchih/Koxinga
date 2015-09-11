import time
import pygame

background_image_filename = 'Image/Formosa-1863_1600x900.jpg'
block_image = 'Image/wood_40x27.jpg'
block2_image = 'Image/wood_27x40.jpg'
block_selected_image = 'Image/wood_selected_40x27.jpg'
block2_selected_image = 'Image/wood_selected_27x40.jpg'
coin_image = 'Image/gold_coin_14x14.gif'
treasure_image = 'Image/treasure_30x30.gif'

screen_width = 1599
screen_height = 860

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Koxinga')

background = pygame.image.load(background_image_filename).convert()
block = pygame.image.load(block_image).convert()
block2 = pygame.image.load(block2_image).convert()
block_sel = pygame.image.load(block_selected_image).convert()
block2_sel = pygame.image.load(block_selected_image).convert()
coin = pygame.image.load(coin_image).convert()
treasure = pygame.image.load(treasure_image).convert()

player1_start_w = 400
player_1_3_block_start_w = player1_start_w
player_1_6_block_start_h = screen_height - block.get_height()
player_2_block_start_w = 0
player_2_5_block_start_h = int((screen_height - 5*block2.get_height())/2)
player_3_4_block_start_h = 0
player_4_6_block_start_w = screen_width - player1_start_w - 5*block.get_width()
player_5_block_start_w = screen_width - block2.get_width()

player_image_pos = [[[0,0], [0,0], [0,0], [0,0], [0,0]], [[0,0], [0,0], [0,0], [0,0], [0,0]], [[0,0], [0,0], [0,0], [0,0], [0,0]], [[0,0], [0,0], [0,0], [0,0], [0,0]], [[0,0], [0,0], [0,0], [0,0], [0,0]], [[0,0], [0,0], [0,0], [0,0], [0,0]]]

#player is 1 base
def five_block_w(start_w, start_h, b_image, player):
    for i in range(0, 5):
        screen.blit(b_image, (start_w + i*b_image.get_width(), start_h))
        player_image_pos[player-1][i][0] = start_w + i*b_image.get_width()
        player_image_pos[player-1][i][1] = start_h

#player is 1 base        
def five_block_h(start_w, start_h, b_image, player):
    for i in range(0, 5):
        screen.blit(b_image, (start_w, start_h + i*b_image.get_height()))
        player_image_pos[player-1][i][0] = start_w
        player_image_pos[player-1][i][1] = start_h + i*b_image.get_height()

def draw_map(Surface):
    width = 2
    twidth = 1
    dark_blue = 0x0000aa
    red = 0xff0000
    big_block = 160
    margin = 60
    
    #each block width is 61
    wblock = 61
    
    #each block width is 60
    hblock = 60
    
    fs_text = "Formosa Strait"
    fs_x = 1390 
    fs_y = 70
    sc_x = margin + big_block + 8*wblock + int(wblock/2) - 12
    sc_y = margin + big_block - 23 
    
    #outer line
    pygame.draw.line(Surface, dark_blue, (margin, margin), (screen_width - margin,margin), width)
    pygame.draw.line(Surface, dark_blue, (screen_width - margin,margin), (screen_width - margin,screen_height - margin), width)
    pygame.draw.line(Surface, dark_blue, (screen_width - margin,screen_height - margin), (margin,screen_height - margin), width)
    pygame.draw.line(Surface, dark_blue, (margin,screen_height - margin), (margin,margin), width)
    
    #inner line
    pygame.draw.line(Surface, dark_blue, (margin, margin+big_block), (screen_width - margin,margin+big_block), twidth)
    pygame.draw.line(Surface, dark_blue, (screen_width - margin-big_block,margin), (screen_width - margin-big_block,screen_height - margin), twidth)
    pygame.draw.line(Surface, dark_blue, (screen_width - margin,screen_height - margin - big_block), (margin,screen_height - margin - big_block), twidth)
    pygame.draw.line(Surface, dark_blue, (margin+big_block,screen_height - margin), (margin + big_block,margin), twidth)
    
    #top left to top right
    pygame.draw.line(Surface, dark_blue, (margin, margin+int(big_block/2)), (margin+big_block+wblock*2, margin+int(big_block/2)), twidth)
    pygame.draw.line(Surface, dark_blue, (margin+int(big_block/2), margin), (margin+int(big_block/2), margin+big_block+hblock*2), twidth)
    #first half block
    pygame.draw.line(Surface, dark_blue, (margin+big_block+wblock, margin), (margin+big_block+wblock,margin+int(big_block/2)), twidth)
    for i in range(0, 17):
        if 7 == i:
            pygame.draw.line(Surface, red, (margin+big_block+(i+2)*wblock, margin), (margin+big_block+(i+2)*wblock,margin+big_block), twidth)
        else:
            pygame.draw.line(Surface, dark_blue, (margin+big_block+(i+2)*wblock, margin), (margin+big_block+(i+2)*wblock,margin+big_block), twidth)
        
    #top right to bottom right
    for i in range(0, 5):
        pygame.draw.line(Surface, dark_blue, (screen_width - margin-big_block, margin+big_block+(i+1)*hblock), (screen_width - margin,margin+big_block+(i+1)*hblock), twidth)
    #half block
    pygame.draw.line(Surface, dark_blue, (screen_width - margin-int(big_block/2), margin+big_block+6*hblock), (screen_width - margin,margin+big_block+6*hblock), twidth)    
    
    #bottom left to bottom right
    pygame.draw.line(Surface, dark_blue, (screen_width - margin-int(big_block/2), screen_height - margin), (screen_width - margin-int(big_block/2), screen_height - margin - big_block - 2*hblock), twidth)
    pygame.draw.line(Surface, dark_blue, (screen_width - margin, screen_height -margin - int(big_block/2)), (screen_width - margin - big_block - 2*wblock, screen_height -margin - int(big_block/2)), twidth)
    #half block
    pygame.draw.line(Surface, dark_blue, (margin+big_block+wblock, screen_height - margin - int(big_block/2)), (margin+big_block+wblock,screen_height - margin), twidth)
    for i in range(0, 16):
            pygame.draw.line(Surface, dark_blue, (margin+big_block+(i+2)*wblock, screen_height - margin - big_block), (margin+big_block+(i+2)*wblock,screen_height - margin), twidth)
    #half block
    pygame.draw.line(Surface, dark_blue, (margin+big_block+18*wblock, screen_height - margin - int(big_block/2)), (margin+big_block+18*wblock,screen_height - margin), twidth)
    
    #top left to button left
    pygame.draw.line(Surface, dark_blue, (margin, screen_height - margin - int(big_block/2)), (margin + big_block + 2*wblock, screen_height - margin - int(big_block/2)), twidth)
    pygame.draw.line(Surface, dark_blue, (margin + int(big_block/2), screen_height - margin), (margin + int(big_block/2), screen_height - margin - big_block - 2*hblock), twidth)
    #half block
    pygame.draw.line(Surface, dark_blue, (margin, margin + big_block + hblock), (margin + int(big_block/2), margin+big_block+hblock), twidth)
    for i in range(0, 4):
        pygame.draw.line(Surface, dark_blue, (margin, margin + big_block + (i+2)*hblock), (margin + big_block, margin+big_block+(i+2)*hblock), twidth)
    #half block
    pygame.draw.line(Surface, dark_blue, (margin, margin + big_block + 6*hblock), (margin + int(big_block/2), margin+big_block+6*hblock), twidth)
    
    #Display font "Formosa Strait"
    screen.blit(write(fs_text, (0, 0, 0), 22), (fs_x, fs_y))
    
    for sc in range(0, 12):
        if 0 == sc:
            screen.blit(write('-5', (0xff, 0, 0), 22), (sc_x, sc_y))
        elif 11 == sc:
            screen.blit(write('15', (0, 0, 0), 22), (sc_x+sc*wblock, sc_y))
        else:
            screen.blit(write(str(sc), (0, 0, 0), 22), (sc_x+sc*wblock, sc_y))

def write(msg="pygame is cool", color= (0,0,0), size = 14):
    myfont = pygame.font.Font("wqy-zenhei.ttf", size)
    mytext = myfont.render(msg, True, color)
    mytext = mytext.convert_alpha()
    return mytext 
    
def main():
    while True:
        screen.blit(background, (0,0))
        five_block_w(player_1_3_block_start_w, player_1_6_block_start_h, block, 1)
        five_block_h(player_2_block_start_w, player_2_5_block_start_h, block2, 2)
        five_block_w(player_1_3_block_start_w, player_3_4_block_start_h, block, 3)
        five_block_w(player_4_6_block_start_w, player_3_4_block_start_h, block, 4)
        five_block_h(player_5_block_start_w, player_2_5_block_start_h, block2, 5)
        five_block_w(player_4_6_block_start_w, player_1_6_block_start_h, block, 6)
        draw_map(screen)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
    pygame.quit()
    quit()

if __name__ == "__main__":
    main()