def selection_sort(arr):

    for i in range(len(arr)-1):
        min_index = i
        print(i)
        for j in range(i+1,len(arr)):
           if arr[min_index] > arr[j]:
               min_index = j
        arr[i],arr[min_index] = arr[min_index],arr[i]
    print(arr)

arr = [72,50,10,44,8,20]
selection_sort(arr=arr)
