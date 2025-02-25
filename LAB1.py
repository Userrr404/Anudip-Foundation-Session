# 1.Python program to convert the temperature in degree centigrade to Fahrenheit

celsius = 25

fahrenheit = (celsius * 9/5) + 32
print(celsius, "celsius eqal to fahrenheit: ", fahrenheit)

# 2.Python program to find the area of a triangle whose sides are given

import math

side1 = 3
side2 = 6
side3 = 7
print("side 1: ",side1)
print("side 2: ",side2)
print("side 3: ",side3)

semiPerimeter = (side1 + side2 + side3) / 2

areaOfTriangle = math.sqrt(semiPerimeter*((semiPerimeter - side1)*(semiPerimeter - side2)*(semiPerimeter - side3)))

print("area of triangle: ",areaOfTriangle)

