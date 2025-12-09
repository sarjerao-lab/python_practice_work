#31 – Reverse a List Without Using Reverse()
#Input: [1,2,3,4]
#Output: [4,3,2,1]

lst = [1,2,3,4]
rev_lst =[lst[i] for i in range(len(lst)-1, -1, -1) ]

print(rev_lst)

rev_lst = []
for elm in lst[::-1]:
    rev_lst.append(elm)

print(rev_lst)

rev_lst = lst[::-1]
print(rev_lst)