def countFriendsPairings(n):
    dp = [0 for i in range(n + 1)]
    for i in range(n + 1):

        if i <= 2:
            dp[i] = i
        else:
            dp[i] = dp[i - 1] + (i - 1) * dp[i - 2]

    return dp[n]


if __name__ == '__main__':
    t = int(input("Enter number of test cases\n"))

    while t > 0:
        n = int(input("Enter number of friends\n"))
        if 1 <= n < 30:
            print(countFriendsPairings(n))
        t -= 1
#end
