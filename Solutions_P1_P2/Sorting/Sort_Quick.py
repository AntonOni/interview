import random

my_list = [7, 90, -8, 4, 15, 2, 0]


def quick(my_list):
    if len(my_list) <= 1:
        return my_list
    else:
        # random_index = random.randint(0, len(my_list)-1)
        # random_el = my_list[random_index]
        random_el = random.choice(my_list)
        greater = []
        equal = []
        less = []
        for x in my_list:
            if x > random_el:
                greater.append(x)
            if x == random_el:
                equal.append(x)
            if x < random_el:
                less.append(x)
        return quick(less) + equal + quick(greater)



print(quick(my_list))