def fact(n): #defining a function for factorial
    if n<0: 
        return "Factorial does not exist for negative numbers."
    elif n==0 or n==1: #base case
        return 1
    return n*fact(n-1) #recursive idea
num=int(input("Enter a number for which you have to find the factorial:="))
print(f"The factorial of {num} is {fact(num)}") #final result given