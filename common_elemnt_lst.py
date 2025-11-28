##24 – Find Common Elements Between Two Lists - Date : 28-11-2025
#Input: [1,2,3], [3,4,5]
#Output: [3]

lst1, lst2 = [1,2,3], [3,4,5]
common = []
for elm in lst1:
    if elm in lst2:
        common.append(elm)

print(common)