#17 – Find Even and Odd Numbers in a List
#Input: [1,2,3,4,5,6]
#Output:
#Even = [2,4,6]
#Odd = [1,3,5]

def even_odd_find(lst):
    even_lst = []
    odd_lst = []
    for elm in lst:
        if elm % 2 == 0:
            even_lst.append(elm)
        else:
            odd_lst.append(elm)
    print(f"Even = {even_lst}\nOdd = {odd_lst}")

lst = [num for num in range(1,10)]
even_odd_find(lst)