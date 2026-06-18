# Take Marks fromt student and print their grade (A,B,C,D) Using "elif"
 
marks = float(input("Enter your marks: "))
if marks >= 75 and marks <= 100 :
    print("A")
elif marks >= 50 and marks < 75 : 
    print("B")
elif marks >=25 and marks < 50:
    print("C")
elif marks > 0 and marks < 25:
    print("D")
elif marks == 0:
    print("fail")
else:
    print("Invalid marks")