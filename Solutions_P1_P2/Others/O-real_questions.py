

"""
How will you locate the child element ‘Orange’ by CSS selector


< ul id = "fruit" >
    < li > Apple < / li >
    < li > Orange < / li >
    < li > Banana < / li >
< / ul >
"""


# Правой кнопкой на элемент, скопировать Copy > selector
#fruit > ul:nth-child(2) > li



"""
Reverse a string but special characters in the same indexes

"""

abc = "strin@gRe#ve$$se"
#      eseve@Rgn#ir$$ts

def sol():
    chars = []
    lettes = []
    for i in abc:
        if i.isalpha():
            lettes.append(i)
        else:
            indx = abc.index(i)
            chars.append([indx, i])
    lettes.reverse()
    for z in chars:
        lettes.insert(z[0], z[1])
    return "".join(lettes)

print(sol())





"""
Write a method to calculate the number of letters and digits in a string.

Then the output should be:
LETTERS 10
DIGITS 3

"""

srt = "hello world! 123"

def question3():
    d = 0
    l = 0
    for i in srt:
        if i.isdigit():
            d += 1
        elif i.isalpha():
            l += 1
    return d, l

print(question3())


"""
You have file with string with numbers. Find max, min and avg number

"""

def solvr():
    with open("/Users/anton/PycharmProjects/interview/file.txt", "r") as fp:
        content = fp.read()
        n = 0
        s_content = content.split()
        for i in s_content:
            if i.lower() == "error":
                n += 1
    return n

"""
1. Write a function to reverse a sentence. (Just the order of words not the words itself)
for example
input:      "I love Apple"
output: "Apple love I"

"""

inp = "I love Apple"

def solve():
    inp_e = inp.split(" ")
    inp_e.reverse()
    final = " ".join(inp_e)
    return final

print(solve())


"""
Reverse string. Do not create new string. What is the issues with Python 3 strings?
"""
s = "sadaw"

def reverse_str(s):
    list_s = list(s)
    list_s.reverse()
    s = "".join(list_s)
    return s

print(reverse_str(s))


"""
Given a Python list. Return copy of the list.
"""

list1 = [1,2,3,5,"6"]

def return_copy():
    newlist = list1.copy()
    return newlist

print(return_copy())



"""
Given lwo lists return a single list of tuples that is the aggregate of each of the lists
"""
list2 = [1,2,3]
list3 = [9,8,7]

def single_list():
    new_list = []
    for i in range(len(list2)):
        new_list.append((list2[i], list3[i]))
    return new_list

print(single_list())


"""
Given a list that can contain nested lists, return a single list. 
It can contain other objects such as str and int
"""


l = ["a", "b", ["c", "d", ["e", ["f", "g"]]]]

res = []

def recurse_list(l, res):
    for item in l:
        if isinstance(item, list):
            recurse_list(item, res)
        else:
            res.append(item)


recurse_list(l, res)
print(res)


"""
Write a function to count the number of times you see
"aaabbcdddda" to "a3b2c1d4a1"
"""


def zanogo(st):
    res = []
    n = 1
    res.append(st[0])
    for i in range(0, len(st)-1):
        if st[i] == st[i+1]:
            n += 1
        else:
            res.append(str(n))
            res.append(st[i+1])
            n = 1
    res.append(str(n))
    return "".join(res)





