#9 – Count Uppercase and Lowercase Letters in a String
#Input: "Hello World"
#Output:
#Uppercase = 2
#Lowercase = 8

str = "Hello World"
uppercase, lowercase = 0, 0

for ch in str:
    if ch.isupper():
        uppercase +=1
    elif ch == ' ':
        pass
    else:
        lowercase +=1

print(f"Uppercase = {uppercase} \nLowercase = {lowercase}")