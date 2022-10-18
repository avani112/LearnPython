def linear_Search(lis, n, key):   
    for i in range(0, n):  
        if (lis[i] == key):  
            return i  
    return -1  
  
  
lis = [1 ,3, 5, 4, 7, 9]  
key = 7  
  
n = len(lis)  
res = linear_Search(lis, n, key)  
if(res == -1):  
    print("Element not found")  
else:  
    print("Element found at index: ", res)  
