#33 – Count Occurrences of Each Word in a Sentence
#Input: "python python is easy"
#Output: {'python': 2, 'is': 1, 'easy': 1}

string = "python python is easy"
str_occ = {}
word =''

lst = [] #string.split()

for ch in string:
    if ch == ' ':
        lst.append(word)
        word = ''
    else:
        if ch not in word:
            word += ch
if word:
    lst.append(word)

for str in lst:
    if str in str_occ:
        str_occ[str] +=1
    else:
        str_occ[str] = 1

print(str_occ)
