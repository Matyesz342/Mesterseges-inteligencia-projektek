class Domino:
    def __init__(self):
        self.start = [[0 for _ in range(8)] for _ in range(8)]
        self.goal = 1
        self.remains = 21

    def celteszt(self, state):
        return 64 - sum([i for row in state for i in row]) == self.goal and self.remains == 0

    def next(self, state):
        children = []

        for i in range(8):
            for j in range(8):
                if state[i][j] == 0:
                    # függőlegesen
                    if i <= 5 and state[i+1][j] == 0 and state[i+2][j] == 0:
                        child = [row[:] for row in state]
                        child[i][j] = child[i+1][j] = child[i+2][j] = 1
                        children.append(child)

                    # vízszintesen
                    if j <= 5 and state[i][j+1] == 0 and state[i][j+2] == 0:
                        child = [row[:] for row in state]
                        child[i][j] = child[i][j+1] = child[i][j+2] = 1
                        children.append(child)
        self.remains -= 1
        return children


if __name__ == "__main__":
    d = Domino()
    res = d.next(d.start)
    res = d.next(d.next(d.start)[0])
    temp = 1
    for mtx in res:
        for line in mtx:
            print(line)
        print("")
        