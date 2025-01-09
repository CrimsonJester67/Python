#Add ‘ing’ at the end of a given string. If it already ends with ‘ing’, then add ‘ly’ 
str=input("enter a string:")
if(str[-3:]=='ing'):
    str=str+'ly'
else:
    str=str+'ing'
print(str)
