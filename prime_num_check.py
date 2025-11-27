##12 – Check if a Number is Prime
#Input: 17
#Output: Prime

def prime_num_check(num):
    for i in range(2, num //2):
        if num % i  == 0:
            return None
    return "Prime" 
        
num = int(input("Enter number to check whether it is prime or not:"))
print(prime_num_check(num))
