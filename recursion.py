# ~ Find the amount of a certain number using recursion

# ~ Random List of numbers

lst = [1,3,5,7,9,2,0,3,2,1,4,7,0,2,0,2,0,3,1,6,4,8,7,9,3,1,0]

def get_number_of(list, num):
  if len(list) == 1:
    return 1 if list[0] == num else 0
  if list[0] == num:
    return 1 + get_number_of(list[1:], num)
  else:
    return 0 + get_number_of(list[1:], num)

# ~ Example 

number_of_2 = get_number_of(lst,2)

print(number_of_2)

# ~ Fibonacci numbers with recursion

def fibonacci(n):
  if n == 0:
    return 0
  if n == 1:
    return 1
  return fibonacci(n-1) + fibonacci(n-2)

nth_num = fibonacci(8)

print(nth_num)

# ~ First 25 terms of the fibonacci sequence

for i in range(25):
  print(f"NTH TERM:{i} ==> {fibonacci(i)}")

# ~ Factorial of a number - (in one line)

def factorial(n):
  return n * factorial(n - 1) if n != 1 else n * 1 


print(f"Factorial {factorial(10)}")
