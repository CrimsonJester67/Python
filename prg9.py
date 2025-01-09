list=[]
n=int(input('Enter the Limit:'))
for i in range(0,n):
    fname=input('Enter the first name:')
    list.append(fname)
print('Full List',list)
count=0
for name in list:
    count=count+name.count('a')
print('occurance of a:',count)