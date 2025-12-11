#Question:
#Write a Python program that extracts all valid email addresses from a string using a regular expression, and then store them as keys in a dictionary.
#The value for each key should be the domain name (part after @).
#Example Input:
#text = "Contact us at support@example.com or sales@company.org for more info."
#Expected Output:
#{'support@example.com': 'example.com', 'sales@company.org': 'company.org'}

import re

text = "Contact us at support@example.com or sales@company.org for more info."

email = re.findall(r'\S+@\S+', text)
domain = {}
#print(email)
for mail in email:
   domain[mail] = mail.split('@')[1]
print(domain)






