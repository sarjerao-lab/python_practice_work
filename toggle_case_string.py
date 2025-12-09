##34 – Convert a String to Toggle Case
#Input: "PyThOn"
#Output: "pYtHoN"

str = "PyThOn"
toggle_case =''

for ch in str:
    if  ch >= 'A' and ch <= 'Z':
        toggle_case += ch.lower()
    else:
        toggle_case += ch.upper()

print(toggle_case)
        
        
