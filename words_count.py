##18 – Count Words in a Sentence
#Input: "Python is fun"
#Output: 3

def words_counts(str):
    word_count = 0
    word = ""
    for ch in str:
        if ch == ' ':   # Count is incremented on space.
            word_count +=1
            word =""
        else:
            word +=ch
    if word:  # Count is incremented if no space available in end of string
        word_count +=1
    return word_count

str = "Python is fun"
print(words_counts(str))