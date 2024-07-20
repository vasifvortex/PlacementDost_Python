s="interesting"
def reverse(s):
    n=""
    for i in range(len(s)):
        n=n+s[len(s)-i-1]
    return n
print(reverse(s))