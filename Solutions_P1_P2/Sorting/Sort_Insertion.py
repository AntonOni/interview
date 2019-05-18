
arr = [2,3,7,0,5, 1,0,9]

"""
[2,3,7,0,5]
[2,3,7,7,5]
[2,3,3,7,5]
[2,2,3,7,5]
[0,2,3,7,5]
[0,2,3,7,7]
[0,2,3,5,7]
"""


def insertionSort(arr):
    for i in range(0, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

print(insertionSort(arr))





































