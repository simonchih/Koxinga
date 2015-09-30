import random
import time
from game_map import *
from game_player import *
from mythread import *

background_image_filename = 'Image/Formosa-1863_1600x900.jpg'
block_image = 'Image/wood_40x27.jpg'
block2_image = 'Image/wood_27x40.jpg'
block_selected_image = 'Image/wood_selected_40x27.jpg'
block2_selected_image = 'Image/wood_selected_27x40.jpg'
coin_image = 'Image/gold_coin_14x14.gif'
treasure_image = 'Image/treasure_30x30.gif'
button1_image = 'Image/button1_100x50.gif'
# card
move2 = 'Image/move_move_100x50.jpg'
move_cannon = 'Image/move_cannon_100x50.jpg'
cannon_move = 'Image/cannon_move_100x50.jpg'
back_move = 'Image/back_move_100x50.jpg'
move_back = 'Image/move_back_100x50.jpg'
n1_food = 'Image/-1_food_100x50.jpg'
n2_gold = 'Image/-2_gold_100x50.jpg'
food_n2 = 'Image/food_-2_100x50.jpg'
gold_n1 = 'Image/gold_-1_100x50.jpg'
food_gold = 'Image/food_gold_100x50.jpg'

dice_1_2 = 'Image/die-1+2.gif'
dice_1_3 = 'Image/die-1+3.gif'
dice_1_4 = 'Image/die-1+4.gif'
dice_1_5 = 'Image/die-1+5.gif'
dice_2_1 = 'Image/die-2+1.gif'
dice_2_3 = 'Image/die-2+3.gif'
dice_2_4 = 'Image/die-2+4.gif'
dice_2_6 = 'Image/die-2+6.gif'
dice_3_1 = 'Image/die-3+1.gif'
dice_3_2 = 'Image/die-3+2.gif'
dice_3_5 = 'Image/die-3+5.gif'
dice_3_6 = 'Image/die-3+6.gif'
dice_4_1 = 'Image/die-4+1.gif'
dice_4_2 = 'Image/die-4+2.gif'
dice_4_5 = 'Image/die-4+5.gif'
dice_4_6 = 'Image/die-4+6.gif'
dice_5_1 = 'Image/die-5+1.gif'
dice_5_3 = 'Image/die-5+3.gif'
dice_5_4 = 'Image/die-5+4.gif'
dice_5_6 = 'Image/die-5+6.gif'
dice_6_2 = 'Image/die-6+2.gif'
dice_6_3 = 'Image/die-6+3.gif'
dice_6_4 = 'Image/die-6+4.gif'
dice_6_5 = 'Image/die-6+5.gif'

background = pygame.image.load(background_image_filename).convert()
block = pygame.image.load(block_image).convert()
block2 = pygame.image.load(block2_image).convert()
block_sel = pygame.image.load(block_selected_image).convert()
block2_sel = pygame.image.load(block_selected_image).convert()
coin = pygame.image.load(coin_image).convert()
treasure = pygame.image.load(treasure_image).convert()
button1 = pygame.image.load(button1_image).convert()

# card
mv2       = pygame.image.load(move2).convert()
mv_cannon = pygame.image.load(move_cannon).convert()
cannon_mv = pygame.image.load(cannon_move).convert()
back_mv   = pygame.image.load(back_move).convert()
mv_back   = pygame.image.load(move_back).convert()
m1_food   = pygame.image.load(n1_food).convert()
m2_gold   = pygame.image.load(n2_gold).convert()
food_m2   = pygame.image.load(food_n2).convert()
gold_m1   = pygame.image.load(gold_n1).convert()
fd_gd     = pygame.image.load(food_gold).convert()

di_1_2 = pygame.image.load(dice_1_2).convert()
di_1_3 = pygame.image.load(dice_1_3).convert()
di_1_4 = pygame.image.load(dice_1_4).convert()
di_1_5 = pygame.image.load(dice_1_5).convert()
di_2_1 = pygame.image.load(dice_2_1).convert()
di_2_3 = pygame.image.load(dice_2_3).convert()
di_2_4 = pygame.image.load(dice_2_4).convert()
di_2_6 = pygame.image.load(dice_2_6).convert()
di_3_1 = pygame.image.load(dice_3_1).convert()
di_3_2 = pygame.image.load(dice_3_2).convert()
di_3_5 = pygame.image.load(dice_3_5).convert()
di_3_6 = pygame.image.load(dice_3_6).convert()
di_4_1 = pygame.image.load(dice_4_1).convert()
di_4_2 = pygame.image.load(dice_4_2).convert()
di_4_5 = pygame.image.load(dice_4_5).convert()
di_4_6 = pygame.image.load(dice_4_6).convert()
di_5_1 = pygame.image.load(dice_5_1).convert()
di_5_3 = pygame.image.load(dice_5_3).convert()
di_5_4 = pygame.image.load(dice_5_4).convert()
di_5_6 = pygame.image.load(dice_5_6).convert()
di_6_2 = pygame.image.load(dice_6_2).convert()
di_6_3 = pygame.image.load(dice_6_3).convert()
di_6_4 = pygame.image.load(dice_6_4).convert()
di_6_5 = pygame.image.load(dice_6_5).convert()

draw_player_thread = mythread(1, screen, 0)

RED = (0xff, 0, 0)
BLACK = (0, 0, 0)
Dark_Blue = (0, 0, 0xaa)

big_block = 160
margin = 60

#each block width is 61
wblock = 61

#each block width is 60
hblock = 60

turn_id = 0
start_p = 0
inner_gap = 5
player1_start_w = 400
player_1_3_block_start_w = player1_start_w
player_1_6_block_start_h = screen_height - block.get_height()
player_2_block_start_w = 0
player_2_5_block_start_h = int((screen_height - 5*block2.get_height())/2)
player_3_4_block_start_h = 0
player_4_6_block_start_w = screen_width - player1_start_w - 5*block.get_width()
player_5_block_start_w = screen_width - block2.get_width()

dice_value1 = -1
dice_value2 = -1

player_image_pos = [[[0,0], [0,0], [0,0], [0,0], [0,0]], [[0,0], [0,0], [0,0], [0,0], [0,0]], [[0,0], [0,0], [0,0], [0,0], [0,0]], [[0,0], [0,0], [0,0], [0,0], [0,0]], [[0,0], [0,0], [0,0], [0,0], [0,0]], [[0,0], [0,0], [0,0], [0,0], [0,0]]]

main_map = [0] * map_block_num
map_mark = [0] * map_block_num
player_data = [0] * player_num

def card_id_to_image(cid):
    if 0 == cid:
        return mv2
    elif 1 == cid:
        return mv_cannon
    elif 2 == cid:
        return cannon_mv
    elif 3 == cid:
        return back_mv
    elif 4 == cid:
        return mv_back
    elif 5 == cid:
        return m1_food
    elif 6 == cid:
        return m2_gold
    elif 7 == cid:
        return food_m2
    elif 8 == cid:
        return gold_m1
    elif 9 == cid:
        return fd_gd    

# return 0 based
def pick_up_one_card(player_id):
    global player_data
    index = random.randint(1, player_data[player_id].remain_card_num)
    for i in range(0, total_card_num):
        if 0 == player_data[player_id].marked_card[i]:
            index -= 1
        if 0 == index:
           player_data[player_id].marked_card[i] = 2
           player_data[player_id].remain_card_num -= 1
           return i

def index_to_image_dice(index):
    if 0 == index:
        return di_1_2
    elif 1 == index:
        return di_1_3
    elif 2 == index:
        return di_1_4
    elif 3 == index:
        return di_1_5
    elif 4 == index:
        return di_2_1
    elif 5 == index:
        return di_2_3
    elif 6 == index:
        return di_2_4
    elif 7 == index:
        return di_2_6
    elif 8 == index:
        return di_3_1
    elif 9 == index:
        return di_3_2
    elif 10 == index:
        return di_3_5
    elif 11 == index:
        return di_3_6
    elif 12 == index:
        return di_4_1
    elif 13 == index:
        return di_4_2
    elif 14 == index:
        return di_4_5
    elif 15 == index:
        return di_4_6
    elif 16 == index:
        return di_5_1
    elif 17 == index:
        return di_5_3
    elif 18 == index:
        return di_5_4
    elif 19 == index:
        return di_5_6
    elif 20 == index:
        return di_6_2
    elif 21 == index:
        return di_6_3
    elif 22 == index:
        return di_6_4
    elif 23 == index:
        return di_6_5
    
    return None

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
        Surface.blit(write(str(value), Dark_Blue, 14), (x, y))
        Surface.blit(coin, (x+15, y+2))
    elif 3 == type:
        if 2 == value:
            pygame.draw.circle(Surface, Dark_Blue, (x+c_left, y+c_middle), radius, width)
            pygame.draw.circle(Surface, Dark_Blue, (x+c_right, y+c_middle), radius, width)
        elif 3 == value:
            pygame.draw.circle(Surface, Dark_Blue, (x+c_middle, y+c_top), radius, width)
            pygame.draw.circle(Surface, Dark_Blue, (x+c_left, y+c_bottom), radius, width)
            pygame.draw.circle(Surface, Dark_Blue, (x+c_right, y+c_bottom), radius, width)
        elif 4 == value:
            pygame.draw.circle(Surface, Dark_Blue, (x+c_left, y+c_top), radius, width)
            pygame.draw.circle(Surface, Dark_Blue, (x+c_right, y+c_top), radius, width)
            pygame.draw.circle(Surface, Dark_Blue, (x+c_left, y+c_bottom), radius, width)
            pygame.draw.circle(Surface, Dark_Blue, (x+c_right, y+c_bottom), radius, width)

def five_block_w(start_w, start_h, b_image):
    for i in range(0, 5):
        screen.blit(b_image, (start_w + i*b_image.get_width(), start_h))
      
def five_block_h(start_w, start_h, b_image):
    for i in range(0, 5):
        screen.blit(b_image, (start_w, start_h + i*b_image.get_height()))

#player is 1 base, but player_image_pos is 0 base
def generate_five_block_w(start_w, start_h, b_image, player):
    for i in range(0, 5):
        player_image_pos[player-1][i][0] = start_w + i*b_image.get_width()
        player_image_pos[player-1][i][1] = start_h

#player is 1 base, but player_image_pos is 0 base        
def generate_five_block_h(start_w, start_h, b_image, player):
    for i in range(0, 5):
        player_image_pos[player-1][i][0] = start_w
        player_image_pos[player-1][i][1] = start_h + i*b_image.get_height()        
        
def draw_map(Surface):
    global main_map

    width = 2
    twidth = 1
    
    fs_text = "Formosa Strait"
    fs_x = 1390 
    fs_y = 70
    sc_x = margin + big_block + 8*wblock + int(wblock/2) - 12
    sc_y = margin + big_block - 23
    sc_size = 22
    sc_num = 12    
 
    #outer line
    pygame.draw.line(Surface, Dark_Blue, (margin, margin), (screen_width - margin,margin), width)
    pygame.draw.line(Surface, Dark_Blue, (screen_width - margin,margin), (screen_width - margin,screen_height - margin), width)
    pygame.draw.line(Surface, Dark_Blue, (screen_width - margin,screen_height - margin), (margin,screen_height - margin), width)
    pygame.draw.line(Surface, Dark_Blue, (margin,screen_height - margin), (margin,margin), width)
    
    #inner line
    pygame.draw.line(Surface, Dark_Blue, (margin, margin+big_block), (screen_width - margin,margin+big_block), twidth)
    pygame.draw.line(Surface, Dark_Blue, (screen_width - margin-big_block,margin), (screen_width - margin-big_block,screen_height - margin), twidth)
    pygame.draw.line(Surface, Dark_Blue, (screen_width - margin,screen_height - margin - big_block), (margin,screen_height - margin - big_block), twidth)
    pygame.draw.line(Surface, Dark_Blue, (margin+big_block,screen_height - margin), (margin + big_block,margin), twidth)
    
    #top left to top right
    pygame.draw.line(Surface, Dark_Blue, (margin, margin+int(big_block/2)), (margin+big_block+wblock*2, margin+int(big_block/2)), twidth)
    pygame.draw.line(Surface, Dark_Blue, (margin+int(big_block/2), margin), (margin+int(big_block/2), margin+big_block+hblock*2), twidth)
    #first half block
    pygame.draw.line(Surface, Dark_Blue, (margin+big_block+wblock, margin), (margin+big_block+wblock,margin+int(big_block/2)), twidth)
    for i in range(0, 17):
        if 7 == i:
            pygame.draw.line(Surface, RED, (margin+big_block+(i+2)*wblock, margin), (margin+big_block+(i+2)*wblock,margin+big_block), twidth)
        else:
            pygame.draw.line(Surface, Dark_Blue, (margin+big_block+(i+2)*wblock, margin), (margin+big_block+(i+2)*wblock,margin+big_block), twidth)
        
    #top right to bottom right
    for i in range(0, 5):
        pygame.draw.line(Surface, Dark_Blue, (screen_width - margin-big_block, margin+big_block+(i+1)*hblock), (screen_width - margin,margin+big_block+(i+1)*hblock), twidth)
    #half block
    pygame.draw.line(Surface, Dark_Blue, (screen_width - margin-int(big_block/2), margin+big_block+6*hblock), (screen_width - margin,margin+big_block+6*hblock), twidth)    
    
    #bottom left to bottom right
    pygame.draw.line(Surface, Dark_Blue, (screen_width - margin-int(big_block/2), screen_height - margin), (screen_width - margin-int(big_block/2), screen_height - margin - big_block - 2*hblock), twidth)
    pygame.draw.line(Surface, Dark_Blue, (screen_width - margin, screen_height -margin - int(big_block/2)), (screen_width - margin - big_block - 2*wblock, screen_height -margin - int(big_block/2)), twidth)
    #half block
    pygame.draw.line(Surface, Dark_Blue, (margin+big_block+wblock, screen_height - margin - int(big_block/2)), (margin+big_block+wblock,screen_height - margin), twidth)
    for i in range(0, 16):
            pygame.draw.line(Surface, Dark_Blue, (margin+big_block+(i+2)*wblock, screen_height - margin - big_block), (margin+big_block+(i+2)*wblock,screen_height - margin), twidth)
    #half block
    pygame.draw.line(Surface, Dark_Blue, (margin+big_block+18*wblock, screen_height - margin - int(big_block/2)), (margin+big_block+18*wblock,screen_height - margin), twidth)
    
    #top left to button left
    pygame.draw.line(Surface, Dark_Blue, (margin, screen_height - margin - int(big_block/2)), (margin + big_block + 2*wblock, screen_height - margin - int(big_block/2)), twidth)
    pygame.draw.line(Surface, Dark_Blue, (margin + int(big_block/2), screen_height - margin), (margin + int(big_block/2), screen_height - margin - big_block - 2*hblock), twidth)
    #half block
    pygame.draw.line(Surface, Dark_Blue, (margin, margin + big_block + hblock), (margin + int(big_block/2), margin+big_block+hblock), twidth)
    for i in range(0, 4):
        pygame.draw.line(Surface, Dark_Blue, (margin, margin + big_block + (i+2)*hblock), (margin + big_block, margin+big_block+(i+2)*hblock), twidth)
    #half block
    pygame.draw.line(Surface, Dark_Blue, (margin, margin + big_block + 6*hblock), (margin + int(big_block/2), margin+big_block+6*hblock), twidth)
    
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
        map_loc = main_map[i].loc
        if map_type != 0:
            draw_item(Surface, map_type, map_value, map_loc)
            
    # Test pieces only
    #for p in range(0, player_num):
    #    for i in range(0, map_block_num):
    #        Surface.blit(player_id_to_image(p), player_data[p].loc[i]) 
    # End test pieces        

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

#player is 0 base                
def map_loc_to_player_loc(map_loc, block_id, player):
    gap = 5
    (x, y) = map_loc
    
    # right and left on the map
    # minimum width is 80
    # minimum height is 60
    # (x, y) = (25, 15)
    if (block_id >=0 and block_id <= rb_outer_start+4) or (block_id >= rb_outer_end+1 and block_id <= rb_outer_end+2) or (block_id >= lb_outer_start+4 and block_id <= l_end+4) or (block_id >= lb_outer_end+2 and block_id <= lb_outer_end+3) or (block_id >= lt_outer_end+1 and block_id <= lt_outer_end+2):
        if 0 == player:
            #(5, 5)
            return (x-piece0.get_height(), y-int(piece0.get_height()/2))
        elif 1 == player:
            #(30, 5)
            return (x+gap, y-int(piece0.get_height()/2))
        elif 2 == player:
            #(55, 5)
            return (x+2*gap+piece0.get_height(), y-int(piece0.get_height()/2))
        elif 3 == player:
            #(5, 30)
            return (x-piece0.get_height(), y+int(piece0.get_height()/2)+gap)
        elif 4 == player:
            #(30, 30)
            return (x+gap, y+int(piece0.get_height()/2)+gap)
        elif 5 == player:
            #(55, 30)
            return (x+2*gap+piece0.get_height(), y+int(piece0.get_height()/2)+gap)
        
    # top and bottom on the map
    # minimum width is 61
    # minimum height is 80
    # (x, y) = (15, 25)
    else:
        if 0 == player:
            #(5, 5)
            return (x-int(piece0.get_height()/2),y-piece0.get_height())
        elif 1 == player:
            #(5, 30)
            return (x-int(piece0.get_height()/2),y+gap)
        elif 2 == player:
            #(5, 55)
            return (x-int(piece0.get_height()/2),y+2*gap+piece0.get_height())
        elif 3 == player:
            #(30, 5)
            return (x+int(piece0.get_height()/2)+gap,y-piece0.get_height())
        elif 4 == player:
            #(30, 30)
            return (x+int(piece0.get_height()/2)+gap,y+gap)
        elif 5 == player:
            #(30, 55)
            return (x+int(piece0.get_height()/2)+gap,y+2*gap+piece0.get_height())
                
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
def generate_map():
    global main_map
    global map_mark
    
    block_loc = [0] * map_block_num
    
    #ini main_map
    for i in range(0, map_block_num):
        main_map[i] = game_map()
        
    #ini player_data
    for i in range(0, player_num):
        player_data[i] = game_player()
    
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
            
    for i in range(0, t_end+1):
        map_type = main_map[i].type
        map_value = main_map[i].value
        if 0 == i:
            main_map[i].loc = (screen_width - margin - int((big_block+item_size)/2), margin + int(big_block-item_size)/2)
        elif i >= r_start and i <= r_end:
            main_map[i].loc = (screen_width - margin - int((big_block+item_size)/2), margin+big_block+int((hblock-item_size)/2)+(i-1)*hblock)
        elif i >= rb_outer_start and i <= rb_outer_start+1:
            main_map[i].loc = (screen_width - margin - int(big_block/4) - int(item_size/2), margin+big_block+int((hblock-item_size)/2)+(i-1)*hblock)
        elif i >= rb_outer_start+2 and i <= rb_outer_start+3:
            main_map[i].loc = (screen_width - margin - int(big_block/4) - int(item_size/2), screen_height-margin-big_block+int((int(big_block/2)-item_size)/2)+(i-(rb_outer_start+2))*int(big_block/2))
        elif i == rb_outer_start+4:
            main_map[i].loc = (screen_width - margin - int(big_block/4) - int(item_size/2) - int(big_block/2), screen_height-margin-big_block+int((int(big_block/2)-item_size)/2)+int(big_block/2))
        elif i >= rb_outer_start+5 and i <= rb_outer_end:
            main_map[i].loc = (screen_width - margin - big_block - (i-(rb_outer_start+4))*wblock + int((wblock-item_size)/2), screen_height-margin-big_block+int((int(big_block/2)-item_size)/2)+int(big_block/2))
        elif i == rb_outer_end+1:
            main_map[i].loc = (screen_width-margin-int(big_block/2)-int(big_block/4)-int(item_size/2), screen_height-margin-big_block-hblock-int(item_size/2))
        elif i == rb_outer_end+2:
            main_map[i].loc = (screen_width-margin-int(big_block/2)-int(big_block/4)-int(item_size/2), screen_height-margin-int(big_block/2)-int(big_block/4)-int(item_size/2))
        elif i == rb_outer_end+3:
            main_map[i].loc = (screen_width-margin-big_block-wblock-int(item_size/2), screen_height-margin-int(big_block/2)-int(big_block/4)-int(item_size/2))
        elif i >= b_start and i <= b_end:
            main_map[i].loc = (screen_width - margin -big_block -((i-b_start+2)*wblock)- int((wblock+item_size)/2), screen_height-margin-int((big_block+item_size)/2))
        elif i >= lb_outer_start and i <= lb_outer_start+1:
            main_map[i].loc = (screen_width - margin -big_block -((i-b_start+2)*wblock)- int((wblock+item_size)/2), screen_height-margin-int(big_block/4)-int(item_size/2))
        elif i == lb_outer_start+2:
            main_map[i].loc = (margin+int(big_block/2)+int(big_block/4)-int(item_size/2), screen_height-margin-int(big_block/4)-int(item_size/2))
        elif i >= lb_outer_start+3 and i <= lb_outer_start+4:
            main_map[i].loc = (margin+int(big_block/4)-int(item_size/2), screen_height-margin-int(big_block/4)-int(item_size/2)-((i-(lb_outer_start+3))*int(big_block/2)))
        elif i >= lb_outer_start+5 and i <= lb_outer_end:
            main_map[i].loc = (margin+int(big_block/4)-int(item_size/2), screen_height-margin-big_block-((i-(lb_outer_start+5))*hblock)-int(hblock/2)-int(item_size/2))
        elif i == lb_outer_end+1:
            main_map[i].loc = (margin+big_block+wblock-int(item_size/2), screen_height-margin-int(big_block/2)-int(big_block/4)-int(item_size/2))
        elif i == lb_outer_end+2:
            main_map[i].loc = (margin+int(big_block/2)+int(big_block/4)-int(item_size/2), screen_height-margin-int(big_block/2)-int(big_block/4)-int(item_size/2))
        elif i == lb_outer_end+3:
            main_map[i].loc = (margin+int(big_block/2)+int(big_block/4)-int(item_size/2), screen_height-margin-big_block-hblock-int(item_size/2))
        elif i >= l_start and i <= l_end:
            main_map[i].loc = (margin+int(big_block/2)-int(item_size/2), screen_height-margin-big_block-((i-l_start+2)*hblock)-int(hblock/2)-int(item_size/2))
        elif i >= lt_outer_start and i <= lt_outer_start+1:
            main_map[i].loc = (margin+int(big_block/4)-int(item_size/2), screen_height-margin-big_block-((i-l_start+2)*hblock)-int(hblock/2)-int(item_size/2))
        elif i == lt_outer_start+2:
            main_map[i].loc = (margin+int(big_block/4)-int(item_size/2), margin+int(big_block/2)+int(big_block/4)-int(item_size/2))
        elif i >= lt_outer_start+3 and i <= lt_outer_start+4:
            main_map[i].loc = (margin+int(big_block/4)-int(item_size/2)+((i-(lt_outer_start+3))*int(big_block/2)), margin+int(big_block/4)-int(item_size/2))
        elif i >= lt_outer_start+5 and i <= lt_outer_end:
            main_map[i].loc = (margin+big_block+int(wblock/2)-int(item_size/2)+((i-(lt_outer_start+5))*wblock), margin+int(big_block/4)-int(item_size/2))
        elif i == lt_outer_end+1:
            main_map[i].loc = (margin+int(big_block/2)+int(big_block/4)-int(item_size/2), margin+big_block+hblock-int(item_size/2))
        elif i == lt_outer_end+2:
            main_map[i].loc = (margin+int(big_block/2)+int(big_block/4)-int(item_size/2), margin+int(big_block/2)+int(big_block/4)-int(item_size/2))
        elif i == lt_outer_end+3:
            main_map[i].loc = (margin+big_block+wblock-int(item_size/2), margin+int(big_block/2)+int(big_block/4)-int(item_size/2))
        elif i >= t_start and i <= t_end:
            main_map[i].loc = (margin+big_block+((i-t_start+2)*wblock)+int(wblock/2)-int(item_size/2), margin+int(big_block/2)-int(item_size/2))
    
    # player 0 is human
    player_data[0].IsAI = 0
    
    for p in range(0, player_num):
        for i in range(0, map_block_num):
            block_loc[i] = map_loc_to_player_loc(main_map[i].loc, i, p)
        player_data[p].loc = block_loc[:]
        (player_data[p].x, player_data[p].y) = player_data[p].loc[0]
        player_data[p].b_id = 0
        player_data[p].next_id = 0
        
    draw_player_thread.player_data = player_data

def generate_player_card():
    global player_data
    
    for i in range(0, player_num):
        pick_up_one_card(i)
        pick_up_one_card(i)
        pick_up_one_card(i)
    
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

def draw_button(Surface, loc, str, color, size = 14, image = button1):
    (mouseX, mouseY) = pygame.mouse.get_pos()
    fontx = loc[0]+ 50 - int(len(str)/2*6)
    fonty = loc[1]+15
    Surface.blit(image, loc)
    if loc[0] <= mouseX <= loc[0]+image.get_width() and loc[1] <= mouseY <= loc[1]+image.get_height():
        Surface.blit(write(str, RED, size), (fontx, fonty))
    else:
        Surface.blit(write(str, color, size), (fontx, fonty))
    
    
def draw_inner_item(Surface):
    global dice_value1, dice_value2, turn_id, inner_gap
    
    rect_width = 2
    #TEST only
    #dice_value1 = 1
    #dice_value2 = 2
    #END TEST
    
    index1 = index_to_image_dice(dice_value1)
    index2 = index_to_image_dice(dice_value2)
    
    card_x =  margin+big_block+inner_gap
    card_y =  margin+big_block+inner_gap+di_1_2.get_height()+button1.get_height()+inner_gap
    
    if None != index1:
        Surface.blit(index1, (margin+big_block+inner_gap, margin+big_block+inner_gap))
    if None != index2:
        Surface.blit(index2, (margin+big_block+inner_gap+di_1_2.get_width()+inner_gap, margin+big_block+inner_gap))

    if 0 == player_data[turn_id].IsAI:
        if 3 == player_data[turn_id].mode:
            draw_button(Surface, (margin+big_block+inner_gap, margin+big_block+inner_gap+di_1_2.get_height()), "Roll", BLACK)
        elif 4 == player_data[turn_id].mode:
            draw_button(Surface, (margin+big_block+inner_gap, margin+big_block+inner_gap+di_1_2.get_height()), "Swap", BLACK)
            for i in range(0, total_card_num):
                if 2 == player_data[turn_id].marked_card[i]:
                    Surface.blit(card_id_to_image(i), (card_x, card_y))
                    (MouseX, MouseY) = pygame.mouse.get_pos()
                    if card_x <= MouseX <= card_x + mv2.get_width() and card_y <= MouseY <= card_y + mv2.get_height():
                        pygame.draw.rect(Surface, RED, (card_x, card_y, mv2.get_width(), mv2.get_height()), rect_width)
                    card_y += mv2.get_height() + inner_gap
        
            
    
def main():
    global draw_player_thread, player_data, dice_value1, dice_value2
    
    generate_map()
    generate_dock()
    generate_player_card()
    draw_player_thread.start()
    # test p backward
    #pd = draw_player_thread.player_data
    #(pd[1].x, pd[1].y) = pd[1].loc[70]
    #pd[1].b_id = 70
    #pd[1].next_id = 70
    # end test p
    while True:
        screen.blit(background, (0,0))
        draw_dock()
        draw_map(screen)
        draw_inner_item(screen)
        draw_player_thread.run()
        pygame.display.update()
        if 0 == player_data[turn_id].IsAI:
            if start_p == turn_id and 0 == player_data[turn_id].mode:
                player_data[turn_id].mode = 3        
        # test p
        #pd = draw_player_thread.player_data
        #if 0 == pd[1].mode and 0 == pd[1].goal_game:
        #    pd[1].step = 1
        #    pd[1].mode = 1
        #    pd[1].dir = 1
        #    pd[1].forward = 1
        # end test p
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif 3 == player_data[turn_id].mode and event.type == pygame.MOUSEBUTTONDOWN:
                (mouseX, mouseY) = pygame.mouse.get_pos()
                (x, y) = (margin+big_block+inner_gap, margin+big_block+inner_gap+di_1_2.get_height())
                if x <= mouseX <= x+button1.get_width() and y <= mouseY <= y+button1.get_height():
                    dice1 = random.randint(0, 23)
                    dice2 = random.randint(0, 23)
                    dice_value1 = dice1
                    dice_value2 = dice2
                    player_data[turn_id].mode = 4
            elif 4 == player_data[turn_id].mode and event.type == pygame.MOUSEBUTTONDOWN:
                (mouseX, mouseY) = pygame.mouse.get_pos()
                (x, y) = (margin+big_block+inner_gap, margin+big_block+inner_gap+di_1_2.get_height())
                if x <= mouseX <= x+button1.get_width() and y <= mouseY <= y+button1.get_height():
                    (dice_value1, dice_value2) = (dice_value2, dice_value1)
            
    pygame.quit()
    quit()

if __name__ == "__main__":
    main()