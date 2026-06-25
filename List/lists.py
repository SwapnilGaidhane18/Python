L = [] # empty list
print(L)

A = [1, 2, 3, 4, 5] # Homogenous
B = [1, "hello", True, 4.5] # Hetrogenous
print(A,B)

# Multi-diamentional List
# 2d  list
m = [1,2,3,[4,5]]
 

# 3d list
n = [[[1,2],[3,4]],[[5,6],[7,8]]]
 
#List creating by (type casting)
l1 = list("hello")
print(l1)

# how to access list items
X = [5,4,3,2,1]
print(X[0])
print(X[-1])
print(X[::-1])

# access 2d list items
x =  [1,2,3,[4,5]]
print(x[-1][0])

# access 3d list items
c = n = [[[1,2],[3,4]],[[5,6],[7,8]]]
print(c[0][1][0])

# how to edit items of list
# List in python is mutable

g = ["hello","My", "name", "is", "swapnil"]
g[-1] = "yash"
print(g)
g[1:4] = ["swapnil", "yash", "devansh", "sahil"]
print(g)

# How to add [append/extend/insert]

#append()  function
g.append(1000) 
print(g)
#append will always try to add only one item
g.append([1,2])

g.extend([5000,6000,7000])
print(g)
#extend will always try to add multiple items
g.extend("hello")
print(g)

#insert

g.insert(2,"goa")
print(g)

# How to delete [del/remove/pop/clear]
del L # delete the entire list
del A[-1] # delete some portion of the list
print(A)
del g[-5:]
print(g)

# remove
# if you want to delete sahil from g but dont know the index of the item so you can use remove() function to do it.
g.remove("sahil")
print(g)

g.pop() # pop() function deletes the last item of your list
print(g)

g.clear() # clear not deletes the list completely, it makes list empty
print

# Some operations that are present in the list 
d = [1,2,3,4,5]
c = ["a","b","c","d"]
sum = d + c # concatination
print(sum)

mul = d * 4
print(mul) # multiplication

for i in d:
    print(i)

j = [1,2,3,[4,5]]
for i in j:
    print(i,end=" ")

print(4 in j)

# functions

print(len(j))
print(min(d)) # min and max only works on numeric list
print(max(d))

k = [5,4,3,2,1]

print(sorted(k)) # is not makes permanent change
k.sort()
print(k) # makes permanent change 
print(sorted(d,reverse=True))
print(k.index(3))