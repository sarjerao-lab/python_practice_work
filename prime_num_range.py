##35 – Find All Prime Numbers Within a Range
#Input: 1 to 20
#Output: [2,3,5,7,11,13,17,19]

prime_range = []

for i in range(2,20):
    prime = True
    for j in range(2,i//2 + 1):
        if i % j == 0:
            prime = False
            break
    if prime:
         prime_range.append(i)       
           
print(prime_range)