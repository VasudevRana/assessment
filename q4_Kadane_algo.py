def que_4_kadane_algo():
      ini_test_case = 0
      no_test_cases = int(input("test cases"))

      while ini_test_case < no_test_cases:

            test_list =[]
            ini_list_size = 0
            ini_test_case += 1
            list_size = int(input("list size"))

            while ini_list_size < list_size:

                  list_elements = int(input("list elements"))
                  ini_list_size += 1
                  test_list.append(list_elements)

            def kadane(test_list):
                  maxSoFar = 0
                  maxEndingHere = 0

                  for i in test_list:
                        maxEndingHere = (maxEndingHere +i)
                        maxEndingHere = max(maxEndingHere, 0)
                        maxSoFar = max(maxSoFar, maxEndingHere)

                  return maxSoFar

            if __name__ == '__main__':
                  print("The sum of contiguous subset is", kadane(test_list))

que_4_kadane_algo()
