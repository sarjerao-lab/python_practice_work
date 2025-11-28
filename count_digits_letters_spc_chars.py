##23 – Count Digits, Letters, and Special Characters - Date: 28-11-2025
#Input: "Hello@123"
#Output:
#Digits = 3
#Letters = 5
#Special = 1

str = "Hello@!123"
letters, digits, special = 0, 0, 0
for elm in str:
    if "A" <= elm <= "z":
        letters +=1
    elif "0" <= elm <="9":
        digits += 1
    else:
        special += 1

print(f"Letters = {letters}\nDigits = {digits}\nSpecial = {special}")