##32 – Sum of Digits of a Number
#Input: 987
#Output: 24

num = input("Enter num to calculate sum of degits: ")
sum = 0

for elm in num:
    sum += int(elm)
print(sum)