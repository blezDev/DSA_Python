def quick_sort(array,low,high):
    n = len(arr)
    if low < high:
        pi = partition(array, low, high)
  
        # Recursive call on the left of pivot
        quick_sort(array, low, pi - 1)
  
        # Recursive call on the right of pivot
        quick_sort(array, pi + 1, high)
    else:
       pass

def partition(array, low, high):
  
    
    pivot = array[high]
  
   
    i = low - 1
  
   
    for j in range(low, high):
        if array[j] <= pivot:
            
            i = i + 1
  
           
            (array[i], array[j]) = (array[j], array[i])
  
 
    (array[i + 1], array[high]) = (array[high], array[i + 1])
  
   
    return i + 1
  


arr = [10,20,9,3,5,12,48,50,2]