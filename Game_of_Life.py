from tkinter import *

class Field:
    def __init__(self, c, n, m, width, height, walls=False):

        self.c = c
        self.a = []
        self.n = n + 2
        self.m = m + 2
        self.width = width
        self.height = height
        self.count = 0
        for i in range(self.n):
            self.a.append([])
            for j in range(self.m):
                # self.a[i].append(choice([0, 1]))
                self.a[i].append(0)


        self.a[24][24] = 1
        self.a[24][25] = 1
        self.a[24][26] = 1
        self.a[25][24] = 1
        self.a[25][25] = 1
        self.a[25][26] = 1
        self.a[26][24] = 1
        self.a[26][25] = 1
        self.a[26][26] = 1
        self.draw()

    def step(self):
        b = []
        for i in range(self.n):
            b.append([])
            for j in range(self.m):
                b[i].append(0)

        for x in range(1, self.n - 1):
            for y in range(1, self.m - 1):
                n_sum = self.a[x - 1][y - 1] + self.a[x - 1][y] + self.a[x - 1][y + 1] + self.a[x][y - 1] + \
                        self.a[x][y + 1] + self.a[x + 1][y - 1] + self.a[x + 1][y] + self.a[x + 1][y + 1]
                if n_sum < 2 or n_sum > 3:
                    b[x][y] = 0
                elif n_sum == 3:
                    b[x][y] = 1
                else:
                    b[x][y] = self.a[x][y]
        self.a = b

    def print_field(self):
        for i in range(self.n):
            for j in range(self.m):
                print(self.a[i][j], end="")
            print()

    def draw(self):
        color = "blue"
        sizen = self.width // (self.n - 2)
        sizem = self.height // (self.m - 2)
        for i in range(1, self.n - 1):
            for j in range(1, self.m - 1):
                if (self.a[i][j] == 1):
                    color = "yellow"
                else:
                    color = "white"
                self.c.create_rectangle((i - 1) * sizen, (j - 1) * sizem, (i) * sizen, (j) * sizem, fill=color)
        self.step()
        self.c.after(100, self.draw)


class Player:
    def __init__(self, c, x, y, size, color="RED"):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.c = c
        self.body = self.c.create_oval(self.x - self.size / 2,
                                       self.y - self.size / 2,
                                       self.x + self.size / 2,
                                       self.y + self.size / 2,
                                       fill=self.color)

    def moveto(self, x, y):
        self.mx = x
        self.my = y
        self.dx = (self.mx - self.x) / 50
        self.dy = (self.my - self.y) / 50
        self.draw()

    def draw(self):
        self.x += self.dx
        self.y += self.dy
        self.c.move(self.body, self.dx, self.dy)

        print(abs(self.x))
        if abs(self.mx - self.x) > 2:
            self.c.after(100, self.draw)

    def distance(self, x, y):
        return ((self.x - x) ** 2 + (self.y - y) ** 2) ** 0.5


root = Tk()
root.geometry("800x800")
c = Canvas(root, width=800, height=800)
c.pack()

root.title('Game of Life')
f = Field(c, 50, 50, 800, 800)
f.print_field()

root.mainloop()
