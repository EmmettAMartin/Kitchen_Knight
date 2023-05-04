class Player:

    sprite_state = "standing"

    def __init__(self, curr_pos_x, curr_pos_y, prev_x, prev_y, starting_x, starting_y) -> None:
        
        self.curr_pos_x = curr_pos_x
        self.curr_pos_y = curr_pos_y
        self.prev_x = prev_x
        self.prev_y = prev_y
        self.starting_x = starting_x
        self.starting_y = starting_y
    
    def player_move_left(self):

        self.curr_pos_x = self.prev_x
        self.curr_pos_x -= 10
        Player.stand()
        return self.curr_pos_x
    
    def player_move_right(self):
        
        Player.sprite_state = "running"
        self.curr_pos_x = self.prev_x
        self.curr_pos_x += 10
        Player.stand()
        return self.curr_pos_x
    
    def player_jump(self):

        y_list = []

        self.curr_pos_y = self.prev_y
        Player.sprite_state = "jumping"

        for i in range(30):
            self.curr_pos_y -= 1
            y_list.append(self.curr_pos_y)

        for i in range(30):
            self.curr_pos_y += 1
            y_list.append(self.curr_pos_y)

        Player.stand()
        return y_list

    
    def stand():
        Player.sprite_state = "standing"

if __name__ == "__main__":
    
    john = Player(5, 5, 5, 5, 5, 5)

    print(john.player_jump())