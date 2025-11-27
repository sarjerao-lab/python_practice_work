##16 – Check if a Number is Armstrong
#Input: 153
#Output: Armstrong Number (1^3 + 5^3 + 3^3) and power of 3 is number of digits in Input

def armstrong(num):
    l = len(str(num))
    temp = num
    add_dig = 0
    for num in str(num):
        add_dig = add_dig + int(num) **l

    if temp == add_dig:
        return "Armstrong Number"

num = 153
print(armstrong(num))