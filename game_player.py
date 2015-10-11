total_card_num = 10
dock_num = 5
treasure_num = 10

class game_player():
    def __init__(self, x_now = 0, y_now = 0, block_id = 0, next_block_id = 0, location=(0, 0), IsAI = 1, steps = 0, mode = 0, direction = [0, 0], Is_Forward = 1, goal_game = 0, selected_card_value = None, marked_card = [0] * total_card_num, remain_card_num = total_card_num, dock_type = [0] * dock_num, dock_value = [0] * dock_num, treasure_own = [0] * treasure_num):
        self.x = x_now
        self.y = y_now
        self.b_id = block_id
        self.next_id = next_block_id
        self.loc = location
        self.IsAI = IsAI
        # step is positive value only
        self.step = steps
        # mode 0:nothing, 1:moving 2:suspend, 3:roll, 4:swap, 5: finish step, 6: handle step 7: fight, 8: end fight(take/pay) 9: end turn
        self.mode = mode
        # dir 0:nothing, 1:outer, 2:inner
        self.dir = direction[:]
        self.forward = Is_Forward
        self.goal_game = goal_game
        self.selected_card_value = selected_card_value
        # 0: unused, 1: showed card, 2:own card
        self.marked_card = marked_card[:]
        self.remain_card_num = remain_card_num
        # 0: unused, 1:food, 2:gold, 3: cannon
        self.dtype = dock_type[:]
        self.dvalue = dock_value[:]
        # index: 0:food, 1:gold, 2~9: 2~9 points
        # value: 0: unused, 1: own
        self.treasure = treasure_own[:]