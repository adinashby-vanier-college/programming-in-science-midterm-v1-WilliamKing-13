import math

# Q1: Calculate the area of a circle
def area_of_circle(radius):
    area_of_circle = math.pi * (radius ** 2)
    return round(area_of_circle, 2)

# Q2: Hollow Right Triangle
def hollow_right_triangle(n):
    if n < 4:
        return("The triangle height should be at least 4.")
    rows = 1
    while rows <= n:
        if rows == 0:
          print("*", end="")
        x = print("*" * 2)
        y = print("*" + " " + "*")
        z = print("*" + "  " + "*")
        if rows == n-1:
            print("*" * n)
        result += x + y + z 
    return result
    


# Q3: Inverted Pyramid
def inverted_pyramid(n):
    result = ()
    rows = 1
    if n < 3:
        return("The pyramid height should be at least 3.")
    while rows <= n:
        stars = "*" * (n + 4) 
        spaces = " " * (n + 2) + "\n"
        result = stars + spaces
        return result
# ----------------------------------------------------------------
print(area_of_circle(5))
print()

print(hollow_right_triangle(3))
print()

print(hollow_right_triangle(4))
print()

print(hollow_right_triangle(5))
print()

print(inverted_pyramid(3))
print()

print(inverted_pyramid(4))
print()

print(inverted_pyramid(5))
print()