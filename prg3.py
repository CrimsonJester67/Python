#First and last character exchange in a string 
str=input('Enter a string:')
f=str[0] 
l=str[-1]
str=l+str[1:-1]+f
print('New string is:',str)
