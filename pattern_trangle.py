###3
#Enter the row size for the pattern: 5
#        *
#      * * *
#    * * * * *
#   * * * * * * *
#* * * * * * * * *

def print_pattern(num):
    for i in range(0, num):
        for j in range(0,num+2):
            print("  ", end="")
        for j in range(0,2*i+1):
            print("*", end=" ")
        num = num -1
        print()

num = int(input("Enter number:"))
print_pattern(num)