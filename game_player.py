class game_player():
    def __init__(self, block_id = 0, next_block_id = 0, location=(0, 0), IsAI = 1, steps = 0, mode = 0):
        self.b_id = block_id
        self.next_id = next_block_id
        self.loc = location
        self.IsAI = IsAI
        self.step = steps
        # mode 0:nothing, 1:moving 2:suspend
        self.mode = mode