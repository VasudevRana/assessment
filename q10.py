import math


def divSum(n):
    result = 0
    for i in range(2,(int)(math.sqrt(n))+1) :
        if n % i == 0 :
            if i == (n/i) :
                result = result + i
            else :
                result = result + (i + n//i)
    return result + n + 1


def maxSum(n):
    if n == 1:
        return 1
    for i in reversed(range(1,n)):
        if n == divSum(i):
            return i
        else:
            return -1


t = int(input("Enter number of test cases \n"))
if __name__ == '__main__':
    while t != 0:
        n = int(input("Enter a positive number \n"))
        if 0 < n <= 10000:
            print(maxSum(n))
        else:
            print(-1)
        t -= 1
