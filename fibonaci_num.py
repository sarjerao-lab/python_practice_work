##1
#Write a Python function to find the Nth Fibonacci number
#Input: n = 6
#Output: 8 (0, 1, 1, 2, 3, 5, 8)

def fibonaci_series(n):
    fib_list = [0,1]
    while len(fib_list) <= n:
        fib_list.append(fib_list[-1] + fib_list[-2])

    print(fib_list)
    return fib_list[-1]

num = int(input("Enter number to which generate fib series:"))
print(fibonaci_series(num))