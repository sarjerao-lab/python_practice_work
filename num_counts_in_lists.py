#15 – Count Positive, Negative, and Zero Values in a List
#Input: [2, -4, 6, 0, -3, 0]
#Output:
#Positive = 2
#Negative = 2
#Zeros = 2

lst = [2, -4, 6, 0, -3, 0]
positive, negative, zeros = 0,0,0
for num in lst:
    if num == 0:
        zeros += 1 # zeros = zeros + 1
    elif num < 0:
        negative += 1 # negative = negative + 1
    else:
        positive += 1 # positive = positve + 1

print(f"Positive = {positive}\nNegative = {negative}\nZeros = {zeros}")