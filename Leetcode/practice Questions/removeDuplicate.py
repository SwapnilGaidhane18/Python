a = [1,1,2,2,3,3,4,4,5,5]
b = []
for i in range(len(a)):
    if a[i] not in b:
        b.append(a[i])
  
print(b)
 