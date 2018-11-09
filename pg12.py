# To find area of the circle , triangle, square using lambda functions
print("To find area of circle using lambda functions\n")
r = float(input("Enter the radius of the circle\n"))
area =lambda r: 3.142*r*r
print("The area of the circle is :")
print(area(r))
print("To find the area of triangle using lambda functions\n")
h = float(input("Enter the height\n"))
b= float(input("Enter the base \n"))
tarea = lambda h,b: 0.5*h*b
print("The area of the triangle is:",tarea(h,b))
print("To find the are of squareusing lambdafunctions")
s = float(input("Enter the length of the side"))
sarea = lambda s: s*s
print("THe area of the square",sarea(s))