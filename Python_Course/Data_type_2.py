#to learn more about python data strucutre

#dictionary
my_dict = {'key1': 1, 'key2': 'Mike'}

print(my_dict['key2'])

my_dict['k3'] = [1,2,3,4]

print(my_dict['k3'][1])

my_dict['k4'] = {'k5':'Pushparaj'} #nestted dictionary

print(my_dict)

print(my_dict['k4']['k5'][0:3])

#Tuples: non-modifiable list
l =[1,2,3,4]
t = (1,2,3,4,'mikey')

print(l)
print(t)

l[0] = 'God is good'

print(l)

#t[0] = 'Not possible' # tuples are non-modifiable/inmutable

#SETS - Collections of unique elements i.e will give out values without repeating, Looks similar to dictionary with curly brackets

my_set = {1,2,3,'mikey',3,2,1}

print(my_set)

my_set.add(4)

print(my_set)

#COMPARISON OPERATOR #CONDITIONAL STATEMENT

if 1 < 2 or 2 >3:
    print('statement is TRUE')
else:
    print('statement is FALSE')

