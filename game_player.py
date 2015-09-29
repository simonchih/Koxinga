total_card_num = 10

class game_player():
    def __init__(self, x_now = 0, y_now = 0, block_id = 0, next_block_id = 0, location=(0, 0), IsAI = 1, steps = 0, mode = 0, direction = 0, Is_Forward = 1, goal_game = 0, selected_card_value = None, marked_card = [0] * total_card_num, remain_card_num = total_card_num):
        self.x = x_now
        self.y = y_now
        self.b_id = block_id
        self.next_id = next_block_id
        self.loc = location
        self.IsAI = IsAI
        self.step = steps
        # mode 0:nothing, 1:moving 2:suspend, 3:roll, 4:swap, 5: finish step, 6: fight, 7: end fight
        self.mode = mode
        # dir 0:nothing, 1:outer, 2:inner
        self.dir = direction
        self.forward = Is_Forward
        self.goal_game = goal_game
        self.selected_card_value = selected_card_value
        # 0: unused, 1: showed card, 2:own card
        self.marked_card = marked_card[:]
        self.remain_card_num = remain_card_num