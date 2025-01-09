n=int(input("Enter the number of key value pairs in the dictionary:"))
dict={}
for i in range(n):
    key=input("Enter the key:")
    value=input("Enter the value:")
    dict[key]=value
print("The dictonary is:",dict) 
dict_asc=sorted(dict.items(),key=lambda item:item[0])
print("sorted dictinary in ascending order:",dict_asc)
dict_desc=sorted(dict.items(),key=lambda item:item[0],reverse=True)
print("sorted dictinary in descending order:",dict_desc)