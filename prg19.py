#Accept a list of words and return length of longest word. 
list=[]
n=int(input("enter the limit:"))
for i in range(0,n):
    el=input("enter the value:")
list.append(el)
print(list)
long=len(list[0])
str=list[0]
for i in range(1,n):
    if(len(list[i])>long):
        str=list[i]
long=len(str)
print("longest word:",str)
print("length:",long)
