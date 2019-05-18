"""
Дан массив чисел. Найти подмассив чисел этого массива с наибольшей суммой
Например:
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""

my_list = nums = [-2,1,-3,4,-1,2,1,-5,4]


# Do you want to return just subarray or subarray with value?



def solve1():
    max_key = ""
    max_val = 0
    for i in range(0, len(my_list)):
        for x in range(i+1, len(my_list)):
            sliced = my_list[i:x]
            sum_sliced = sum(sliced)
            if sum_sliced > max_val:
                max_val = sum_sliced
                max_key = str(sliced)
    return max_val, max_key

print(solve1())








def solve():
    result = []
    for i in range(0, len(my_list)):
        for a in range(i+1, len(my_list)):
            dict_result = {}
            border = my_list[i:a]
            border_sum = sum(border)
            dict_result[str(border)] = border_sum
            result.append(dict_result)
    new_value = 0
    max_key = []
    for i in result:
        list_of_keys = list(i.keys())
        key = list_of_keys[0]
        value = i[key]
        if value > new_value:
            new_value = value
            max_key = key
    return max_key, new_value


print(solve())








