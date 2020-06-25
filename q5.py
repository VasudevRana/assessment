if __name__ == '__main__':
    test_cases = int(input("Enter number of test cases: \n"))
    results = []
    def string_div(string1, string2):
        string1_1 = string1[:len(string1)//2]
        string1_2 = string1[len(string1)//2:]

        string2_1 = string2[:len(string2) // 2]
        string2_2 = string2[len(string2) // 2:]

        if string1_1 == string2_1 and string1_2 == string2_2 or string1_1 == string2_2 and string1_2 == string2_1:
            results.append("YES")
        else:
            results.append("NO")


    if 1 <= test_cases <= 10:
        for i in range(0, test_cases):
            s1 = input()
            s2 = input()
            if 1 <= len(s1) <= 50000 and 1 <= len(s2) <= 50000:
                string_div(s1, s2)

    print(*results, sep="\n")
