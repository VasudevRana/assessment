def maxCrossingSum(arr, l, m, h):
    sm = 0
    left_sum = -10000

    for i in range(m, l - 1, -1):
        sm = sm + arr[i]

        if sm > left_sum:
            left_sum = sm
    sm = 0
    right_sum = -1000

    for i in range(m + 1, h + 1):
        sm = sm + arr[i]

        if sm > right_sum:
            right_sum = sm
    return max(left_sum + right_sum, left_sum, right_sum)

def maxSubArraySum(arr, l, h):
    if l == h:
        return arr[l]
    m = (l + h) // 2
    return max(maxSubArraySum(arr, l, m),
               maxSubArraySum(arr, m + 1, h),
               maxCrossingSum(arr, l, m, h))


if __name__ == '__main__':
    t = int(input("Enter number of test cases \n"))
    for i in range(0, t):
        n = int(input("Enter size of array \n"))
        arr = [None] * n
        max_sum = [None] * n
        print("Enter array")
        for j in range(0, n):
            arr.append(int(input()))
            max_sum[j] = maxSubArraySum(arr, 0, n - 1)
for i in range(0, t):
    print(f"Maximum contiguous sum of array {i + 1} is ", max_sum[i])
