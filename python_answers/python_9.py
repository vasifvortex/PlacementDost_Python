n = str(input())
if n[:int(len(n)/2)] == n[-int(len(n)/2):][::-1]:
    print("it is a palindrome")
else:
    print("it is not a palindrome")