#30 – Check Perfect Number - Date : 28-11-2025
#Input: 28
#Output: Perfect Number

num = 28
sum = 0

for i in range(1,num):
    if num % i == 0:
        sum += i

if sum == num:
    print("Perfect Number")