from random import *


# for flipping variables
def flip(flip_index_f, variables_dict_f, copy_variables_dict_f):
    if (flip_index_f > 1):
        variables_dict_f[(flip_index_f - 1)] = copy_variables_dict_f[(flip_index_f - 1)]
    if variables_dict_f[flip_index_f] == {0}:
        variables_dict_f[flip_index_f] = {1}
    elif variables_dict_f[flip_index_f] == {1}:
        variables_dict_f[flip_index_f] = {0}
    flip_index_f += 1
    return flip_index_f


def max_SAT(val_list_f, variables_dict_f, Mylist_f, temp_list_f, temp_val_f):
    # flip(f_index_f, variables_dict_f, copy_variables_dict_f)
    local_max_f = 0
    local_or_f = 0
    for k in range(len(Mylist_f)):
        if (Mylist_f[k]) != 0:
            temp_list_f.append(list(variables_dict_f[(abs(Mylist_f[k]))]))
        elif Mylist_f[k] == 0:
            temp_list_f.append(list(temp_val_f))
    for k in range(0, len(temp_list_f)):
        val_list_f += temp_list_f[k]
    for k in range(len(Mylist_f)):
        if Mylist_f[k] < 0:
            if val_list_f[k] == 0:
                val_list_f[k] = 1
            else:
                val_list_f[k] = 0
    for k in range(len(Mylist_f)):
        if Mylist_f[k] != 0:
            local_or_f = local_or_f | val_list_f[k]
        elif Mylist_f[k] == 0:
            if local_or_f == 1:
                local_max_f = local_max_f + 1
            local_or_f = 0
    return local_max_f


def main():
    final_dict = {}
    final_dict_res = {}
    temp_list = []
    temp_val = []
    sat_counter = 0
    global_max = 0
    final_res = 0
    local_max = 0
    local_or = 0
    f_index = 1  # for controlling flip
    #file = open("max-sat-20-80.txt", "r")
    file = open("max-sat-20-90.txt", "r")
    c = file.read()
    c = c.replace("\n", " ")
    # print(c[0])
    Mylist = c.split(" ")
    for i in Mylist:
        if i == '':
            Mylist.remove(i)
    NumberOfVar = Mylist.pop(0)
    NumberOfCl = Mylist.pop(0)
    # print(NumberOfVar)
    # print(NumberOfCl)
    for i in range(0, len(Mylist)):
        Mylist[i] = int(Mylist[i])
    val_list = []
    variables_dict = {}
    copy_variables_dict = {}
    # random restart ****************************************
    for j in range(29):
        f_index = 1
        global_max = 0
        local_max = 0
        local_or = 0
        variables_dict.clear()
        copy_variables_dict.clear()
        temp_list.clear()
        temp_val.clear()
        val_list.clear()
        for i in range(0, int(NumberOfVar)):
            variables_dict[i + 1] = {randint(0, 1)}
        copy_variables_dict = variables_dict
        temp_val.append(2)
        for i in range(len(Mylist)):
            if (Mylist[i]) != 0:
                temp_list.append(list(variables_dict[(abs(Mylist[i]))]))
            elif Mylist[i] == 0:
                temp_list.append(list(temp_val))
        for i in range(0, len(temp_list)):
            val_list += temp_list[i]
        for i1 in range(0, len(Mylist)):
            if Mylist[i1] < 0:
                if val_list[i1] == 0:
                    val_list[i1] = 1
                else:
                    val_list[i1] = 0
        for i3 in range(0, len(Mylist)):
            if Mylist[i3] != 0:
                local_or = local_or | val_list[i3]
            elif Mylist[i3] == 0:
                if local_or == 1:
                    local_max = local_max + 1
                local_or = 0
        if local_max > global_max:
            global_max = local_max
            final_dict = variables_dict
        # ***************************
        for c in range(int(NumberOfVar)):
            f_index = flip(f_index, variables_dict, copy_variables_dict)
            local_max = max_SAT(val_list, variables_dict, Mylist, temp_list, temp_val)
            if local_max > global_max:
                global_max = local_max
                final_dict = variables_dict
                # print(global_max)
        if global_max > final_res:
            final_res = global_max
            final_dict_res = final_dict
    print(final_res)
    for l in final_dict_res:
        print(final_dict_res[l])


main()
