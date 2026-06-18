# Check the users age for voting

Age = int(input("Enter your age: "))
if Age >=18 and Age <= 100: 
    print("You can vote!")
elif Age < 18 and Age > 0 : 
    print("You cannt vote now!") 
else:
    print("Invalid Age!")
    