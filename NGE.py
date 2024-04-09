def find_next_greater_element(arr):
    nge_dict = {} 
    stack = [] 
    for num in arr[::-1]:
        while stack and stack[-1] <= num:
            stack.pop()
        
        if not stack:
            nge_dict[num] = -1
        else:
            nge_dict[num] = stack[-1]
        
        stack.append(num)
    
    nge_list = [nge_dict[num] for num in arr]
    
    return nge_list

arr = [2, 7, 3, 5, 4, 6, 8]
result = find_next_greater_element(arr)

for i in range(len(arr)):
    print(arr[i], "-->", result[i])
