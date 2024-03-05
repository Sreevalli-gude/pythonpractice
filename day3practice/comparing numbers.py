# Create a program that takes two numbers as input and prints whether the first number
# is greater than, less than, or equal to the second number.
n1 = int(input("enter 1st number "))
n2 = int(input("enter 2nd number"))
if n1 > n2:
    print(+n1, "is greaterthen", +n2)
elif n1 < n2:
    print(+n1, "is lessthan", +n2)
else:
    print(+n1, '&', +n2, "both are equal")
