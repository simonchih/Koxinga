import random
import time
import pygame
from game_map import *

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

RED = (0xff, 0, 0)
BLACK = (0, 0, 0)

item_size = 30
map_block_num = 71
inner_block_num = 3
r_start = 1
r_end = 5
rb_outer_start = 6
rb_outer_end = 12
b_start = 16
b_end = 30
lb_outer_start = 31
lb_outer_end = 37
l_start = 41
l_end = 43
lt_outer_start = 44
lt_outer_end = 50
t_start = 54
t_end = 70
player1_start_w = 400
player_1_3_block_start_w = player1_start_w
player_1_6_block_start_h = screen_height - block.get_height()
player_2_block_start_w = 0
player_2_5_block_start_h = int((screen_height - 5*block2.get_height())/2)
player_3_4_block_start_h = 0
player_4_6_block_start_w = screen_width - player1_start_w - 5*block.get_width()
player_5_block_start_w = screen_width - block2.get_width()

player_image_pos = [[[0,0], [0,0], [0,0], [0,0], [0,0]], [[0,0], [0,0], [0,0], [0,0], [0,0]], [[0,0], [0,0], [0,0], [0,0], [0,0]], [[0,0], [0,0], [0,0], [0,0], [0,0]], [[0,0], [0,0], [0,0], [0,0], [0,0]], [[0,0], [0,0], [0,0], [0,0], [0,0]]]

main_map = [0] * map_block_num
map_mark = [0] * map_block_num

def draw_item(Surface, type, value, pos):
    (x, y) = pos
    radius = 6
    width = 2
    c_left = 7
    c_middle = 15
    c_right = 22
    c_top = 7
    c_bottom = 22
    if 1 == type:
        Surface.blit(treasure, (x, y))
    elif 2 == type:
        Surface.blit(write(str(value), BLACK, 14), (x, y))
        Surface.blit(coin, (x+15, y+2))
    elif 3 == type:
        if 2 == value:
            pygame.draw.circle(Surface, BLACK, (x+c_left, y+c_middle), radius, width)
            pygame.draw.circle(Surface, BLACK, (x+c_right, y+c_middle), radius, width)
        elif 3 == value:
            pygame.draw.circle(Surface, BLACK, (x+c_middle, y+c_top), radius, width)
            pygame.draw.circle(Surface, BLACK, (x+c_left, y+c_bottom), radius, width)
            pygame.draw.circle(Surface, BLACK, (x+c_right, y+c_bottom), radius, width)
        elif 4 == value:
            pygame.draw.circle(Surface, BLACK, (x+c_left, y+c_top), radius, width)
            pygame.draw.circle(Surface, BLACK, (x+c_right, y+c_top), radius, width)
            pygame.draw.circle(Surface, BLACK, (x+c_left, y+c_bottom), radius, width)
            pygame.draw.circle(Surface, BLACK, (x+c_right, y+c_bottom), radius, width)

#player is 1 base
def five_block_w(start_w, start_h, b_image):
    for i in range(0, 5):
        screen.blit(b_image, (start_w + i*b_image.get_width(), start_h))

#player is 1 base        
def five_block_h(start_w, start_h, b_image):
    for i in range(0, 5):
        screen.blit(b_image, (start_w, start_h + i*b_image.get_height()))

def generate_five_block_w(start_w, start_h, b_image, player):
    for i in range(0, 5):
        player_image_pos[player-1][i][0] = start_w + i*b_image.get_width()
        player_image_pos[player-1][i][1] = start_h

#player is 1 base        
def generate_five_block_h(start_w, start_h, b_image, player):
    for i in range(0, 5):
        player_image_pos[player-1][i][0] = start_w
        player_image_pos[player-1][i][1] = start_h + i*b_image.get_height()        
        
def draw_map(Surface):
    global main_map

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
    sc_size = 22
    sc_num = 12    
    
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
    Surface.blit(write(fs_text, (0, 0, 0), 22), (fs_x, fs_y))
    
    for sc in range(0, sc_num):
        if 0 == sc:
            Surface.blit(write('-5', RED, sc_size), (sc_x, sc_y))
        elif 11 == sc:
            Surface.blit(write('15', BLACK, sc_size), (sc_x+sc*wblock, sc_y))
        else:
            Surface.blit(write(str(sc), BLACK, sc_size), (sc_x+sc*wblock, sc_y))
            
    for i in range(1, t_end+1):
        map_type = main_map[i].type
        map_value = main_map[i].value
        if i >= r_start and i <= r_end:
            draw_item(Surface, map_type, map_value, (screen_width - margin - int((big_block+item_size)/2), margin+big_block+int((hblock-item_size)/2)+(i-1)*hblock))
        

def write(msg="pygame is cool", color= (0,0,0), size = 14):
    myfont = pygame.font.Font("wqy-zenhei.ttf", size)
    mytext = myfont.render(msg, True, color)
    mytext = mytext.convert_alpha()
    return mytext 

def set_random_item(mark, low, high, type=0, value=0):
    global main_map
    index = random.randint(0, high - low)
    i = 0
    if low == high:
        if 0 == mark[low]:
            mark[low] = 1
            main_map[low].type = type
            main_map[low].value = value
    else:
        while index >= 0:
            v = low + (i % (high - low + 1))
            if 1 == mark[v]:
                i += 1
            elif 0 == index:
                mark[v] = 1
                main_map[v].type = type
                main_map[v].value = value
                index -= 1
            else:
                i += 1
                index -= 1
                
# formosa strait:0
# right bock:1 ~ 5
# outer block: 6 ~ 12
# inner block: 13 ~ 15

# bottom block: 16 ~ 30
# outer block: 31 ~ 37
# inner block: 38 ~ 40

# left block: 41 ~ 43
# outer block: 44 ~ 50
# inner block: 51 ~ 53

# top block: 54 ~ 70   
def generate_map(Surface):
    global main_map
    global map_mark
    
    for i in range(0, map_block_num):
        main_map[i] = game_map()
    
    # right treasure
    r = random.randint(r_start, r_end)
    main_map[r].type = 1
    map_mark[r] = 1
    
    # right bottom treasure
    set_random_item(map_mark, rb_outer_start+1, rb_outer_end-1, 1)
    set_random_item(map_mark, rb_outer_start+1, rb_outer_end-1, 1)
    
    # right
    set_random_item(map_mark, r_start, rb_outer_end+inner_block_num, 2, 3)
    set_random_item(map_mark, r_start, rb_outer_end+inner_block_num, 2, 5)
    set_random_item(map_mark, r_start, rb_outer_end+inner_block_num, 3, 4)
    set_random_item(map_mark, r_start, rb_outer_end+inner_block_num, 3, 4)
    set_random_item(map_mark, r_start, rb_outer_end+inner_block_num, 3, 3)
    set_random_item(map_mark, r_start, rb_outer_end+inner_block_num, 3, 3)
    set_random_item(map_mark, r_start, rb_outer_end+inner_block_num, 3, 3)
    set_random_item(map_mark, r_start, rb_outer_end+inner_block_num, 3, 3)
    
    # rest of right
    for i in range(r_start, b_start):
        if 0 == map_mark[i]:
            map_mark[i] = 1
            main_map[i].type = 3
            main_map[i].value = 2
    
    # bottom treasure
    set_random_item(map_mark, b_start, b_end, 1)
    
    # bottom
    set_random_item(map_mark, b_start, b_end, 2, 3)
    set_random_item(map_mark, b_start, b_end, 2, 5)
    set_random_item(map_mark, b_start, b_end, 3, 4)
    set_random_item(map_mark, b_start, b_end, 3, 4)
    set_random_item(map_mark, b_start, b_end, 3, 3)
    set_random_item(map_mark, b_start, b_end, 3, 3)
    set_random_item(map_mark, b_start, b_end, 3, 3)
    set_random_item(map_mark, b_start, b_end, 3, 3)
    
    # rest of bottom
    for i in range(b_start, lb_outer_start):
        if 0 == map_mark[i]:
            map_mark[i] = 1
            main_map[i].type = 3
            main_map[i].value = 2
    
    # left bottom treasure
    set_random_item(map_mark, lb_outer_start+1, lb_outer_end-1, 1)
    set_random_item(map_mark, lb_outer_start+1, lb_outer_end-1, 1)
    
    # left treasure
    set_random_item(map_mark, l_start, l_end, 1)
    
    # left top treasure
    set_random_item(map_mark, lt_outer_start+1, lt_outer_end-1, 1)
    set_random_item(map_mark, lt_outer_start+1, lt_outer_end-1, 1)
    
    # left
    set_random_item(map_mark, lb_outer_start, lt_outer_end+inner_block_num, 2, 3)
    set_random_item(map_mark, lb_outer_start, lt_outer_end+inner_block_num, 2, 5)
    set_random_item(map_mark, lb_outer_start, lt_outer_end+inner_block_num, 3, 4)
    set_random_item(map_mark, lb_outer_start, lt_outer_end+inner_block_num, 3, 4)
    set_random_item(map_mark, lb_outer_start, lt_outer_end+inner_block_num, 3, 4)
    set_random_item(map_mark, lb_outer_start, lt_outer_end+inner_block_num, 3, 3)
    set_random_item(map_mark, lb_outer_start, lt_outer_end+inner_block_num, 3, 3)
    set_random_item(map_mark, lb_outer_start, lt_outer_end+inner_block_num, 3, 3)
    set_random_item(map_mark, lb_outer_start, lt_outer_end+inner_block_num, 3, 3)
    set_random_item(map_mark, lb_outer_start, lt_outer_end+inner_block_num, 3, 3)
    set_random_item(map_mark, lb_outer_start, lt_outer_end+inner_block_num, 3, 3)
    
    # rest of left
    for i in range(lb_outer_start, t_start):
        if 0 == map_mark[i]:
            map_mark[i] = 1
            main_map[i].type = 3
            main_map[i].value = 2
    
    # top treasure
    set_random_item(map_mark, t_start, t_end, 1)
    
    # top
    set_random_item(map_mark, t_start, t_end, 2, 5)
    set_random_item(map_mark, t_start, t_end, 2, 7)
    set_random_item(map_mark, t_start, t_end, 3, 4)
    set_random_item(map_mark, t_start, t_end, 3, 4)
    set_random_item(map_mark, t_start, t_end, 3, 3)
    set_random_item(map_mark, t_start, t_end, 3, 3)
    set_random_item(map_mark, t_start, t_end, 3, 3)
    set_random_item(map_mark, t_start, t_end, 3, 3)
    
    # rest of top
    for i in range(t_start, t_end+1):
        if 0 == map_mark[i]:
            map_mark[i] = 1
            main_map[i].type = 3
            main_map[i].value = 2
    
def draw_dock():
    # player 1~6
    five_block_w(player_1_3_block_start_w, player_1_6_block_start_h, block)
    five_block_h(player_2_block_start_w, player_2_5_block_start_h, block2)
    five_block_w(player_1_3_block_start_w, player_3_4_block_start_h, block)
    five_block_w(player_4_6_block_start_w, player_3_4_block_start_h, block)
    five_block_h(player_5_block_start_w, player_2_5_block_start_h, block2)
    five_block_w(player_4_6_block_start_w, player_1_6_block_start_h, block)

def generate_dock():
    generate_five_block_w(player_1_3_block_start_w, player_1_6_block_start_h, block, 1)
    generate_five_block_h(player_2_block_start_w, player_2_5_block_start_h, block2, 2)
    generate_five_block_w(player_1_3_block_start_w, player_3_4_block_start_h, block, 3)
    generate_five_block_w(player_4_6_block_start_w, player_3_4_block_start_h, block, 4)
    generate_five_block_h(player_5_block_start_w, player_2_5_block_start_h, block2, 5)
    generate_five_block_w(player_4_6_block_start_w, player_1_6_block_start_h, block, 6)
    
def main():
    generate_map(screen)
    generate_dock()
    while True:
        screen.blit(background, (0,0))
        draw_dock()
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