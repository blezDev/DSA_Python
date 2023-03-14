items = [10,20,30,40,50,60,70]
t = 10
def binary_search(items,left,right,x):
    if right >= left :
      mid = int((left + right)/2)
      if items[mid] == x:
            return mid

      elif(items[mid] > x):
       return binary_search(left= left,items=items,right=mid -1,x=x)
      
      else : 
          return binary_search(items =items,left=mid +1,right=right,x=x)
    
    
      
          
    else:
        return -1

result =binary_search(items,0,len(items) -1, t)

if result == -1:
    print("Not able to find {} value in the array".format(t))
else:
    print("Found {} on index {}".format(t,result))



