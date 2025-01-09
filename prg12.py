list_1=input("Enter the first list of integers(seperated by comma):")
list1=[int(x) for x in list_1.split(',')]
list_2=input("Enter the second list of integers(seperated by comma):")
list2=[int(x) for x in list_2.split(',')]
if len(list1)==len(list2):
    print("The lists are same length",len(list1))
else:
    print("The list are not same length")
print("The sum of elements of list1:",sum(list1))
print("The sum of elements of list2:",sum(list2))
if sum(list1)==sum(list2):
    print("The sums of list are same")
else:
    print("The sums of lists are not same")
common=[]
for value in list1:
    if value in list2:
        common.append(value)
if common:
    print("The common value in both list:",common)
else:
    print("No common value found in both list")