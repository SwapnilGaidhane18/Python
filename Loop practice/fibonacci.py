#  fibonacci series ke first N numbers print kar

n = int(input("Enter the number: "))

a,b = 0,1
for i in range(n):
    print(a, end= " ")
    c = a + b
    a = b
    b = c