##36 – Check if Two Strings are Anagram
#Input: "listen", "silent"
#Output: Anagram

str1 = input("Enter string 1:")
str2 = input("Enter the string 2:")

anagram_string = sorted(str1) == sorted(str2)

print(anagram_string)