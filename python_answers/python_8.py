a=[1,3,5,6,7,8,9]
def even(a):
    count=0
    sum=0
    for i in a:
        sum +=i
        count=count+1
    return(sum/count)
print(even(a))