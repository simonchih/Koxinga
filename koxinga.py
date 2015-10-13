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
small_own_treasure_image = 'Image/treasure_25x25.gif'
own_treasure_image = 'Image/treasure_50x50.gif'
button1_image = 'Image/button1_100x50.gif'

# resource
food_image = 'Image/food_25x25.jpg'
gold_image = 'Image/gold_25x25.jpg'
cannon_image = 'Image/cannon_25x25.gif'


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
gold_food = 'Image/gold_food_100x50.jpg'
cannon_cannon = 'Image/cannon_cannon_100x50.jpg'
back_card0 = 'Image/back0.gif'
back_card1 = 'Image/back1.gif'
back_card2 = 'Image/back2.gif'
back_card3 = 'Image/back3.gif'
back_card4 = 'Image/back4.gif'
back_card5 = 'Image/back5.gif'

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
treasure_s = pygame.image.load(small_own_treasure_image).convert()
treasure_b = pygame.image.load(own_treasure_image).convert()
button1 = pygame.image.load(button1_image).convert()

# resource
food = pygame.image.load(food_image).convert()
gold = pygame.image.load(gold_image).convert()
cannon = pygame.image.load(cannon_image).convert()

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
gd_fd     = pygame.image.load(gold_food).convert()
ca_ca     = pygame.image.load(cannon_cannon).convert()
back0     = pygame.image.load(back_card0).convert()
back1     = pygame.image.load(back_card1).convert()
back2     = pygame.image.load(back_card2).convert()
back3     = pygame.image.load(back_card3).convert()
back4     = pygame.image.load(back_card4).convert()
back5     = pygame.image.load(back_card5).convert()

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
GREEN1 = (15, 96, 25)

turn_id = 0
start_p = 0
inner_gap = 5
player1_start_w = 400
player_1_3_block_start_w = player1_start_w
player_1_6_block_start_h = screen_height - block.get_height()
player_2_block_start_w = 0
player_2_5_block_start_h = int((screen_height - dock_num*block2.get_height())/2)
player_3_4_block_start_h = 0
player_4_6_block_start_w = screen_width - player1_start_w - dock_num*block.get_width()
player_5_block_start_w = screen_width - block2.get_width()

dice_value1 = -1
dice_value2 = -1

player_image_pos = [[[0,0], [0,0], [0,0], [0,0], [0,0]], [[0,0], [0,0], [0,0], [0,0], [0,0]], [[0,0], [0,0], [0,0], [0,0], [0,0]], [[0,0], [0,0], [0,0], [0,0], [0,0]], [[0,0], [0,0], [0,0], [0,0], [0,0]], [[0,0], [0,0], [0,0], [0,0], [0,0]]]

main_map = [0] * map_block_num
map_mark = [0] * map_block_num
player_data = [0] * player_num
treasure_card = [0] * treasure_num

def turn_id_to_image(tid):
    if 0 == tid:
        return back0
    elif 1 == tid:
        return back1
    elif 2 == tid:
        return back2
    elif 3 == tid:
        return back3
    elif 4 == tid:
        return back4
    elif 5 == tid:
        return back5
    

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
    elif 10 == cid:
        return gd_fd
    elif 11 == cid:
        return ca_ca
      
# return 0 based
def pick_up_one_card(player_id):
    global player_data
    
    if 0 == player_data[player_id].remain_card_num:
        for i in range(0, total_card_num):
            if 1 == player_data[player_id].marked_card[i]:
                player_data[player_id].remain_card_num += 1
                player_data[player_id].marked_card[i] = 0
                
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

def five_block_item_w(start_w, start_h, p_id):
    item_gap = 1
    font_size = 22
    #player 3, 4
    if 2 == p_id or 3 == p_id:
        font_gap_x = 0
        font_gap_y = block.get_height()+1
    #player 1, 6
    else:
        font_gap_x = 0
        font_gap_y = 0-block.get_height()-1
    
    for i in range(0, dock_num):
        b_image = dock_type_id_to_image(player_data[p_id].dtype[i])
        if None != b_image:
            value = player_data[p_id].dvalue[i]
            x = start_w + int((block.get_width()-b_image.get_width())/2) + i*block.get_width()
            y = start_h
            screen.blit(b_image, (x+item_gap, y+item_gap))
            screen.blit(write(str(value)+"x", RED, font_size), (x+font_gap_x, y+font_gap_y))
      
def five_block_item_h(start_w, start_h, p_id):
    item_gap = 1
    font_size = 22
    #player 2
    if 1 == p_id:
        font_gap_x = block2.get_width()+1
        font_gap_y = 0
    #player 5
    else:
        font_gap_x = 0-block2.get_width()-1
        font_gap_y = 0
    for i in range(0, dock_num):
        b_image = dock_type_id_to_image(player_data[p_id].dtype[i])
        if None != b_image:
            value = player_data[p_id].dvalue[i]
            x = start_w
            y = start_h + int((block2.get_height()-b_image.get_height())/2) + i*block2.get_height()
            screen.blit(b_image, (x+item_gap, y+item_gap))
            screen.blit(write(str(value)+"x", RED, font_size), (x+font_gap_x, y+font_gap_y))

def num_of_treasure_own(t_id):
    global treasure_num
    sum = 0
    for i in range(2, treasure_num):
        if 1 == player_data[t_id].treasure[i]:
            sum += 1
    return sum
    
def draw_treasure_w(start_w, start_h, bk_image, t_image, t_id):
    font_size = 22
    #player 3, 4
    if 2 == t_id or 3 == t_id:
        font_gap_x = 0
        font_gap_y = bk_image.get_height()+1
    #player 1, 6
    else:
        font_gap_x = 0
        font_gap_y = 0-bk_image.get_height()-1
        
    w = start_w + dock_num*bk_image.get_width() + inner_gap + 1
    h = start_h + 1
    sum_t = num_of_treasure_own(t_id)
    
    if 0 != sum_t:
        screen.blit(t_image, (w, h))
        screen.blit(write(str(sum_t)+"x", RED, font_size), (w+font_gap_x, h+font_gap_y))

def draw_treasure_h(start_w, start_h, bk_image, t_image, t_id):
    font_size = 22
    #player 2
    if 1 == t_id:
        font_gap_x = bk_image.get_width()+1
        font_gap_y = 0
    #player 5
    else:
        font_gap_x = 0-bk_image.get_width()-1
        font_gap_y = 0
        
    w = start_w + 1
    h = start_h + dock_num*bk_image.get_height() + inner_gap + 1
    sum_t = num_of_treasure_own(t_id)
    
    if 0 != sum_t:
        screen.blit(t_image, (w, h))
        screen.blit(write(str(sum_t)+"x", RED, font_size), (w+font_gap_x, h+font_gap_y))
    
def five_block_w(start_w, start_h, b_image):
    for i in range(0, dock_num):
        screen.blit(b_image, (start_w + i*b_image.get_width(), start_h))
      
def five_block_h(start_w, start_h, b_image):
    for i in range(0, dock_num):
        screen.blit(b_image, (start_w, start_h + i*b_image.get_height()))

#player is 1 base, but player_image_pos is 0 base
def generate_five_block_w(start_w, start_h, b_image, player):
    for i in range(0, dock_num):
        player_image_pos[player-1][i][0] = start_w + i*b_image.get_width()
        player_image_pos[player-1][i][1] = start_h

#player is 1 base, but player_image_pos is 0 base        
def generate_five_block_h(start_w, start_h, b_image, player):
    for i in range(0, dock_num):
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

def dock_type_id_to_image(type_id):
    if 1 == type_id:
        return food
    elif 2 == type_id:
        return gold
    elif 3 == type_id:
        return cannon
        
def draw_dock():
    # player 1~6
    five_block_w(player_1_3_block_start_w, player_1_6_block_start_h, block)
    five_block_h(player_2_block_start_w, player_2_5_block_start_h, block2)
    five_block_w(player_1_3_block_start_w, player_3_4_block_start_h, block)
    five_block_w(player_4_6_block_start_w, player_3_4_block_start_h, block)
    five_block_h(player_5_block_start_w, player_2_5_block_start_h, block2)
    five_block_w(player_4_6_block_start_w, player_1_6_block_start_h, block)
    
    # draw_dock_item:
    # player 1~6
    five_block_item_w(player_1_3_block_start_w, player_1_6_block_start_h, 0)
    five_block_item_h(player_2_block_start_w, player_2_5_block_start_h, 1)
    five_block_item_w(player_1_3_block_start_w, player_3_4_block_start_h, 2)
    five_block_item_w(player_4_6_block_start_w, player_3_4_block_start_h, 3)
    five_block_item_h(player_5_block_start_w, player_2_5_block_start_h, 4)
    five_block_item_w(player_4_6_block_start_w, player_1_6_block_start_h, 5)
    
    # draw treasure for player 1~6
    draw_treasure_w(player_1_3_block_start_w, player_1_6_block_start_h, block, treasure_s, 0)
    draw_treasure_h(player_2_block_start_w, player_2_5_block_start_h, block2, treasure_s, 1)
    draw_treasure_w(player_1_3_block_start_w, player_3_4_block_start_h, block, treasure_s, 2)
    draw_treasure_w(player_4_6_block_start_w, player_3_4_block_start_h, block, treasure_s, 3)
    draw_treasure_h(player_5_block_start_w, player_2_5_block_start_h, block2, treasure_s, 4)
    draw_treasure_w(player_4_6_block_start_w, player_1_6_block_start_h, block, treasure_s, 5)
    
def generate_dock():
    global player_data 
    generate_five_block_w(player_1_3_block_start_w, player_1_6_block_start_h, block, 1)
    generate_five_block_h(player_2_block_start_w, player_2_5_block_start_h, block2, 2)
    generate_five_block_w(player_1_3_block_start_w, player_3_4_block_start_h, block, 3)
    generate_five_block_w(player_4_6_block_start_w, player_3_4_block_start_h, block, 4)
    generate_five_block_h(player_5_block_start_w, player_2_5_block_start_h, block2, 5)
    generate_five_block_w(player_4_6_block_start_w, player_1_6_block_start_h, block, 6)
    for i in range(0, player_num):
        player_data[i].dtype[0] = 1
        player_data[i].dvalue[0] = 3
        player_data[i].dtype[1] = 2
        player_data[i].dvalue[1] = 3    

def draw_button(Surface, loc, str, color, size = 14, image = button1):
    (mouseX, mouseY) = pygame.mouse.get_pos()
    fontx = loc[0]+ 50 - int(len(str)/2*6)
    fonty = loc[1]+15
    Surface.blit(image, loc)
    if loc[0] <= mouseX <= loc[0]+image.get_width() and loc[1] <= mouseY <= loc[1]+image.get_height():
        Surface.blit(write(str, RED, size), (fontx, fonty))
    else:
        Surface.blit(write(str, color, size), (fontx, fonty))
    
def draw_show_card(p_id, showc=1):    
    gap = 20
    if 1 == showc: # show card
        show_card_image = card_id_to_image(player_data[p_id].selected_card_value)
    else: #show back
        show_card_image = turn_id_to_image(p_id)
        
    if 1 == p_id or 4 == p_id:
        show_card_image = pygame.transform.rotate(show_card_image, 270)
    
    if 0 == p_id:
        (start_w, start_h) = (player_1_3_block_start_w-gap-show_card_image.get_width(), screen_height - show_card_image.get_height())
    elif 1 == p_id:
        (start_w, start_h) = (player_2_block_start_w, player_2_5_block_start_h-gap-show_card_image.get_height())
    elif 2 == p_id:
        (start_w, start_h) = (player_1_3_block_start_w-gap-show_card_image.get_width(), player_3_4_block_start_h)
    elif 3 == p_id:
        (start_w, start_h) = (player_4_6_block_start_w-gap-show_card_image.get_width(), player_3_4_block_start_h)
    elif 4 == p_id:
        (start_w, start_h) = (screen_width - show_card_image.get_width(), player_2_5_block_start_h-gap-show_card_image.get_height())
    elif 5 == p_id:
        (start_w, start_h) = (player_4_6_block_start_w-gap-show_card_image.get_width(), screen_height - show_card_image.get_height())
    
    screen.blit(show_card_image, (start_w, start_h))

def draw_selected_card(t_id, start, mode=6):
    global player_num
    
    back = 0
    
    if 0 == mode:
        return
    
    showc = 1
    
    if 5 == mode:
        showc = 0
    
    for i in range(0, player_num):
        s = (start+i)%player_num
        if 1 == back and 5 != mode:
            # draw back card
            draw_show_card(s, 0)
            continue
        draw_show_card(s, showc)
        if s == t_id:
            back = 1
    
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
            if None != player_data[turn_id].selected_card_value:
                draw_button(Surface, (card_x, card_y), "Finish", BLACK)
                # draw player0 show card
                draw_show_card(turn_id)
        elif 5 == player_data[turn_id].mode:
            for i in range(0, total_card_num):
                if 2 == player_data[turn_id].marked_card[i]:
                    Surface.blit(card_id_to_image(i), (card_x, card_y))
                    (MouseX, MouseY) = pygame.mouse.get_pos()
                    if card_x <= MouseX <= card_x + mv2.get_width() and card_y <= MouseY <= card_y + mv2.get_height():
                        pygame.draw.rect(Surface, RED, (card_x, card_y, mv2.get_width(), mv2.get_height()), rect_width)
                    card_y += mv2.get_height() + inner_gap
            if None != player_data[turn_id].selected_card_value:
                draw_button(Surface, (card_x, card_y), "Finish", BLACK)
                # draw player0 show card
                draw_show_card(turn_id)

# return 0 for OK, and 1 is NOT enough(fail)                
def spend_dock_resource(type, value):
    global player_data
    #type 1:food, 2:gold
    
    spent_value_total = 0
    
    # dvalue, index is 0 base
    dvalue = [0] * dock_num
    for i in range(0, dock_num):
        dvalue[i] = (i, player_data[turn_id].dvalue[i])
        
    sorted_value = sorted(dvalue, key=lambda l:l[1])
    
    # handle spend
    for i in range(0, dock_num):
        sv = sorted_value[i]
        if type == player_data[turn_id].dtype[sv[0]] and sv[1] > 0:
            if sv[1] >= (value - spent_value_total):
                player_data[turn_id].dvalue[sv[0]] -= (value - spent_value_total) 
                if 0 == player_data[turn_id].dvalue[sv[0]]:
                    player_data[turn_id].dtype[sv[0]] = 0
                # spent_value_total = value
                return 0
            else:
                spent_value_total += player_data[turn_id].dvalue[sv[0]]
                player_data[turn_id].dvalue[sv[0]] = 0
                player_data[turn_id].dtype[sv[0]] = 0
            
    return 1

def get_dock_resource(type, value):
    global player_data
    
    # dvalue, index is 0 base
    dvalue = [0] * dock_num
    
    for i in range(0, dock_num):
        if 0 == player_data[turn_id].dtype[i]:
            player_data[turn_id].dtype[i] = type
            player_data[turn_id].dvalue[i] = value
            # dock NOT full
            return
        dvalue[i] = (i, player_data[turn_id].dvalue[i])
    
    # dock full
    sorted_value = sorted(dvalue, key=lambda l:l[1])
    
    for i in range(0, dock_num):
        sv = sorted_value[i]
        if type != player_data[turn_id].dtype[sv[0]]:
            player_data[turn_id].dtype[sv[0]] = type
            player_data[turn_id].dvalue[sv[0]] = value
            return
    
    # added fail

# steps is positive only, but fwd = 0 for back    
def prepare_move(steps, dir, fwd=1):
    global player_data, turn_id, draw_player_thread
    player_data[turn_id].step = steps
    player_data[turn_id].mode = 1
    player_data[turn_id].forward = fwd
    player_data[turn_id].dir[draw_player_thread.is_night] = dir

def resource_dest(dest, res, food, gold):
    global main_map
    
    r_sum = res
    total_food = food
    total_gold = gold
    
    if None == dest:
        # -1 for fail
        return -1, -1, -1
    
    if 1 == main_map[dest].type:
        #treasure
        r_sum += 7
    elif 2 == main_map[dest].type:
        r_sum -= main_map[dest].value
        total_gold -= main_map[dest].value
    elif 3 == main_map[dest].type:
        r_sum -= main_map[dest].value
        total_food -= main_map[dest].value
    
    return r_sum, total_food, total_gold
    
def handle_step(night, dir):
    type, dice_point, forward = card_action(night, player_data[turn_id].selected_card_value)
    if 0 != dice_point:
        if 0 == type:
            prepare_move(dice_point, dir, forward)
        else:
            get_dock_resource(type, dice_point)

# return type(0:move, 1:food, 2:gold, 3:cannon), dice_val(0~6), forward (1:forward, 0:back, None)
def card_action(night, s_card):
    global player_data, turn_id, dice_value1, dice_value2
    # dice_val 1~6
    dice_val = int(dice_value1/4)+1
    sid = s_card
    if 0 == night:
        if 0 == sid:
            return 0, dice_val, 1
        elif 1 == sid:
            return 0, dice_val, 1
        elif 2 == sid:
            #get cannon
            return 3, dice_val, None
        elif 3 == sid:
            return 0, dice_val, 0
        elif 4 == sid:
            return 0, dice_val, 1
        elif 5 == sid:
            return 0, dice_val-1, 1
        elif 6 == sid:
            if dice_val - 2 >= 0:
                return 0, dice_val-2, 1
            elif dice_val - 2 < 0:
                return 0, abs(dice_val-2), 0
        elif 7 == sid:
            #get food
            return  1, dice_val, None
        elif 8 == sid:
            #get gold
            return  2, dice_val, None
        elif 9 == sid:
            #get food
            return  1, dice_val, None
        elif 10 == sid:
            #get gold
            return 2, dice_val, None
        elif 11 == sid:
            #get cannon
            return 3, dice_val, None
    else: # 1 == night
        dice_val = int(dice_value2/4)+1
        
        if 0 == sid:
            return 0, dice_val, 1
        elif 1 == sid:
            #get cannon
            return  3, dice_val, None
        elif 2 == sid:
            return 0, dice_val, 1
        elif 3 == sid:
            return 0, dice_val, 1
        elif 4 == sid:
            return 0, dice_val, 0
        elif 5 == sid:
            #get food
            return  1, dice_val, None
        elif 6 == sid:
            #get gold
            return  2, dice_val, None
        elif 7 == sid:
            if dice_val - 2 >= 0:
                return 0, dice_val - 2, 1
            elif dice_val - 2 < 0:
                return 0, abs(dice_val - 2), 0 
        elif 8 == sid:
            return 0, dice_val - 1, 1
        elif 9 == sid:
            #get gold
            return  2, dice_val, None
        elif 10 == sid:
            #get food
            return 1, dice_val, None
        elif 11 == sid:
            #get cannon
            return 3, dice_val, None
            
def resource_ai():
    dir1 = 0
    dir2 = 0
    sdir1 = 1
    sdir2 = 1
    resource_max = 0
    total_food = 0
    total_gold = 0
    r_sum = 0
    s_card = 0
    first = 1
    org_food = 0
    org_gold = 0
    type1, dv1, fwd1 = 0, 0, 0
    type2, dv2, fwd2 = 0, 0, 0
    for i in range(0, dock_num):
        if 1 == player_data[turn_id].dtype:
            org_food += player_data[turn_id].dvalue
        elif 2 == player_data[turn_id].dtype:
            org_gold += player_data[turn_id].dvalue
    
    for c in range(0, total_card_num):
        if 2 == player_data[turn_id].marked_card[c]:
            if 1 == first:
                s_card = c
                first = 0
                
            total_food = org_food
            total_gold = org_gold
            dest = player_data[turn_id].b_id
            
            # 0 == night
            type1, dv1, fwd1 = card_action(0, c)
            # 1 == night
            type2, dv2, fwd2 = card_action(1, c)
            if 1 == type1:
                r_sum += dv1
                total_food += dv1
            elif 2 == type1:
                r_sum += dv1
                total_gold += dv1
            elif 3 == type1:
                r_sum += dv1
            else:
                if 0 == fwd1:
                    dv1 = (-1) * dv1
                outer, inner = go_dest_id(player_data[turn_id].b_id, dv1)
                res1, food1, gold1 = resource_dest(outer, r_sum, total_food, total_gold)
                res2, food2, gold2 = resource_dest(inner, r_sum, total_food, total_gold)
                if (food1 < 0 or gold1 < 0) and (food2 < 0 or gold2 < 0):
                    # fail
                    continue
                elif food2 < 0 or gold2 < 0:
                    r_sum, total_food, total_gold = res1, food1, gold1
                    dest = outer
                    dir1 = 1
                elif food1 < 0 or gold1 < 0:
                    r_sum, total_food, total_gold = res2, food2, gold2
                    dest = inner
                    dir1 = 2
                else:
                    if res2 > res1:
                        r_sum, total_food, total_gold = res2, food2, gold2
                        dest = inner
                        dir1 = 2
                    else:
                        r_sum, total_food, total_gold = res1, food1, gold1
                        dest = outer
                        dir1 = 1
            
            if 1 == type2:
                r_sum += dv2
                total_food += dv2
            elif 2 == type2:
                r_sum += dv2
                total_gold += dv2
            elif 3 == type2:
                r_sum += dv2
            else:
                if 0 == fwd2:
                    dv2 = (-1) * dv2
                outer, inner = go_dest_id(dest, dv2)
                res1, food1, gold1 = resource_dest(outer, r_sum, total_food, total_gold)
                res2, food2, gold2 = resource_dest(inner, r_sum, total_food, total_gold)
                if (food1 < 0 or gold1 < 0) and (food2 < 0 or gold2 < 0):
                    # fail
                    continue
                elif food2 < 0 or gold2 < 0:
                    r_sum, total_food, total_gold = res1, food1, gold1
                    dir2 = 1
                    #dest = outer
                elif food1 < 0 or gold1 < 0:
                    r_sum, total_food, total_gold = res2, food2, gold2
                    dir2 = 2
                    #dest = inner
                else:
                    if res2 > res1:
                        r_sum, total_food, total_gold = res2, food2, gold2
                        dir2 = 2
                        #dest = inner
                    else:
                        r_sum, total_food, total_gold = res1, food1, gold1
                        dir2 = 1
                        #dest = outer    
            
            if r_sum > resource_max:
                resource_max = r_sum
                s_card = c
                sdir1 = dir1
                sdir2 = dir2
        r_sum = 0
    return s_card, sdir1, sdir2, resource_max
    
def forward_ai():
    dir1 = 0
    dir2 = 0
    sdir1 = 1
    sdir2 = 1
    step_max = 0
    total_food = 0
    total_gold = 0
    r_sum = 0
    s_card = -1
    first = 1
    org_food = 0
    org_gold = 0
    type1, dv1, fwd1 = 0, 0, 0
    type2, dv2, fwd2 = 0, 0, 0
    for i in range(0, dock_num):
        if 1 == player_data[turn_id].dtype:
            org_food += player_data[turn_id].dvalue
        elif 2 == player_data[turn_id].dtype:
            org_gold += player_data[turn_id].dvalue
    
    for c in range(0, total_card_num):
        if 2 == player_data[turn_id].marked_card[c]:
            if 1 == first:
                s_card = c
                first = 0
                
            total_food = org_food
            total_gold = org_gold
            dest = player_data[turn_id].b_id
            
            # 0 == night
            type1, dv1, fwd1 = card_action(0, c)
            # 1 == night
            type2, dv2, fwd2 = card_action(1, c)
            if 1 == type1:
                r_sum += dv1
                total_food += dv1
            elif 2 == type1:
                r_sum += dv1
                total_gold += dv1
            #elif 3 == type1:
            #    r_sum += dv1
            else:
                if 0 == fwd1:
                    dv1 = (-1) * dv1
                outer, inner = go_dest_id(player_data[turn_id].b_id, dv1)
                res1, food1, gold1 = resource_dest(outer, r_sum, total_food, total_gold)
                res2, food2, gold2 = resource_dest(inner, r_sum, total_food, total_gold)
                if (food1 < 0 or gold1 < 0) and (food2 < 0 or gold2 < 0):
                    # fail
                    continue
                elif food2 < 0 or gold2 < 0:
                    dir1 = 1
                elif food1 < 0 or gold1 < 0:
                    dir1 = 2
                else:
                    dir1 = 2
            
            if 1 == type2:
                r_sum += dv2
                total_food += dv2
            elif 2 == type2:
                r_sum += dv2
                total_gold += dv2
            #elif 3 == type2:
            #    r_sum += dv2
            else:
                if 0 == fwd2:
                    dv2 = (-1) * dv2
                outer, inner = go_dest_id(dest, dv2)
                res1, food1, gold1 = resource_dest(outer, r_sum, total_food, total_gold)
                res2, food2, gold2 = resource_dest(inner, r_sum, total_food, total_gold)
                if (food1 < 0 or gold1 < 0) and (food2 < 0 or gold2 < 0):
                    # fail
                    continue
                elif food2 < 0 or gold2 < 0:
                    dir2 = 1
                elif food1 < 0 or gold1 < 0:
                    dir2 = 2
                else:
                    dir2 = 2   
            
            if dv1 + dv2 > step_max:
                step_max = dv1 + dv2
                s_card = c
                sdir1 = dir1
                sdir2 = dir2
        r_sum = 0
    return s_card, sdir1, sdir2, step_max
    
def ai():
    global  player_data, dice_value1, dice_value2
    s_card = 0
    dir1 = 1
    dir2 = 1
    if start_p == turn_id and 0 == player_data[turn_id].mode:
        dice_value1 = random.randint(0, 23)
        dice_value2 = random.randint(0, 23)
        pygame.display.update()
        time.sleep(1)
        r = random.randint(0, 2)
        if 0 == r:
            card1, d1, d2, max1 = forward_ai()
            dice_value1, dice_value2 = dice_value2, dice_value1
            card2, sd1, sd2, max2 = forward_ai()
            if max1 > max2: # back to original
                s_card = card1
                dir1 = d1
                dir2 = d2
                dice_value1, dice_value2 = dice_value2, dice_value1
            else: # swap dice
                s_card = card2
                dir1 = sd1
                dir2 = sd2
        else: # 1, 2 == r
            card1, d1, d2, max1 = resource_ai()
            dice_value1, dice_value2 = dice_value2, dice_value1
            card2, sd1, sd2, max2 = resource_ai()
            if max1 > max2: # back to original
                s_card = card1
                dir1 = d1
                dir2 = d2
                dice_value1, dice_value2 = dice_value2, dice_value1
            else: # swap dice
                s_card = card2
                dir1 = sd1
                dir2 = sd2
        player_data[turn_id].selected_card_value = s_card
        player_data[turn_id].marked_card[s_card] = 1
        player_data[turn_id].mode = 5
        pygame.display.update()
    elif 0 == player_data[turn_id].mode:
        r = random.randint(0, 2)
        if 0 == r:
            s_card, dir1, dir2, max1 = forward_ai()
        else: # 1, 2 == r
            s_card, dir1, dir2, max1 = resource_ai()
        player_data[turn_id].selected_card_value = s_card
        player_data[turn_id].marked_card[s_card] = 1
        player_data[turn_id].mode = 5
    
    return dir1, dir2

def remain_treasure_card():
    global treasure_card
    sum = 0
    for i in range(0, treasure_num):
        if 0 == treasure_card[i]:
            sum += 1
    return sum
    
def get_treasure(t_id, b_id):
    global player_data, treasure_card, main_map
    index = 0
    remain_tc = remain_treasure_card()
    if remain_tc > 0:
        tc = random.randint(1, remain_tc)
        while tc > 0:
            if 0 == treasure_card[index]:
                tc -= 1
            if tc > 0:
                index += 1
        
        treasure_card[index] = 1
        player_data[t_id].treasure[index] = 1
    main_map[b_id].type = 0
    player_data[t_id].mode = 6
    
def step_done(t_id, b_id):
    global player_data, main_map, draw_player_thread
    #type:0 = nothing,1 = treasure, 2 = gold coin, 3 = food
    type  = main_map[b_id].type
    value = main_map[b_id].value
    fail = 0
    
    if 1 == type:
        get_treasure(t_id, b_id)
    elif 2 == type:
        fail = spend_dock_resource(2, value)
    elif 3 == type:
        fail = spend_dock_resource(1, value)
    else: # 0 == type
        player_data[t_id].mode = 6
        print("step=%d"%player_data[t_id].step)
        
    if 1 == fail:
        player_data[t_id].step = 1
        player_data[t_id].forward = 0
        player_data[t_id].dir[draw_player_thread.is_night] = 1
    
def end_turn():
    global player_data, start_p, turn_id, draw_player_thread
    
    for i in range(0, player_num):
        player_data[i].mode = 0
        player_data[i].handle_done = [0, 0]
        player_data[i].selected_card_value = None
        pick_up_one_card(i)
    
    draw_player_thread.is_night = 0
    start_p = (start_p+1)%player_num
    turn_id = start_p

def handle_card(mouse_loc):
    global player_data, turn_id
    (mouseX, mouseY) = mouse_loc
    card_x =  margin+big_block+inner_gap
    card_y =  margin+big_block+inner_gap+di_1_2.get_height()+button1.get_height()+inner_gap
    for i in range(0, total_card_num):
        if 2 == player_data[turn_id].marked_card[i]:        
            if card_x <= mouseX <= card_x + mv2.get_width() and card_y <= mouseY <= card_y + mv2.get_height():
                if None == player_data[turn_id].selected_card_value:
                    player_data[turn_id].selected_card_value = i
                    player_data[turn_id].marked_card[i] = 1
                else:
                    player_data[turn_id].marked_card[player_data[turn_id].selected_card_value] = 2
                    player_data[turn_id].selected_card_value = i
                    player_data[turn_id].marked_card[i] = 1
            card_y += mv2.get_height() + inner_gap
    if None != player_data[turn_id].selected_card_value and card_x <= mouseX <= card_x + button1.get_width() and card_y <= mouseY <= card_y + button1.get_height():
        player_data[turn_id].mode = 6
        turn_id = (turn_id + 1)%player_num
    
def main():
    global draw_player_thread, player_data, dice_value1, dice_value2, turn_id, start_p
    
    dir1 = 1
    dir2 = 1
    
    generate_map()
    generate_dock()
    generate_player_card()
    draw_player_thread.start()
    # test p backward
    #pd = draw_player_thread.player_data
    #pd[0].step = 6
    #pd[0].mode = 1
    #pd[0].forward = 1
    # end test p
    while True:        
        screen.blit(background, (0,0))
        draw_dock()
        draw_map(screen)
        draw_inner_item(screen)        
        draw_player_thread.run()
        if 3 != player_data[turn_id].mode and 4 != player_data[turn_id].mode and 5 != player_data[turn_id].mode:
            draw_selected_card(turn_id, start_p, player_data[turn_id].mode)
        pygame.display.update()
        
        if 0 == player_data[turn_id].IsAI:
            if start_p == turn_id and 0 == player_data[turn_id].mode:
                player_data[turn_id].mode = 3
            elif 0 == player_data[turn_id].mode:
                player_data[turn_id].mode = 5
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif 0 == player_data[turn_id].IsAI:
                if 3 == player_data[turn_id].mode and event.type == pygame.MOUSEBUTTONDOWN:
                    (mouseX, mouseY) = pygame.mouse.get_pos()
                    (x, y) = (margin+big_block+inner_gap, margin+big_block+inner_gap+di_1_2.get_height())
                    if x <= mouseX <= x+button1.get_width() and y <= mouseY <= y+button1.get_height():
                        dice1 = random.randint(0, 23)
                        dice2 = random.randint(0, 23)
                        dice_value1 = dice1
                        dice_value2 = dice2
                        player_data[turn_id].mode = 4
                if 4 == player_data[turn_id].mode and event.type == pygame.MOUSEBUTTONDOWN:
                    (mouseX, mouseY) = pygame.mouse.get_pos()
                    (x, y) = (margin+big_block+inner_gap, margin+big_block+inner_gap+di_1_2.get_height())
                    if x <= mouseX <= x+button1.get_width() and y <= mouseY <= y+button1.get_height():
                        (dice_value1, dice_value2) = (dice_value2, dice_value1)
                    handle_card((mouseX, mouseY))
                if 5 == player_data[turn_id].mode and event.type == pygame.MOUSEBUTTONDOWN:
                    (mouseX, mouseY) = pygame.mouse.get_pos()
                    handle_card((mouseX, mouseY))
                if 2 == player_data[turn_id].mode and event.type == pygame.MOUSEBUTTONDOWN:
                    (mouseX, mouseY) = pygame.mouse.get_pos()
                    aimg, aimg_alpha, loc1, loc2 = bid_to_arrow_image_and_pos(player_data[turn_id].b_id)
                    (x1, y1) = loc1
                    (x2, y2) = loc2
                    if 1 == player_data[turn_id].forward:
                        outer, inner = go_dest_id(player_data[turn_id].b_id, 1)
                    else:
                        outer, inner = go_dest_id(player_data[turn_id].b_id, -1)
                                    
                    if x1 < mouseX < x1 + aimg.get_width() and y1 < mouseY < y1 + aimg.get_height():
                        player_data[turn_id].next_id = outer
                        player_data[turn_id].dir[draw_player_thread.is_night] = 1
                        player_data[turn_id].mode = 1
                    elif x2 < mouseX < x2 + aimg.get_width() and y2 < mouseY < y2 + aimg.get_height():
                        player_data[turn_id].next_id = inner
                        player_data[turn_id].dir[draw_player_thread.is_night] = 2
                        player_data[turn_id].mode = 1
                
        
        if 1 == player_data[turn_id].IsAI:
            player_data[turn_id].dir[0],  player_data[turn_id].dir[1] =  ai()
            if 5 == player_data[turn_id].mode:
                #draw_selected_card(turn_id, start_p, player_data[turn_id].mode)
                if (turn_id + 1)%player_num == start_p:
                    turn_id = (turn_id + 1)%player_num
                    for i in range(0, player_num):
                        # human mode also mode = 6
                        player_data[i].mode = 6
        
        if 6 == player_data[turn_id].mode:
            if 0 == player_data[turn_id].handle_done[draw_player_thread.is_night]:
                handle_step(draw_player_thread.is_night, player_data[turn_id].dir[draw_player_thread.is_night])
                player_data[turn_id].handle_done[draw_player_thread.is_night] = 1
            elif 1 == player_data[turn_id].handle_done[draw_player_thread.is_night] and 0 == player_data[turn_id].step:
                step_done(turn_id, player_data[turn_id].b_id)
            
            if player_data[turn_id].step > 0:
                player_data[turn_id].mode = 1
            #draw_selected_card(turn_id, start_p, player_data[turn_id].mode)
            print("[%d].mode=%d, step=%d, fwd=%d"%(turn_id, player_data[turn_id].mode, player_data[turn_id].step, player_data[turn_id].forward))
        
        if 1 == player_data[turn_id].mode and 0 == player_data[turn_id].step:
            # do spend_dock_resource or get_treasure 
            step_done(turn_id, player_data[turn_id].b_id)
            print("step = %d,done, fwd=%d"%(player_data[turn_id].step, player_data[turn_id].forward))
            
        if 1 == player_data[turn_id].IsAI and 0 == player_data[turn_id].step:    
            if (turn_id + 1)%player_num == start_p:
                if 0 == draw_player_thread.is_night:
                    turn_id = start_p
                    draw_player_thread.is_night = 1
                else: # draw_player_thread.is_night == 1
                    end_turn()
            else:
                turn_id = (turn_id + 1)%player_num
            print("AI turn_id=%d"%turn_id)
        elif 0 == player_data[turn_id].IsAI and 6 == player_data[turn_id].mode:
            if (turn_id + 1)%player_num == start_p:
                if 0 == draw_player_thread.is_night:
                    turn_id = start_p
                    draw_player_thread.is_night = 1
                else: # draw_player_thread.is_night == 1
                    end_turn()
            else:
                turn_id = (turn_id + 1)%player_num
            print("human turn_id=%d"%turn_id)
            
    pygame.quit()
    quit()

if __name__ == "__main__":
    main()