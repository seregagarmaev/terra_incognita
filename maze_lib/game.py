from maze_lib.map_class import Map
from maze_lib.player import Player

class Game:
    def __init__(self, map_path):
        maze_map = Map(map_path)
        self.player = Player(maze_map)
        self.status = 'started'
        self.motion_map = {'up': self.player.move_up,
                           'down': self.player.move_down,
                           'left': self.player.move_left,
                           'right': self.player.move_right}
    
    def __read_command(self):
        user_input = input('>')
        return user_input
    
    def play(self):
        while not self.player.has_won():
            print(f'Initial position {self.player.position}')
            command = self.__read_command()
            self.player.receive_command(command)
            print(f'Updated position {self.player.position}')