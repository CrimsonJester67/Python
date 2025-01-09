#Read two list ,print out all colors from colorlist1 not contained in colorlist2 
list1=[]
list2=[]
n=int(input("enter the no.of colours in list 1:"))
print("colours are:")
for i in range(0,n):
    color=input()
    list1.append(color)
n=int(input("enter the no.of colours in list 2:"))
print("colours are:")
for i in range(0,n):
    color=input()
    list2.append(color)
set1=set(list1)
set2=set(list2)
print("Orginal set are:\n",list1,"\n",list2)
print("Colour difference:",set1-set2)
