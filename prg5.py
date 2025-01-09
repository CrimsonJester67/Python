ist=[]
n=int(input('Enter the no of elements:'))
print('Elements are:')
for i in range (0,n):
    element=int(input())
    list.append(element)
print('Positive Numbers are:')
for i in range(0,n):
    if(list[i]>=0):
        print(list[i])