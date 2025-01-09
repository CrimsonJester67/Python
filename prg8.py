ist=[]
n=int(input('Enter the no of elements:'))
print('Numbers are : \t')
for i in range(0,n):
    number=int(input())
    list.append(number)
print('\n',list)
for i in range(0, n):
    if(list[i]>100):
        list[i]='over'
print(list)