from random import *


def flip_item_list(item_list_f, flip_index, tabu_list, NumberOfItems_f):
    if tabu_list[flip_index] == 0:
        if item_list_f[flip_index] == 0:
            item_list_f[flip_index] = 1
        elif item_list_f[flip_index] == 1:
            item_list_f[flip_index] = 0
        for k in range(0, NumberOfItems_f):
            if tabu_list[k] != 0:
                tabu_list[k] -= 1
        tabu_list[flip_index] = 5
    return flip_index, item_list_f, tabu_list


def main():
    item_dict = {}
    item_list = []
    tabu_list = []
    neighbor_list = []
    neighbor_max_v = 0
    neighbor_max_w = 0
    final_list = []
    local_max_V = 0
    global_max_value = 0
    local_max_w = 0
    global_max_w = 0
    flip_index = 0
    j = 0
    file = open("knapsack-20.txt", "r")
    # file = open("knapsack-100.txt", "r")
    c = file.read()
    c = c.replace("\n", " ")
    Mylist = c.split(" ")
    for i in Mylist:
        if i == '':
            Mylist.remove(i)
    NumberOfItems = int(Mylist.pop(0))
    totalW = int(Mylist.pop(0))
    i = 0
    while j < NumberOfItems:  # value weight
        item_dict[j] = [int(Mylist[i]), int(Mylist[i + 1])]
        i += 2
        j += 1
    # print(item_dict)
    Mylist.clear()
    for k in range(0, NumberOfItems):
        item_list.append(randint(0, 1))  # initial state
        tabu_list.append(0)
        neighbor_list.append(0)
    copy_item_list = item_list
    for k in range(0, NumberOfItems):
        temp = local_max_w + item_dict[k][1]
        if temp <= totalW:
            local_max_w = local_max_w + item_dict[k][1]
            local_max_V = local_max_V + item_dict[k][0]
    global_max_value = local_max_V
    global_max_w = local_max_w
    # print(local_max_V)
    # print(local_max_w)
    # print(item_list)
    # print(tabu_list)
    for counter in range(2000):
        for w in range(0, NumberOfItems):
            flip_index = w
            pre = item_list[flip_index]
            item_list = list(copy_item_list)
            flip_index, item_list, tabu_list = flip_item_list(item_list, flip_index, tabu_list, NumberOfItems)
            # flip_item_list(item_dict, tabu_list, item_list, neighbor_list, totalW, NumberOfItems)
            after = item_list[flip_index]
            # print(pre)
            # print(after)
            # print("*********")
            if pre == 1 and after == 0:
                local_max_w = local_max_w - item_dict[flip_index][1]
                local_max_V = local_max_V - item_dict[flip_index][0]
                if local_max_V > neighbor_max_v:
                    neighbor_max_v = local_max_V
                    neighbor_max_w = local_max_w
                    neighbor_list = list(item_list)
            if pre == 0 and after == 1:
                temp = local_max_w + item_dict[flip_index][1]
                if temp <= totalW:
                    local_max_w = local_max_w + item_dict[flip_index][1]
                    local_max_V = local_max_V + item_dict[flip_index][0]
                    if local_max_V > neighbor_max_v:
                        neighbor_max_v = local_max_V
                        neighbor_max_w = local_max_w
                        neighbor_list = list(item_list)
        global_max_value = neighbor_max_v
        global_max_w = neighbor_max_w
        copy_item_list = list(neighbor_list)
    print(global_max_value)
    print(global_max_w)
    for x in range(NumberOfItems):
        print(neighbor_list[x])


main()
