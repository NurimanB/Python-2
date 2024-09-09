import math

#TASK 1
print(10//3) #it divides without a remainder
print(10/3) #simple division with remainder

#TASK 2
print(10**3) #degree of number

#TASK 3
x=1
for i in range(4):
    x+=2
    print (x) #+=n add n number to the previous vwlue changinh it

#TASK 4
print(float(1)) #prints float number

#TASK 5
print(bool("False")) #returns true becase the argument is correct

#TASK 6
print(bool(False)) 

#TASK 7
res = 10 == "10" #the statement is False because == checks if the values and types are same
print(res)

#TASK 8
print("bag" > "apple")

#TASK 9
print(not(True or False))

#TASK 10
age = 18
if 18<=age<65:
   print(True)

#TASK 11
for i in range(1,10,2):
   print(i)

#TASK 12
#list, dictionary, tuple    

#task 1 
#py --version

#task 2
'''x = int(input("a side: "))
y = x*2
print(x*y)'''

#task 3
'''full_name = input("Enter full name: ")
x = full_name.split( )
x.reverse()
print(x)'''

#task 4
num = ("1,2,3,4,4,5,6,7,87")
x = num.split(",")
print(x)

#task 5
row = [1, 3, 5, 6, 8, 9]
print(row[0])
print(row[-1])

#task 6
'''n = int(input("enter a number: "))
print(n+n**2+n**3)'''

#task 7
r = 8
pi = 3.14
V = 3/4*pi*r**3
print(V)

#task 8
'''num = int(input("enter a number: "))
if 100 < num < 1000:
   print("The number is within 100 and 1000")
elif 1000 < num < 2000:
   print("The number is within 1000 and 2000")
else: 
   print("The number is not within")'''

#task 9
'''num = [1, 4, 6, 6, 3, 7, 8, 10]
n = int(input("enter a number: "))

if n in num:
   print(True)
else:
   print(False)'''

#task 10
'''base = int(input("enter a base: "))
height = int(input("enter a height: "))
print(1/2*base*height)'''

#task 11
'''x1 = int(input("enter a x1: "))
x2 = int(input("enter a x2: "))
y1 = int(input("enter a y1: "))
y2 = int(input("enter a y2: "))
dist = math.sqrt((x2-x1)*2+(y2-y1)*2)
print(dist)'''

#task 12
'''a, b, c = 5, 8, 6
d, e, f = 7, 9, 4
#By Cramer's rule: x=denom(c,b,f,e)/denom(a,b,d,e)   y=denom(a,c,d,f)/denom(a,b,d,e)
#the determinant of the denom
denominator = a * e - b * d
# If the denominator is zero, the system has no unique solution 
if denominator == 0:
    print("The system has no unique solution.")
else:
    x = (c * e - b * f) / denominator
    y = (a * f - c * d) / denominator

    print(f"Values of x and y: {x}, {y}")
'''

#task 13
# Function to calculate distances between the points
def distance(x1, y1, x2, y2, x3, y3):
    a = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    b = math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)
    c = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
    return a, b, c

# Function to calculate the area of the triangle formed by the points
def area(a, b, c):
    p = (a + b + c) / 2  # Semi-perimeter
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return s

# Function to calculate the radius of the circumcircle
def radius(a, b, c, s):
    r = (a * b * c) / (4 * s)
    return r

# Function to calculate the centroid 
def central(x1, y1, x2, y2, x3, y3):
    Mx = (x1 + x2 + x3) / 3
    My = (y1 + y2 + y3) / 3
    return Mx, My

try:
    # Input prompt for the three coordinates
    print("Enter the coordinates of three points (x1 y1 x2 y2 x3 y3):")
    x1, y1, x2, y2, x3, y3 = map(int, input().split())

    # Calculate the distances between points
    a, b, c = distance(x1, y1, x2, y2, x3, y3)

    # Calculate the area of the triangle
    s = area(a, b, c)

    # Check if the points are collinear (area should not be zero)
    if s == 0:
        raise ValueError("The given points are collinear, so no circle can be formed.")

    # Calculate the radius of the circle
    r = radius(a, b, c, s)

    # Calculate the central coordinate (currently centroid, but not actual circumcenter)
    centralPoint = central(x1, y1, x2, y2, x3, y3)

    # Print the results
    print(f"Radius of the circle is: {r:.3f}")
    print(f"Central coordinate (x, y) of the circle: ({centralPoint[0]:.3f}, {centralPoint[1]:.3f})")

except ValueError as e:
    print(f"Error: {e}")
