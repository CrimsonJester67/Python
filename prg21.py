n1=int(input("ENter the number of key value pairs in first dictionary:"))
dict1={}
for i in range(n1):
    key=input("Enter key:")
    value=input("Enter value:")
    dict1[key]=value
n2=int(input("Enter the number of key value pairs in second dictionary:"))
dict2={}
for i in range(n2):
    key=input("Enter key:")
    value=input("Enter value:")
    dict2[key]=value 
print(dict1)
print(dict2)
merge_dict=dict1.copy()
merge_dict.update(dict2)
print("Merged dictionary:",merge_dict)