def que_4_div_conq():
      initial_test_case = 0
      no_test_cases = int(input("test cases"))

      while initial_test_case < no_test_cases:

            arr =[]
            ini_list_size = 0

            initial_test_case += 1
            list_size = int(input("list size"))

            while ini_list_size < list_size:
                  list_elements = int(input("list elements"))

                  ini_list_size += 1
                  arr.append(list_elements)

            def maxCrossingSum(arr, l,
                               m, h) : 
                     
                    sm = 0; left_sum = -10000
                    for i in range(m, l-1, -1) : 
                            sm = sm + arr[i] 
                            
                            if (sm > left_sum) : 
                                    left_sum = sm
                                    
                    sm = 0; right_sum = -1000
                    for i in range(m + 1, h + 1) : 
                            sm = sm + arr[i] 
                            
                            if (sm > right_sum) : 
                                    right_sum = sm 
                    
                    return max(left_sum + right_sum, left_sum, right_sum) 

            def maxSubArraySum(arr, l, h) : 
                     
                    if (l == h) : 
                            return arr[l] 
                    m = (l + h) // 2

                    return max(maxSubArraySum(arr, l, m), 
                                    maxSubArraySum(arr, m+1, h), 
                                    maxCrossingSum(arr, l, m, h)) 
                                     
            n = len(arr)
            max_sum = maxSubArraySum(arr, 0, n-1) 
            print("Maximum contiguous sum is ", max_sum) 

que_4_div_conq()
# end
