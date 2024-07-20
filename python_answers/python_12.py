list1=[1,3,4,5,6,7,8,9]
list2=[6,10,7,4,2938,90]
list3=[]
for i in list1:
    for j in list2:
        if(i==j):
            list3.append(i)
print(list3)
