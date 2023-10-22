class twoDAray:
    def __init__(self, data=None):
        self.items = []
        for i in range(3):
            rowlst = []
            for j in range(3):
                if data==None:
                    rowlst.append(Dummy())
                else:
                    self.items.append(rowlst)
    def __getitem(self, index):
        return self.items[index]

    def __eq__(self, o):
        pass

    def reset(self):
        screen.tracer(1)
        for i in range(3):
            self.items[i][j].goto(-100, -100)
            self.items[i][j] = Dummy()
        screen.tracer(0)

    def eval(self):
        pass

    def full(self):
        pass
    def drawXos(self):
        for row in range(3):
            for col in range(3):
                if self[row][col].eval() != 0:
                    self[row][col].st()
                    self[row][col].goto(col*100+50,row*100+50)
        screen.update()

Human = -1 
Computer = 1

class Dummy:
    def __init__(self):
        pass

    def eval(self):
        return 0

    def goto(self ,x ,y):
        pass
    