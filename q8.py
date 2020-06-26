import itertools
from itertools import combinations, chain
s1 = set()
s2 = set()
s3 = set()
s4 = set()
s = set()

def findsubsets(s, n):
    return list(map(set, itertools.combinations(s, n)))


test_cases = int(input("Enter test cases \n"))
if 1 <= test_cases <= 10:
    n = int(input("Enter size \n"))
    for i in range(0, n):
        s.add(int(input()))


if __name__ == '__main__':
      s4 = findsubsets(s, n)
      s3 = findsubsets(s, n - 1)
      s2 = findsubsets(s, n - 2)
      s1 = findsubsets(s, n - 3)

print(f" s1 = {s1} \n s2 = {s2} \n s3 = {s3} \n s4 = {s4} \n")
