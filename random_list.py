#10
#Create a list of 10 random integers between 0 and 100 From that list, generate three separate new lists:
#Numbers divisible by 3
#Numbers divisible by 7
#Numbers divisible by 9
#Print all four lists
#O/P
#Original List: [12, 7, 45, 18, 21, 33, 49, 90, 5, 27]
#Divisible by 3: [12, 45, 18, 21, 33, 90, 27]
#Divisible by 7: [7, 21, 49]
#Divisible by 9: [18, 90, 27]

import random

#lst = []
#for num in range(15):
#    lst.append(random.randint(1,100))#

div_by_3, div_by_7, div_by_9 = [],[],[]
lst = [12, 7, 45, 18, 21, 33, 49, 90, 5, 27]

for num in lst:
    if num % 3 == 0:
        div_by_3.append(num)
    if num % 7 == 0:
        div_by_7.append(num)
    if num % 9 == 0:
        div_by_9.append(num)

print(f"Divisible by 3: {div_by_3}\nDivisible by 7: {div_by_7}\nDivisible by 9: {div_by_9}")