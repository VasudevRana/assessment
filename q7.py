def shouldSwap(s, start, curr):
    for i in range(start, curr):
        if s[i] == s[curr]:
            return 0
    return 1

def findPermutations(s, index, n):
    if index >= n:
        print(''.join(s))
        return

    for i in range(index, n):
        check = shouldSwap(string, index, i)
        if check:
            string[index], string[i] = string[i], string[index]
            findPermutations(string, index + 1, n)
            string[index], string[i] = string[i], string[index]


if __name__ == "__main__":
    string = list(input())
    if len(string) <= 8:
        n = len(string)
        findPermutations(string, 0, n)
#end

