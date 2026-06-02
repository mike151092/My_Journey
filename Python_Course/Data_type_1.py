#python basics

#Data types
print(1+4)
print(1*4)
print(1/4)
print(2**4)
print(1 % 4)

#Strings

print('I am going to make it')
print("I am going to make it with the help of GOD")

#formatted Strings
name = 'Michael'
age = 33

print(f"My name is {name} and I am {age} years old")
print("My name is {} and I am {} years old".format(name,age))

#indexing String
var = "Hello"
print(var[-1])
print(var[:3])

#List

my_list=[1,"a",2,"b",3,"c"]

my_list.append(4)
my_list.append('d')

print(my_list)

print(my_list[3])

my_new_list = [1,2,3,['a','b','c']]

print(my_new_list[3][2])