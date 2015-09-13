class game_map():
    def __init__(self, type=0, value=0):
        #type:0 = nothing,1 = treasure, 2 = gold coin, 3 = food
        self.type = type
        self.value = value