global binary
binary = list() 
def decToBin(num):
    if num > 1:
        rem = num % 2
        binary.append(rem)
        decToBin(num // 2)
    if num == 1:
        binary.append(1)

   

num = int(input("Enter number to find binary: "))
decToBin(num)
print(binary)
print(binary.reverse())
            

