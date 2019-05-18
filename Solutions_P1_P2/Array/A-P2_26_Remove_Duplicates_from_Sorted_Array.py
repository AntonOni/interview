"""
Given nums = [0,0,1,1,1,2,2,3,3,4]
Remove duplicates from array

"""

nums = [0,0,1,1,1,2,2,3,3,4,0]




def sol():
    n = 0
    while n < len(nums):
        poped = nums.pop(n)
        if poped not in nums:
            nums.insert(n, poped)
            n += 1
    return nums

print(sol())




# def solve2(num):
#     n = 0
#     while n < len(num)-1:
#         if num[n] == num[n+1]:
#             num.pop(n)
#         else:
#             n += 1
#         # print(i, len(num)-1, num)


# solve2(nums)
# print(nums)



