# Programa que retorna 1 si la suma de los subarrays puede ser dividida entre si misma, retorna 1 si se puede, -1 si no es posible, y 0 si es vacio el array
def canBeSplitted(arr, n) :
  
    leftSum = 0

    for i in range(0, n) :
        leftSum += arr[i]

        rightSum = 0
        for j in range(i+1, n) :
            rightSum += arr[j]
   
        if (leftSum == rightSum) :
            return i+1
      
    return -1
  
   
def returnResponse(arr) :
  
    Splitted = canBeSplitted(arr, len(arr))

    if len(arr)==0:
        print("0")
   
    if (Splitted == -1 or Splitted == len(arr) ) :
        print ("-1")
        return
      
    for i in range(0, len(arr)) :
        if(Splitted == i) :
            print ("1")
  
arr = [1,3,3,8,4,3,2,3,3]
returnResponse(arr)
