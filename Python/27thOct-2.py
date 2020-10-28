"""
Program to print binary of all number 1,2,3.....n
"""

n=int(input("Enter the number: "))

print("\nHere are the binaries for all numbers in range [1,n]:")
for number in range(1,n):
    binary=bin(number)
    print(binary[2:],end=", ")
print(bin(n)[2:])