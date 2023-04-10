import time

class Player:
    def __init__(self, curr_pos_x, curr_pos_y, prev_x, prev_y, starting_x, starting_y, sprite_state) -> None:

        self.curr_pos_x = curr_pos_x
        self.curr_pos_y = curr_pos_y
        self.prev_x = prev_x
        self.prev_y = prev_y
        self.starting_x = starting_x
        self.starting_y = starting_y
        self.sprite_state = sprite_state
    
    def player_move_left(self):

        self.curr_pos_x = self.prev_x
        self.curr_pos_x -= 10
        return self.curr_pos_x
    
    def player_move_right(self):

        self.curr_pos_x = self.prev_x
        self.curr_pos_x += 10
        return self.curr_pos_x
    
    def player_jump(self):

        self.curr_pos_y = self.prev_y

        for i in range(30):
            self.curr_pos_y -= 1
            time.sleep(0.1)
            return self.curr_pos_y

        for i in range(30):
            self.curr_pos_y += 1
            time.sleep(0.1)
            return self.curr_pos_y