from random import randint


class Cell:
    def __init__(self):
        self.around_mines = 0
        self.mine = False
        self.fl_open = False


class GamePole:
    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.pole = self.init()
        self.put_mines()
        # self.calc_around_mines() #По условию подсчет не требуется

    def init(self):
        return [[Cell() for _ in range(self.N)] for _ in range(self.N)]

    def put_mines(self):
        mines_placed = 0
        while mines_placed < self.M:
            i, j = randint(0, self.N - 1), randint(0, self.N - 1)
            if not self.pole[i][j].mine: #Если в клетке еще нет мины
                self.pole[i][j].mine = True
                mines_placed += 1

    def calc_around_mines(self):
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1), (0, 1),
                      (1, -1), (1, 0), (1, 1)]

        for i in range(self.N):
            for j in range(self.N):
                if not self.pole[i][j].mine:
                    count = 0
                    for di, dj in directions:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < self.N and 0 <= nj < self.N:
                            if self.pole[ni][nj].mine:
                                count += 1
                    self.pole[i][j].around_mines = count

    def show(self):
        for row in self.pole:
            for cell in row:
                # if not cell.fl_open:
                if not cell.fl_open and not cell.mine:  # Чтобы соответствовало условию задачи
                    print('#', end=' ')
                elif cell.mine:
                    print('*', end=' ')
                else:
                    print(cell.around_mines, end=' ')
            print()


pole_game = GamePole(10, 12)
pole_game.show()