##38 – Calculate Power Without Using ** Operator
#Input: 2^5
#Output:
p = 1
n = 2
iter = int(input("Enter num: "))
for i in range(iter):
    p = n * p
print(p)