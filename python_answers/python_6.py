def fib(n):
  if n <= 1:
      return n
  else:
      return(fib(n-1) + fib(n-2)) 
size = 20
if size <= 0:
  print("Input should be a positive value")
else:
  print("Fibonacci series:")
for i in range(size):
    print(fib(i))