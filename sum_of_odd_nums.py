#27 – Sum of All Odd Numbers in a List
#Input: [10,21,33,40]
#Output: 54

lst = [10,21,33,40]
odd_sum = 0
for num in lst:
    if num % 2 != 0:
        odd_sum += num

print(odd_sum)
