##21 – Remove Duplicates from a List - Date 28-11-2025
#Input: [1,2,3,2,4,1]
#Output: [1,2,3,4]

lst = [1,2,3,2,4,1]
unique_lst = []

for elm in lst:
    if elm not in unique_lst:
        unique_lst.append(elm)

print(unique_lst)

dup_lst = [elm for elm in lst if lst.count(elm) > 1]
print(dup_lst)
unq_lst  = [elm for elm in lst if lst.count(elm) == 1]
print(unique_lst)