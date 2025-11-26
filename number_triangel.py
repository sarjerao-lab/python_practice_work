##2
#Inverted Pyramid with Numbers
#1 2 3 4 5
#1 2 3 4
#1 2 3
#1 2
#1

def inverted_trangle(num):
    for i in range(1, num+1):
        for j in range(1,num+1):
            print(f"{j} ", end="")    
        print(" ")
        num = num -1
num = int(input("Enter num:"))
inverted_trangle(num)
