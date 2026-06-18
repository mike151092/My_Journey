#Python Exercises

print(7**4)

#Split the string
s = 'Hi there Sam'

print(s.split())

#formatted String
planet = "Earth"
Diameter = 12742

print("The Diamete of {one} is {two} kilometers".format(one=planet,two = Diameter))

#List
lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]

print(lst[3][1][2][0])

#Dictonary

d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}

print(d['k1'][3]['tricky'][3]['target'][3])

#in tuple we cannot pop an item, but in list you can use the pop method

#create a function that gets the domain of the user

def userdoamin(email):
    return email.split('@')[-1]

print(userdoamin('michaelvinodhraj@gmail.com'))

# function to find particular text in a String

def textinstring(text):
    if "dog" in text.lower():
        print(True)
    else:
        print(False)

textinstring("Hi this jimmy and it is a DOG")

#Funtion to count a particular text in a string

def textcount(text1):
    count = 0
    for word in text1.lower().split():
        if word == 'dog':
            count += 1
    return count

print(textcount("There is no dog in this street, but there are dog un another street"))

#Build a lambda function that filters word starting with s
seq = ['soup','dog','salad','cat','great']

for item in seq:
    if item[0]=='s':
        print(item)

print(list(filter(lambda b: b[0] == 's', seq)))

#Program to determine speeding icket
def caught_speeding(speed,Birthday):
    if Birthday == False:
        if speed <= 60:
            print('No ticket')
        elif 61 < speed <= 81:
            print('small ticket')
        else:
            print('Big Ticket')
    if Birthday == True:
        if speed <= 65:
            print('no Ticket')
        elif 66< speed <= 85:
            print('small ticket')
        else:
            print('big Ticket')

#simple way

def speeding_ticket(velocity, Birth_date):
    if Birth_date:
        velocity = velocity -5
    else:
        velocity = velocity
    
    if velocity >80:
        return('Big Ticket')
    elif velocity >60:
        return('Small Ticket')
    else:
        return('No Ticket')

print(speeding_ticket(81,True))