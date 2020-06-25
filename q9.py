if __name__ == '__main__':
    def countWays(n, m):
        count = []
        for i in range(n + 2):
            count.append(0)
        count[0] = 0

        for i in range(1, n + 1):
            if i > m:
                count[i] = count[i - 1] + count[i - m]
            elif i < m or i == 1:
                count[i] = 1
            else:
                count[i] = 2
        return count[n]


    ways = []
    test_cases = int(input())
    if 1 <= test_cases <= 1000:
        for i in range(0, test_cases):
            n = int(input())
            m = int(input())
            if 1 <= n <= 100000 and 1 <= m <= 100000:
                ways.append(countWays(n, m))

    print(*ways, sep='\n')
