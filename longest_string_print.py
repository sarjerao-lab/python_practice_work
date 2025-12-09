##28 – Find the Largest Word in a Sentence  - Date: 28-11-2025
#Input: "Python programming language"
#Output: "programming"

str = "Python programming language"

str_count = {word : len(word) for word in str.split()}
print(str_count.get())

str_lst = str.split()
longest_string =''

for strng in str_lst:
    if len(strng) > len(longest_string):
        longest_string = strng

print(longest_string)