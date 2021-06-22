
    arr = [10,15,34,26,67,11]
    def function(arr): 
     ...:     n = len(arr) 
        ...:     for i in range(n): 
        ...:         for j in range(0, n-i-1): 
        ...:             if arr[j] > arr[j+1] : 
        ...:                 arr[j], arr[j+1] = arr[j+1], arr[j] 
        ...:   
        ...: return arr 
    print(function(arr))
