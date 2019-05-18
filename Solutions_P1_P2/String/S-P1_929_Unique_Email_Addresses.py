emails = ["test.email+alex@leetcode.com",
         "test.e.mail+bob.cathy@leetcode.com",
         "testemail+david@lee.tcode.com"]


def solve():
    result = []
    for i in emails:
        email = i.split("@")
        left = email[0]
        right = email[1]
        if "." in left:
            left = left.replace(".", "")
        if "+" in left:
            indx = left.index("+")
            left = left[:indx]
        final = left + "@" + right
        result.append(final)
    return set(result)
print(solve())


