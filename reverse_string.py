##11 – Reverse a String Without Using Slicing
#Input: "hello"
#Output: "olleh"

str = "hello"
lnth = len(str)-1
rev_str = ""
for i in range(lnth,-1,-1):
    rev_str += str[i]

print(rev_str)

