# take 3 numbers from user and print the bigger number from them

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if num1 > num2 and num1 > num3: 
    print(f"The {num1} is big number")
elif num2 > num1 and num2 > num3: 
    print(f" The {num2} is big number")
else: 
    print(f"  The {num3} is big number")
