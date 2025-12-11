#Question:
#Write a Python program to count the frequency of each word in a given sentence using a dictionary.
#Example Input:
#"apple banana apple orange banana apple"
#Expected Output:
#{'apple': 3, 'banana': 2, 'orange': 1}

str = "apple banana apple orange banana apple"

str_freq_count = {s: str.count(s) for s in str.split()}
print(str_freq_count)

