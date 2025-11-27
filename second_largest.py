##20 – Find the Second Largest Number in a List(without using any build in function))
#Input: [10, 40, 20, 50]
#Output: 40

lst = [10, 40, 20, 50]
len = len(lst)

for i in range(len):
    for j in range(0, len-i-1):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]
print(f"Second largest element is: {lst[-2]}")