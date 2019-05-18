"""
Дан список курса чего либо. Можно совершить только одну сделку. Найти максимальную профит от сделки.
Покупаем в один день и продаем в другой.
Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""


my_list = [7,1,5,3,6,4]

def solve():
    min_price = min(my_list)
    min_price_index = my_list.index(min_price)
    new_list = my_list[min_price_index:]
    max_price = max(new_list)
    result = max_price - min_price
    return result

# print(solve())

def solve_1():
    res = []
    for i in range(0, len(my_list)):
        deal_1 = my_list[i]
        for x in range(i+1, len(my_list)):
            deal_2 = my_list[x]
            deal = deal_2 - deal_1
            res.append(deal)
    return max(res)


print(solve_1())


