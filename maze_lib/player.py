class Player:
    def __init__(self, maze_map):
        self.maze_map = maze_map
        self.position = self.maze_map.get_start_position()
        self.exit = self.maze_map.get_exit_position()
        self.treasure = self.maze_map.get_treasure_position()
        
        self.motion_map = {'up': self.move_up,
                           'down': self.move_down,
                           'left': self.move_left,
                           'right': self.move_right}
        
        self.found_treasure = False
    
    def receive_command(self, movement):
        if movement in self.motion_map:
            if self.maze_map.possible_move(self.position, movement):
                self.motion_map[movement]()
                self.check_treasure()
                print(f'You went {movement}!')
            else:
                print('Impossible move')
        else:
            raise ValueError('Valid options to move are "up", "right", "down", "left"')
    
    def move_right(self):
        self.position[0] += 1
    def move_left(self):
        self.position[0] -= 1
    def move_up(self):
        self.position[1] += 1
    def move_down(self):
        self.position[1] -= 1
    
    def get_position(self):
        return self.position
    
    def check_treasure(self):
        if self.position == self.treasure:
            self.found_treasure = True
            print('You have found a treasure!')
        
    def has_treasure(self):
        return self.found_treasure
    
    def has_won(self):
        result = False
        if self.position == self.exit and self.has_treasure():
            result = True
        return result