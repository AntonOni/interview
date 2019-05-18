



nums = [1,2,3,4,5,6,7]
k = 3


def rotate_right():
    global nums
    n = 0
    while n < k:
        last_e = nums[-1]
        for i in range(len(nums)-1, 0, -1):
            nums[i] = nums[i-1]
        n += 1
        nums[0] = last_e

rotate_right()
print(nums)

def rotate_left():
    global nums
    n = 0
    while n < k:
        firs_e = nums[0]
        for i in range(0, len(nums)-1):
            nums[i] = nums[i+1]
        n += 1
        nums[-1] = firs_e


# rotate_left()
# print(nums)





