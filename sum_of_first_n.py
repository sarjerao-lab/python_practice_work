##13 – Print Sum of First N Natural Numbers
#Input: n = 10
#Output: 55

def Sum_Of_First_N(num):
    sum = 0
    for i in range(num+1):
        sum += i

    return sum

num = int(input("Enter the number:"))
print(Sum_Of_First_N(num))
