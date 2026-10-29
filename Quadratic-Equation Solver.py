#Making a quadratic equation solver

#The Coefficients and the Constant
a = float(input("Enter the coefficient of 'x²' here: "))
b = float(input("Enter the coefficient of 'x' here: "))
c = float(input("Enter the constant term here: "))

#Defining constraints

if a == 0:
    print("'a' cannot be zero")
else:

    #Calculating the roots (formula)
    d_val = (b**2 - 4*a*c)

    if d_val == 0:
        discriminant = d_val**0.5
        root1 = (-b + discriminant) / (2*a)
        print("The roots are real and equal")
        print(f"Roots: {root1}")

    elif d_val >= 0:
        discriminant = d_val**0.5
        root1 = (-b + discriminant) / (2*a)
        root2 = (-b - discriminant) / (2*a)
        print("The roots are real and distinct")
        print(f"Roots: {root1}, {root2}")

    elif d_val <= 0:
        discriminant = d_val**0.5
        real_part = -b / (2*a)
        imaginary_part = discriminant / (2*a)

        print("The roots are imagianary and distinct")
        print(f"Roots: {real_part} + {imaginary_part}j , {real_part} - {imaginary_part}j")
