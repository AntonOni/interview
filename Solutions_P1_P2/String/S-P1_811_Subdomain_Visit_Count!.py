import collections


list1 = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]


def solve321():
    res = {}
    for i in list1:
        visits = i.split(" ")
        count = int(visits[0])
        domain = visits[1].split(".")
        for x in range(0, len(domain)):
            key = ".".join(domain[x:])
            if key not in res.keys():
                res[key] = count
            else:
                res[key] += count
    return res

print(solve321())



def subdomainVisits(list1):
    counted = collections.Counter()
    for el in list1:
        emails = el.split(" ")
        count = int(emails[0])
        domain = emails[1].split('.')
        for i in range(0, len(domain)):
            counted[".".join(domain[i:])] += count
    return dict(counted)

# print(subdomainVisits(list1))


def solve():
    domains = []
    for i in list1:
        visits = i.split(" ")
        count = visits[0]
        f_domain = visits[1].split(".")
        for x in range(0, len(f_domain)):
            temp = {}
            key = ".".join(f_domain[x:])
            temp[key] = int(count)
            domains.append(temp)
    print(domains)
    i = 0
    while i < len(domains):
        key_i = list(domains[i].keys())[0]
        x = i + 1
        while x < len(domains):
            key_x = list(domains[x].keys())[0]
            if key_i == key_x:
                domains[i][key_i] += domains[x][key_x]
                domains.pop(x)
            x += 1
        i += 1
    return domains

# print(solve())



