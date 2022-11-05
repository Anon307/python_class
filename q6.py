def reverse(num):
    
    reversed_num = 0

    while num != 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10

    print("Reversed Number: " + str(reversed_num))
   
n = 123

if n>99 and n<1000:
    reverse()
else:
    print("Number is not three digit")