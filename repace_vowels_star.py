##40 – Replace All Vowels With ‘*’
#Input: "Hello World"
#Output: "H*ll* W*rld"

str = "Hello World"
vowels = "aeiouAEIOU"
str_replace = ""
for ch in str:
    if ch in vowels:
        str_replace += "*"
    else:
        str_replace += ch
print(str_replace)