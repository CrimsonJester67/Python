#From a list of integers, create a list removing even numbers 
list=[]
n=int(input("Enter the no of elements:"))
print("numbers are:")
for i in range(0,n):
    number=int(input())
    list.append(number)
oddlist=[]
for i in range(0,n):
    if((list[i]%2)!=0):
        oddlist.append(list[i])
print(oddlist)
