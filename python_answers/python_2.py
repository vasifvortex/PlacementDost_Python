i=2
j=[]
a=6
def check_prime(a,i,j):
    b=a
    while i*i<=a:
        if a % i == 0:         
            j.append(i)         
            a = a // i     
        else:         
            i+=1 
    if j == []:
        print(str(b)+" is a prime number.")
    else:
        print(str(b)+" is not a prime number.")
print(check_prime(a,i,j))