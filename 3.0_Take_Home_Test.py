'''
HONOR CODE: I solemnly promise that while taking this test I will only use PyCharm or the Internet,
but I will definitely not ask another person except the instructor. Signed: Ezra McCulley
1. Write a line of code that will print your name.
'''
print("Ezra McCulley")

'''
2. Write a program that asks someone for their name and then prints their name to the screen?
'''
Name=input("Name:")
print(Name)
'''
3. Predict the ouput of the following lines of code and then test them? Write down your prediction and the output.
print (17/9) Prediction: 1.8 Output:1.8888888888-
print (17//9) Prediction:1 Output: 1
print (17%9) Prediction: 1.8 Output: 8   Why? Because it finds the remainder
'''

'''
4. Write a a program where a user enters a base and height and you print the area of a triangle.
'''
B=int(input("Base:"))
H=int(input("Height:"))
Area=(B*H)/2
print("Triangle Area:",Area)
'''
5. Change this program so it works.
A=May the Force be with you!
print(a)
'''
A="May the Force be with you!"
print(A)
'''
6. Write a line of code that will ask the user for the length of a square's
side and then print the area of the square
'''
S=int(input("Squares Side Length:"))
S_Area=S*S
print("Area:",S_Area)
'''
7. Ask a user for the length of radii of an ellipse and then print its area. 
Area=pi*a*b where a and b are the lengths of the major radii.
'''
a=int(input("Ellipse Radii height:"))
b=int(input("Ellipse Radii Width:"))
pi=3.14
Ellipse_Area=pi*a*b
print("Ellipse Area",Ellipse_Area)
'''
8. Ask a user for moles, volume and temperature of a gas and print out the pressure. PV=nRT where n is the number of moles, T is the absolute temperature, V is the
volume, and R is the gas constant 8.3144.
'''
moles = n = float(input("Moles: "))
temperature = T = float(input("Temperature: "))
volume = V = float(input("Volume: "))
Gas_Contant = R = 8.3144
Pressure = (n*R*T)/V
print("Pressure:",Pressure)
'''
9. Ask a user for an integer and then print the square root.
'''
a=int(input("Integer:"))
print("Square Root:",a**.5)
'''
10. Good Star Wars joke: "May the mass times acceleration be with you!" because F=ma. Ask the user for mass and acceleration
and then print out the Force on one line and "Get it?" on the next.
'''
Mass=float(input("Mass: "))
acceleration=float(input("Acceleration: "))
Force = Mass * acceleration
print("May the ",Force," be with you")
print("Get it?")