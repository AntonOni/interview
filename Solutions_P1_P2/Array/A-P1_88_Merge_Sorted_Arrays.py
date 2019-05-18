"""
Даны 2 отсортированных массива. Сделать медж двух массивов в один отсортированный.
Расширить первый массив на число элементов второго массива.
Например:
Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
"""


nums1 = [1,9,13,30, 40, 99, 100, 101, 102, 109]
nums2 = [3,6,7, 9, 19]
m = 4
n = 3

# Is lists sorted?
# Do you want keep result in function or global rewrite?
# What list you want to rewrite?
# How many symbols you want to take from first and second list?



def solve2():
    global nums1
    nums1 = nums1[:m] + nums2[:n]
    for z in range(0, len(nums1)):
        slice = nums1[z:]
        min_el = min(slice)
        index_min_el = slice.index(min_el)
        poped_el = nums1.pop(z + index_min_el)
        nums1.insert(z, poped_el)

# solve2()
# print(nums1)





def solve1():
    """
    arr[:] returns arr (alist[:] returns a copy of a list).
    arr[:]=arr2 performs an inplace replacement;
    changing the values of arr to the values of arr2.
    The values of arr2 will be broadcasted and copied as needed.
    """
    nums1[:] = sorted(nums1[:m] + nums2[:n])

# solve1()
# print(nums1)











def solve2():
    global nums1
    if len(nums1) < (m + n):
        nums1 = nums1 + [0] * ((m + n) - len(nums1))
    for i in range(0, n):
        nums1[m+i] = nums2[i]
    for z in range(0, len(nums1)):
        slice = nums1[z:]
        min_el = min(slice)
        index_min_el = slice.index(min_el)
        poped_el = nums1.pop(z + index_min_el)
        nums1.insert(z, poped_el)



# solve2()
# print(nums1)












