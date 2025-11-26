##7 - Count Vowels and Consonants in a String
#Input: "Hello World"
#Output:
#Vowels = 3
#Consonants = 7

str = "Hello World"

vowels = "aeiou"
Vowels = 0
Consonants = 0

for ch in str:
    if ch in vowels:
        Vowels +=1
    elif ch == ' ':
        pass
    else:
        Consonants +=1

print(f"Vowels = {Vowels} \nConsonants = {Consonants}")