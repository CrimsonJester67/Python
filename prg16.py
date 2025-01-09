#Find the sum of all items in a list 
list=[]
n=int(input("enter the limit:"))
for i in range(0,n):
    num=int(input("enter the number:"))
list.append(num)
sum=0
for i in range(0,n):
    sum=sum+list[i]
print("sum is",sum)
