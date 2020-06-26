import itertools
from itertools import combinations, chain
s1 = set()
s2 = set()
s3 = set()
s4 = set()
s = set()

t1 = 0
t2 = 0
t3 = 0
t4 = 0
def findsubsets(s, n):
    return list(map(set, itertools.combinations(s, n)))


test_cases = int(input("Enter test cases \n"))
if 1 <= test_cases <= 10:
    n = int(input("Enter size \n"))
    for i in range(0, n):
        s.add(int(input()))


if __name__ == '__main__':
    s1 = findsubsets(s, n)
    s2 = findsubsets(s, n - 1)
    s3 = findsubsets(s, n - 2)
    s4 = findsubsets(s, n - 3)

    if len(s1) != 0:
        for i in s1:
            if 

    if len(s2) != 0:


    if len(s3) != 0:


    if len(s4) != 0:

# print(f" s1 = {s1} \n s2 = {s2} \n s3 = {s3} \n s4 = {s4} \n")
