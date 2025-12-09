##39 – Count Spaces in a String
#Input: "I love Python"
#Output: 

str = "I love Python"
space = 0
for ch in str:
    if ch == " ":
        space +=1
print(space)