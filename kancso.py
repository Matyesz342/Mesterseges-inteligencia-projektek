class Jug:
    def __init__(self,k,c):
        self.start = k
        self.finish = c
        self.M1 = 3
        self.M2 = 5
        self.M3 = 8

    def finish_test(self, condition):
        #állapot = (a1,a2,a3)
        return condition[0]==self.finish or condition[1]==self.finish or condition[2]==self.finish
    def next(self,condition):
        child_node=list()
        a1,a2,a3=condition
        # tölt 1,2
        '''if a1!=0 and a2!=self.M2:
            T = min([a1,self.M2-a2])
            child_node.append(("a1-ből a2-be",(a1-T,a2+T,a3)))
        # tölt 1,3
        if a1!=0 and a3!=self.M3:
            T = min([a1,self.M3-a3])
            child_node.append(("a1-ből a3-be",(a1-T,a2,a3+T)))
        # tölt 2,1
        if a2!=0 and a1!=self.M1:
            T = min([a2,self.M1-a1])
            child_node.append(("a2-ből a1-be",(a1+T,a2-T,a3)))
        # tölt 2,3
        if a2!=0 and a3!=self.M3:
            T = min([a2,self.M3-a3])
            child_node.append(("a2-ből a3-be",(a1,a2-T,a3+T)))
        # tölt 3,1
        if a3!=0 and a1!=self.M1:
            T = min([a3,self.M1-a1])
            child_node.append(("a3-ből a1-be",(a1+T,a2,a3-T)))
        # tölt 3,2
        if a3!=0 and a2!=self.M2:
            T = min([a3,self.M2-a2])
            child_node.append(("a3-ből a2-be",(a1,a2+T,a3-T)))
        '''
        max = (self.M1,self.M2,self.M3)
        for i in range(0,3):
            for j in range(0,3):
                if i != j and condition[i] != 0 and condition[j] != max[j]:
                    T = min([condition[i], max[j] - condition[j]])
                    e = list(condition)
                    e[i] = condition[i]-T
                    e[j] = condition[j]-T
                    e2 = tuple(e)
        return e2

if __name__ == "__main__":
    Korsó = Jug((0,0,8),4)
