class Map:
    def __init__(self, map_path):
        
        with open(map_path) as map_obj:
            map_file = map_obj.readlines()
            self.start = [int(coordinate) for coordinate in map_file[0].split()]
            self.exit = [int(coordinate) for coordinate in map_file[1].split()]
            self.treasure = [int(coordinate) for coordinate in map_file[2].split()]
            shape = int(map_file[3])
            
            self.vertical_borders = []
            for row in range(4, shape + 4):
                self.vertical_borders.append([int(border) for border in map_file[row].split()])
            
            self.horizontal_borders = []
            for row in range(shape + 4, 2 * shape + 4):
                self.horizontal_borders.append([int(border) for border in map_file[row].split()])
        
        self.motions = {'up': (0, 1),
                        'down': (0, -1),
                        'left': (-1, 0),
                        'right': (1, 0)}
        
    def possible_move(self, departure, movement):
        result = True
        x_shift, y_shift = self.motions[movement]
        
        if x_shift != 0:
            if x_shift == 1:
                if self.vertical_borders[departure[1]][departure[0] + 1] == 1:
                    result = False
            elif x_shift == -1:
                if self.vertical_borders[departure[1]][departure[0]] == 1:
                    result = False
            
        elif y_shift != 0:
            if y_shift == 1:
                if self.horizontal_borders[departure[0]][departure[1] + 1] == 1:
                    result = False
            elif y_shift == -1:
                if self.horizontal_borders[departure[0]][departure[1]] == 1:
                    result = False
        
        return result
    
    def get_start_position(self):
        return self.start
    
    def get_exit_position(self):
        return self.exit
    
    def get_treasure_position(self):
        return self.treasure