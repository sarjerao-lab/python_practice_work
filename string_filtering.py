'''Given a text, find all words that start with a capital letter 
and create a dictionary where keys are the capitalized words and values are their count of occurrences.
Ignore punctuation and case sensitivity.
Example Input:
text = "Alice met Bob . Alice and Bob went to Paris. Bob liked Paris."
Expected Output:
{'Alice': 2, 'Bob': 3, 'Paris': 2}'''

import re

text = "Alice met Bob . Alice and Bob went to Paris. Bob liked Paris."
output ={}
lst = text.split()
#Normal method
for elm in lst:
    if elm.istitle():
        elm = elm.strip('.')
        if elm in output:
            output[elm] += 1
        else:
            output[elm] = 1
print(output)
#RegEx method
output ={}
for elm in lst:
    match = re.search(r"[A-Z]",elm)
    if match:
        elm = elm.strip('.')
        if elm in output:
            output[elm] += 1
        else:
            output[elm] =1
    
print(output)