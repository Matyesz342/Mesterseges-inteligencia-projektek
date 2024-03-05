class Hanoi:
    def __init__(self,k,t):
        self.start = k
        self.target = t

    def finish(self, action):
        return action == self.target
    def next(self,action):
        child_cs = list()
        for melyiket in range(0,3):
            for hova in ['P','Q','R']:
                flag = True # feltételezem, hogy az operátor alkalmazható
                # az operátor alkalmazási előfeltételeinek ellenőrzése
                if action[melyiket] != hova:
                    for i in range(0,melyiket): # bármely i<melyiket
                        if action[i] != action[melyiket] and action[i] != hova:
                            flag = True
                        else:
                            flag = False
                            break
                else:
                    flag = False
                # az operátor alkalmazható, akkor a flag = True
                if flag:
                    tmp = list(action)
                    tmp[melyiket] = hova
                    e = tuple(tmp)
                    child_cs.append(""+str(melyiket)+"-->"+hova,e)
        return child_cs

if __name__ == "__main__":
    ha= Hanoi(('P','P','P'),('Q','Q','Q'))