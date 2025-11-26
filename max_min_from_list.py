##4 – Find Maximum and Minimum Without Using max() or min()
#Input: [12, 45, 2, 67, 33, 89, 1]
#Output: Maximum = 89, Minimum = 1

lst = [12, 45, 2, 67, 33, 89, 1]
max = lst[0]
min = lst[0]

for elm in lst[1:]:
    if elm > max:
        max = elm
    if min > elm:
        min = elm

print(f"Maximum= {max}, Minimum= {min}")

