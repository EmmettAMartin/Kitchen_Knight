import movement

move = movement.Mover()

class Player:
    def __init__(self, curr_pos_x, curr_pos_y, prev_x, prev_y, starting_x, starting_y) -> None:
        self.curr_pos_x = curr_pos_x
        self.curr_pos_y = curr_pos_y
        self.prev_x = prev_x
        self.prev_y = prev_y
        self.starting_x = starting_x
        self.starting_y = starting_y
    
    def player_move_left(self):
        move.move_left()