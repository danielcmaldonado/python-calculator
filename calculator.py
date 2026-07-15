number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

print("Choose the operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice (1/2/3/4): "))

if choice == 1:
    print(f"The result is: {number1 + number2}")

elif choice == 2:
    print(f"The result is: {number1 - number2}")

elif choice == 3:
    print(f"The result is: {number1 * number2}")

elif choice == 4:
    if number2 == 0:
        if number1 == 0:
            print("The result is indeterminate (0/0).")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print(f"The result is: {number1 / number2}")

else:
    print("Invalid input.")