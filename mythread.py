import threading
import pygame

screen_width = 1599
screen_height = 860

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Koxinga')

player_num = 6
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
t_end = map_block_num - 1
forward_suspend = [r_end, b_end, l_end]
backward_suspend = [t_start, l_start, b_start]

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

def go_dest_id(org_id, step = 0, is_forward = 1):
    dest_outer = 0
    dest_inner = None
    if 1 == is_forward:
        pseudo_dest = org_id + step
    else: #is_forward = 0
        pseudo_dest = org_id - step
    
    if pseudo_dest <= 0 or pseudo_dest > t_end:
        return dest_outer, dest_inner
    
    if 1 == is_forward:
        if (r_end >= org_id >= 0):
            dest_outer = pseudo_dest
            if pseudo_dest > r_end:
                # remain step for inner
                pseudo_dest = step - (r_end - org_id)
                dest_inner = pseudo_dest + rb_outer_end
        elif (rb_outer_end >= org_id >= rb_outer_start):
            if rb_outer_end >= pseudo_dest >= rb_outer_start:
                dest_outer = pseudo_dest
            else:
                # remain step for outer
                pseudo_dest = step - (rb_outer_end - org_id)
                dest_outer = pseudo_dest + b_start - 1
        elif (b_start > org_id > rb_outer_end):
            dest_outer = pseudo_dest
        elif (b_end >= org_id >= b_start):
            dest_outer = pseudo_dest
            if pseudo_dest > b_end:
                # remain step for inner
                pseudo_dest = step - (b_end - org_id)
                dest_inner = pseudo_dest + lb_outer_end
        elif (lb_outer_end >= org_id >= lb_outer_start):
            if lb_outer_end >= pseudo_dest >= lb_outer_start:
                dest_outer = pseudo_dest
            else:
                # remain step
                pseudo_dest = step - (lb_outer_end - org_id)
                dest_outer = pseudo_dest + l_start - 1
                if pseudo_dest > (l_end - l_start + 1):
                    pseudo_dest = pseudo_dest - (l_end - l_start + 1)
                    dest_inner = pseudo_dest + lt_outer_end
        elif (l_start > org_id > lb_outer_end):
            dest_outer = pseudo_dest
            if pseudo_dest > l_end:
                # remain step for inner
                pseudo_dest = step - (l_end - org_id)
                dest_inner = pseudo_dest + lt_outer_end
        elif (l_end >= org_id >= l_start):
            dest_outer = pseudo_dest
            if pseudo_dest > l_end:
                # remain step for inner
                pseudo_dest = step - (l_end - org_id)
                dest_inner = pseudo_dest + lt_outer_end
        elif lt_outer_end >= org_id >= lt_outer_start:
            if lt_outer_end >= pseudo_dest >= lt_outer_start:
                dest_outer = pseudo_dest
            else:
                # remain step for outer
                pseudo_dest = step - (lt_outer_end - org_id)
                dest_outer = pseudo_dest + t_start - 1
        elif t_start > org_id > lt_outer_end:
            dest_outer = pseudo_dest
        else: # org_id >= t_start
            dest_outer = pseudo_dest

    else: #is_forward = 0
        if t_end >= org_id >= t_start:
            if t_end >= pseudo_dest >= t_start:
                dest_outer = pseudo_dest
            else:
                cp_pseudo_dest = pseudo_dest
                #remain step for outer
                pseudo_dest = step - (org_id - t_start)
                dest_outer = lt_outer_end - pseudo_dest + 1
                if pseudo_dest <= t_start - (lt_outer_end + 1):
                    dest_inner = cp_pseudo_dest
                else:
                    pseudo_dest -= t_start - (lt_outer_end + 1)
                    dest_inner = lt_outer_start - pseudo_dest
        elif t_start > org_id > lt_outer_end:
            if t_start > pseudo_dest > lt_outer_end:
                dest_outer = pseudo_dest
            else:
                #remain step
                pseudo_dest = step - (org_id - (lt_outer_end + 1))
                if pseudo_dest > l_end - l_start + 1:
                    dest_inner = l_end - pseudo_dest + 1
                    pseudo_dest -= l_end - l_start + 1
                    dest_outer = lb_outer_end - pseudo_dest + 1
                else:
                    dest_outer = l_end - pseudo_dest + 1
        elif lt_outer_end >= org_id >= lt_outer_start:
            if pseudo_dest < l_start:
                #remain step
                pseudo_dest = step - (org_id - l_start)
                dest_inner = l_start - pseudo_dest
                dest_outer = lb_outer_end + 1 - pseudo_dest
            else:
                dest_outer = pseudo_dest
        elif l_end >= org_id >= l_start:
            if l_end >= pseudo_dest >= l_start:
                dest_outer = pseudo_dest
            else:
                #remain step
                pseudo_dest = step - (org_id - l_start)
                dest_outer = lb_outer_end + 1 - pseudo_dest
                if pseudo_dest > l_start -1 - lb_outer_end:
                    pseudo_dest -= l_start -1 - lb_outer_end
                    dest_inner = b_end +1 - pseudo_dest
                else:
                    dest_inner = l_start - pseudo_dest
        elif l_start > org_id > lb_outer_end:
            if l_start > pseudo_dest > lb_outer_end:
                dest_outer = pseudo_dest
            else:
                #remain step
                pseudo_dest = step - (org_id - (lb_outer_end + 1))
                dest_outer = b_end - pseudo_dest + 1
        elif lb_outer_end >= org_id >= lb_outer_start:
            dest_outer = pseudo_dest
        elif b_end >= org_id >= b_start:
            if b_end >= pseudo_dest >= b_start:
                dest_outer = pseudo_dest
            else:
                #remain step
                pseudo_dest = step - (org_id - b_start)
                dest_outer = rb_outer_end + 1 - pseudo_dest
                if pseudo_dest > b_start -1 - rb_outer_end:
                    pseudo_dest -= b_start -1 - rb_outer_end
                    dest_inner = r_end + 1 - pseudo_dest
                else:
                    dest_inner = b_start - pseudo_dest
        elif b_start > org_id > rb_outer_end:
            if b_start > pseudo_dest > rb_outer_end:
                dest_outer = pseudo_dest
            else:
                #remain step
                pseudo_dest = step - (org_id - (rb_outer_end + 1))
                dest_outer = r_end - pseudo_dest + 1
        elif rb_outer_end >= org_id >= rb_outer_start:
            dest_outer = pseudo_dest
        else: #elif r_end >= org_id >= r_start:
            dest_outer = pseudo_dest
        
    return dest_outer, dest_inner        
        
class mythread (threading.Thread):
    def __init__(self, threadID, surface, player_data):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.surface = surface
        self.player_data = player_data
    
    def run(self):
        for p in range(0, player_num):
            if 2 == self.player_data[p].mode:
                break
            (x, y) = (self.player_data[p].x, self.player_data[p].y)
            n_id = self.player_data[p].next_id
            if 1 == self.player_data[p].mode:
                if x == self.player_data[p].loc[n_id][0] and y == self.player_data[p].loc[n_id][1]:
                    if self.player_data[p].b_id != self.player_data[p].next_id:
                        if t_end == self.player_data[p].b_id and 0 == self.player_data[p].next_id:
                            print("goal game")
                            self.player_data[p].b_id = self.player_data[p].next_id
                            self.player_data[p].step = 0
                            self.player_data[p].goal_game = 1
                        else:
                            self.player_data[p].b_id = self.player_data[p].next_id
                            self.player_data[p].step -= 1
                    if 0 == self.player_data[p].step:
                       self.player_data[p].mode = 0
                       self.player_data[p].dir = 0
                    elif 1 == self.player_data[p].IsAI:
                        # move 1 step
                        outer, inner = go_dest_id(self.player_data[p].b_id, 1, self.player_data[p].forward)
                        if None == inner:
                            self.player_data[p].next_id = outer
                        elif 1 == self.player_data[p].dir:
                            self.player_data[p].next_id = outer
                        elif 2 == self.player_data[p].dir:
                            self.player_data[p].next_id = inner
                    elif 0 == self.player_data[p].IsAI:
                        if 1 == self.player_data[p].forward and (self.player_data[p].b_id in forward_suspend):
                            self.player_data[p].mode = 2
                            break
                        elif 0 == self.player_data[p].forward and (self.player_data[p].b_id in backward_suspend):
                            self.player_data[p].mode = 2
                            break
                        else:
                            # move 1 step
                            outer, inner = go_dest_id(self.player_data[p].b_id, 1, self.player_data[p].forward)
                            if None == inner:
                                self.player_data[p].next_id = outer
                            elif 1 == self.player_data[p].dir:
                                self.player_data[p].next_id = outer
                            elif 2 == self.player_data[p].dir:
                                self.player_data[p].next_id = inner
                if x < self.player_data[p].loc[n_id][0]:
                    self.player_data[p].x += 1
                if y < self.player_data[p].loc[n_id][1]:
                    self.player_data[p].y += 1
                if x > self.player_data[p].loc[n_id][0]:
                    self.player_data[p].x -= 1
                if y > self.player_data[p].loc[n_id][1]:
                    self.player_data[p].y -= 1
                                        
        for p in range(0, player_num):
                (x, y) = (self.player_data[p].x, self.player_data[p].y)
                self.surface.blit(player_id_to_image(p), (x, y))