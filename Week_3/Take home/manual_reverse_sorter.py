def reverse_sorter(the_list: list):
    # return the_list.sort(reverse=True)
    for z in range(len(the_list)):
        x = 0
        while x < (len(the_list) - 1):
            if the_list[x] < the_list[x + 1]:
                the_list[x + 1] = the_list[x]
                the_list[x] = the_list[x + 1]
                x += 1

    return the_list


