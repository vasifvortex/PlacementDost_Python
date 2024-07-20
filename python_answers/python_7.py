a=[1,3,5,6,7,8,9]
def even(a):
    b=[]
    for i in a:
        if i%2 == 0:
            b.append(i)
    return(b)
print(even(a))