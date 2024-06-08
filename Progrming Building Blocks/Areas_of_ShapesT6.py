# Team 9 Author:  Jenny Larsen
#File: AreasofShapesT6.py
#Objective:  Write a program to compute the areas of three different shapes.
#Prompt for the necessary information, then compute and display the area
#Make sure that your program can appropriately handle decimal values as well as whole numbers.


# Square leng: the formula of the perimeter of a square = 4 × (length of any one side).
square=int(input('What is the length of a side of the square? ' ))
print('The area of the square is:', 4 * square)

#rectangle formula length ✕ width
length=int(input('What is the length of rectangle? ' ))
width= int(input('What is the width of the rectangle? '))

print('The area of the rectangle is:',length * width )

#are circle formula: A = π r²   (pi=3,141592)
circle=int(input('What is the radius of the circle? '))
print("The area of the circle is:", 3,141592 * (circle **2) )