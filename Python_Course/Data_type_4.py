# Data types

# Map function
def square(a):
    return a*a

sequence = [1,2,3,4,5]

#normal way to iterate
for i in sequence:
    print(square(i))

#using Map function
a = list(map(square,sequence))

print(a)


#lambda expression - used in cases when the function is not repeated

squares= lambda b: b*b

sequence_1 = [6,7,8,9,10]

b = list(map(squares, sequence_1))

print(b)

#Fliter function

print(list(filter(lambda b: b%2 == 0, sequence_1)))


#Methods

name = "My #name #is michael"

print(name.upper())
print(name.lower())
print(name.split()) #splits the the string based on white spaces
print(name.split('#')) #splits string based on where # appears

d= {'k1':1, 'k2': 2}

print(d.keys())

#TUPLE UNPACKING

x = [(1,2),(4,5),(5,6)]

for item in x:
    print(item)

#unpacking
for (a,b) in x:
    print(a,b)