list=[]
n=int(input('Enter the no of elements:'))
print('Elements are:')
for i in range (0,n):
    element=int(input())
    list.append(element)
print('sqaure of elements:')
for i in range(0,n):
    print(list[i]**2)
