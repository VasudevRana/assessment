no_test_case = 1
test_case_len = 4
test_list =[]

for k in range(4):
      list_elements= int(input("list elements "))
      test_list.append(list_elements)

def set(s):
      list1 =[]
      x = len(s)
      for i in range(1 << x):
            list1.append([s[j] for j in range(x) if (i & (1 << j))])
      print(list1)

      for subset in list1:

            if sum(subset) == 0:
                  return True

            elif len(subset) ==0 or len(subset) ==1:
                  return False 
            
            else:
                  continue
                       
print(set(test_list))
