#pedrohcdsouza

a = int(input("Write the a side of a triangle: "))
b = int(input("Write the b side of a triangle: "))
c = int(input("Write the c side of a triangle: "))

if a<=0 or b<=0 or c<=0:
    print("The sides must be greater than 0!")
elif b-c > a > b+c or a-c > b > a+c or a-b > c > a+b:
    print("One side cannot be larger than the others when added or subtracted!")
elif a==b==c:
    print("Your triangle is equilateral!")
elif a != b == c or a != c == b or c != b == a:
    print("Your triangle is isosceles!")
else:
    print("Your triangle is scalene!")