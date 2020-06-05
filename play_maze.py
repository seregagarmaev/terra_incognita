from maze_lib.game import Game

if __name__ == '__main__':
    map_path = input('Enter the map path >')
    g = Game(map_path)
    g.play()
    print('You have reached the end of the mase!')