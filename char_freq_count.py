##6 - Count the Frequency of Each Character in a String (Using Dictionary)
#Input: "programming"
#Output:
#{'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 1, 'n': 1}

str =  "programming"
#Dictionary comprehension
char_freq = {ch : str.count(ch) for ch in str}
print(char_freq)

# using regular for loop
char_freq ={}
for ch in str:
    if ch in char_freq:
        char_freq[ch] +=1
    else:
        char_freq[ch] = 1

print(char_freq)