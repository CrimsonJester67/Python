str=input('Enter the String:')
search=input('Enter the element to be searched:')
x=str.split(" ")
count=0
for i in str:
    if(i==search):
        count=count+1
print(count)