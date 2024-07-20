def gen(limit):
    arr=[2,3]
    x=0
    for i in arr:
        print(i)
    while(x<limit):
        x=x+1
        arr.append(6*x-1)
        arr.append(6*x+1)
    return arr
print(gen(15))