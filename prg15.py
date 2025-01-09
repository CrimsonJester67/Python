n=int(input("enter a number:"))
print("factors of",n,"are:")
for i in range(1,n):
    if(n%i==0):
        print(i)