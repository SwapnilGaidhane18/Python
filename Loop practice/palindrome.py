# check the input number is palindrome number or not 

num = int(input("Enter the number : "))
temp = num
reverse = 0

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp = temp // 10
if num == reverse:
    print("Palindrome Number!")
else:
    print("Not palindrome number!")
