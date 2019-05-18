


numbers = [7,3,5,6,-7,3,6,7,0,11]

def solve(numbers):
    for i in range(0, len(numbers)):
        slice = numbers[i:]
        min_el = min(slice)
        indx = slice.index(min_el)
        poped_el = numbers.pop(i+indx)
        numbers.insert(i, poped_el)
    return numbers

print(solve(numbers))