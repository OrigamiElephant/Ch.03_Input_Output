'''
TRAPEZOID PROGRAM
-------------------
Create a new program that will ask the user for the information needed to find the area of a trapezoid, and then print the area.

Test with the following:

base 1: 2       base 2: 3    height: 4    area: 10
base 1: 5       base 2: 7    height: 2    area: 12
base 1: 1       base 2: 2    height: 3    area: 4.5
base 1: 7       base 2: 2    height: 4    area: 14
'''
b1=int(input("Enter base 1 length:"))
b2=int(input("Enter base 2 length:"))
h=int(input("Enter height:"))
a=(b1+b2)/2*h
print(a)