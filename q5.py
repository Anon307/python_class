def getSum(n):
    
    sum = 0
    for digit in str(n): 
      sum += int(digit)      
    return sum
   
n = 123

if n>99 and n<1000:
    print(getSum(n))
else:
    print("Number is not three digit")