##14 – Factorial of a Number (Without Recursion)
#Input: 5
#Output: 120

def factorial(num):
    if num == 0 or num == 1:
        return 1
    fact = 1
    while num > 1:
        fact = fact * num # fact *= num
        num = num - 1 # num -=1
    return fact

num = int(input("Enter number to calculate the factorial:"))
print(factorial(num))

