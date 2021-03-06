total_card_num = 10
dock_num = 5
treasure_num = 10

class game_player():
    def __init__(self, x_now = 0, y_now = 0, block_id = 0, next_block_id = 0, location=(0, 0), IsAI = 1, handle_done = [0, 0] ,steps = 0, mode = 0, direction = [0, 0], Is_Forward = 1, goal_game = 0, selected_card_value = None, marked_card = [0] * total_card_num, remain_card_num = total_card_num, show_card = 2, dock_type = [0] * dock_num, dock_value = [0] * dock_num, treasure_own = [0] * treasure_num, fight_dice = None, fight_cannon = 0, fight_score = None, fight_solution = "", fight_text = "", final_gold = 0, final_location = 0, final_treasure = 0, final_score = 0, final_win = ""):
        self.x = x_now
        self.y = y_now
        self.b_id = block_id
        self.next_id = next_block_id
        # loc = [[x0, y0], [x1, y1], [x2, y2] ...]
        self.loc = location
        self.IsAI = IsAI
        self.handle_done = handle_done[:]
        # step is positive value only
        self.step = steps
        # mode 0:nothing, 1:moving 2:suspend, 3:roll, 4:swap, 5: finish step(selected card only), 6: handle step 7: fight, 8: end fight(take/pay) 9: end turn
        self.mode = mode
        # dir 0:nothing, 1:outer, 2:inner
        self.dir = direction[:]
        self.forward = Is_Forward
        self.goal_game = goal_game
        self.selected_card_value = selected_card_value
        # 0: unused, 1: showed card, 2:own card
        self.marked_card = marked_card[:]
        self.remain_card_num = remain_card_num
        #0:back card, 1:show card, 2: won't show anything
        self.show_card = show_card
        
        # 0: unused, 1:food, 2:gold, 3: cannon
        self.dtype = dock_type[:]
        self.dvalue = dock_value[:]
        # index: 0:food, 1:gold, 2~9: 2~9 points
        # num_of_treasure_own(t_id) won't display 0:food and 1:gold
        # value: 0: unused, 1: own
        self.treasure = treasure_own[:]
        # None, 0~11
        self.fight_dice = fight_dice
        # 0 ~ 30
        self.fight_cannon = fight_cannon
        # None, 0~40, "max"
        self.fight_score = fight_score
        # Only three string, 1. null string: "", 2. "win" 3. "draw"
        self.fight_solution = fight_solution
        # "", "None", "Take", "Put"
        self.fight_text = fight_text
        
        self.final_gold = final_gold
        self.final_location = final_location
        self.final_treasure = final_treasure
        self.final_score = final_score
        self.final_win = final_win