def factorial(n):
    if(n==0):
        return 1
    if(n==1):
        return 1
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact 
num=(int(input("enter a number :")))
fact=factorial(num)
print("factorial is ",fact)