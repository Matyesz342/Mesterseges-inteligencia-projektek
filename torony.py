class Tower:
    def __init__(self, start, finish, s):
        self.start = list(start)
        self.finish = list(finish)
        self.s = s

    def finish_test(self, condition):

        return condition == self.finish and len(condition)+1 == self.s

    def __next__(self, sorted_list, new_item):
        sorted_list.append(new_item)
        sorted_list.sort()
        return sorted_list


if __name__ == "__main__":
    items = Tower((6, 7, 3, 2, 8, 5, 4, 1), (1, 2, 3, 4, 5, 6, 7, 8), 1)
    temp = 0
    items.start = list(items.start)
    asc_items = items.start[:temp]
    while not items.finish_test(asc_items):
        new_item = items.start[temp]
        left_items = items.start[items.s:]
        asc_items = items.__next__(asc_items,new_item)
        items.s += 1
        temp += 1
        print("Hozzáadott és rendezett elemek: ", asc_items, left_items, " S: ", items.s)


