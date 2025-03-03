import math

# Q1: Calculate the area of a circle
def area_of_circle(radius):
    area_of_circle = math.pi * (radius ** 2)
    return round(area_of_circle, 2)

# Q2: Hollow Right Triangle
def hollow_right_triangle(n):
    rows = 1
    if n < 4:
        return("The triangle height should be at least 4.")
    while n <= 5:
        if rows == 0:
            print("*")
        if rows == n-1:
                print(n * rows)
                print("*")
        
    


# Q3: Inverted Pyramid
def inverted_pyramid(n):
    result = ()
    if n < 3:
        return("The pyramid should be at least 3.")
    while n <= 5:
        stars = "*" * (n)
        space = " " * (2 * n-2)
        result = stars + space
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