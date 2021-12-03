import copy

map = [[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
       [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
       [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1],
       [1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
       [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1],
       [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1],
       [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
       [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
       [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1],
       [1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1],
       [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]]
m1 = [[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
      [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
      [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
      [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1],
      [1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
      [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1],
      [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1],
      [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
      [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
      [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1],
      [1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1],
      [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]]
m2 = [[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
      [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
      [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
      [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1],
      [1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
      [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1],
      [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1],
      [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
      [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
      [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1],
      [1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1],
      [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
      [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]]
m3 = [[0, 1, 1, 1, 1, 1],
      [0, 0, 0, 0, 0, 1],
      [1, 0, 0, 0, 0, 1],
      [1, 0, 0, 0, 0, 1],
      [1, 0, 0, 0, 0, 1],
      [1, 1, 1, 1, 0, 0], ]

m4 = [[0, 1, 1, 1, 1, 1],
      [0, 0, 0, 0, 0, 1],
      [1, 0, 1, 1, 1, 1],
      [1, 0, 0, 0, 0, 1],
      [1, 0, 1, 1, 0, 1],
      [1, 1, 1, 1, 0, 0], ]


class Player:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move(self, dir):
        if dir == 'up':
            self.y += 1
        elif dir == 'down':
            self.y -= 1
        elif dir == 'left':
            self.x -= 1
        elif dir == 'right':
            self.x += 1
        pass

    def get_position(self):
        return (self.y, self.x)


class MazeGame:
    def __init__(self, map=None):
        self.map = map
        self.player = Player()
        self.path = []
        self.map_1 = copy.deepcopy(self.map)

    def play(self):

        self.path.append(self.player.get_position())
        if self.player.get_position() == (len(self.map) - 1, len(self.map) - 1):
            return

        self.player.move('up')

        if self.player.x > len(self.map) - 1 or self.player.y > len(self.map) - 1:
            self.player.move('down')
        else:

            if self.map[self.player.x][self.player.y] == 0:
                if (self.player.y, self.player.x) in self.path:
                    self.map[self.player.x][self.player.y - 1] = 1
                # print("up")
                return self.play()
            else:
                self.player.move('down')

        self.player.move('right')

        if self.player.x > len(self.map) - 1 or self.player.y > len(self.map) - 1:
            self.player.move('left')
        else:
            if self.map[self.player.x][self.player.y] == 0:
                if (self.player.y, self.player.x) in self.path:
                    self.map[self.player.x - 1][self.player.y] = 1

                # print("right")

                return self.play()
            else:
                self.player.move('left')

        self.player.move('left')

        if self.player.x > len(self.map) - 1 or self.player.y > len(self.map) - 1:
            self.player.move('right')
        else:
            if self.map[self.player.x][self.player.y] == 0:
                if (self.player.y, self.player.x) in self.path:
                    self.map[self.player.x + 1][self.player.y] = 1
                # print("left")
                return self.play()
            else:
                self.player.move('right')

        self.player.move('down')

        if self.player.x > len(self.map) - 1 or self.player.y > len(self.map) - 1:
            self.player.move('up')
        else:
            if self.map[self.player.x][self.player.y] == 0:
                if (self.player.y, self.player.x) in self.path:
                    self.map[self.player.x][self.player.y + 1] = 1
                # print("down")
                return self.play()
            else:
                self.player.move('up')

        return

    def get_map(self):
        return self.map_1

    def get_path(self):
        return self.path


if __name__ == "__main__":
    game1 = MazeGame(m1)
    game1.play()
    print(game1.get_map())
    print(game1.get_path())