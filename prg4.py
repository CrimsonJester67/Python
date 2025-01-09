#From a List of colors ,display first and last color 
list=[] 
n=int(input("enter no element:"))
for i in range(0,n):
    element=input('enter the color:')
    list.append(element)
print('full list:',list) 
print('firstelement:',list[0])
print('lastelement:',list[1])
