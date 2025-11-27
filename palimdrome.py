##19 – Check Palindrome String
#Input: "madam"
#Output: Palindrome

def check_palimdrome(str):
    if str == str[::-1]:
        return "Palindrome"
    
str = input("Enter string to check Palindrome:")
print(check_palimdrome(str))