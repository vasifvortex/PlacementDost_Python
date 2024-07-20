#Implement a program to find the factorial of a given number using recursion.
n=5
def rec(n):
  if n == 1:
      return n
  else:
      return n * rec(n-1)
print(rec(n))