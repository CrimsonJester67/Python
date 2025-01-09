#Find GCD of 2 numbers. 
num1=int(input('enter number1:'))
num2=int(input('enter number2:'))
gcd=1
n=min(num1,num2)+1
for i in range(1,n):
    if((num1%i==0) and (num2%i==0)):
        gcd=i
print("GCD",num1,num2,'is',gcd)
