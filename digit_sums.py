#8 - Sum of Digits for Each Number in a List
#Input: numbers = [123, 45, 908]
#Output: Sum List = [6, 9, 17]
#(Explanation: 1+2+3 = 6, 4+5 = 9, 9+0+8 = 17)

lst = [123, 45, 908]
digit_sum =[]
for digit in lst:
    dig_sum = 0
    for dig in str(digit):
        dig_sum += int(dig)
    digit_sum.append(dig_sum)

print(digit_sum)