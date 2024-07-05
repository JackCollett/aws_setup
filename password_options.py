passwords = [ 
    {'service': 'takeaway', 'password': 'asdf', 'added_on': '21/03/22'}, 
    {'service': 'acebook', 'password': 'password123', 'added_on': '22/03/22'}, 
    {'service': 'makersbnb', 'password': 'qwerty789', 'added_on': '22/03/22'}
]

# option 1 - for loop
for password in passwords:
    if password["service"] == "acebook":
        print(password)
        
# option 2 - filter method
def is_acebook(password):
    return password["service"] == "acebook"

print(next(filter(is_acebook, passwords)))

# option 2.1 - filter + lambda

print(next(filter(lambda password: password["service"] == "acebook", passwords)))

# option 3 - list comprehension

print([password for password in passwords if password["service"] == "acebook"])

# version 1 

def are_all_passwords_long_enough(passwords):
    for password in passwords:
        return len(password['password']) >= 8

print(are_all_passwords_long_enough(passwords))

# version 2 

def is_too_short(password):
    return len(password['password']) < 8
    
def are_all_passwords_long_enough(passwords):
    return len(list(filter(is_too_short, passwords))) == 0
    
print(are_all_passwords_long_enough(passwords))

# version 2.1

def are_all_passwords_long_enough(passwords):
    return list(filter(lambda password: len(password['password']) < 8, passwords)) == []

print(are_all_passwords_long_enough(passwords))

# version 3

def are_all_passwords_long_enough(passwords):
    return len([password for password in passwords if len(password['password']) < 8]) == 0
    
print(are_all_passwords_long_enough(passwords))

# Using at least one of the four approaches to wrking with lists you've seen so far:
# - Write a function that checks whether any passwords were added on 21/02/22

def created_on_twenty_second(passwords):
    for password in passwords:
        return password["added_on"] == '21/03/22'
        
print(created_on_twenty_second(passwords))


def is_that_date(password):
    return password["added_on"] == '21/03/22'
    
def created_on_twenty_first(passwords):
    return len(list(filter(is_that_date, passwords))) == 1

print(created_on_twenty_second(passwords))

# - Write a function that returns a list of all passwords added on 22/03/22

def is_that_date(password):
    return password['added_on'] == '22/03/22'

def created_on_twenty_second(passwords):
    pwds = []
    for i in list(filter(is_that_date, passwords)):
        pwds.append(i["password"])
    return pwds
        # pwds.append(password['password'])
    
print(created_on_twenty_second(passwords))

# mapping

result = map(lambda number: number * 2, [1, 2, 3, 4])

print(list(result))

# or
numbers = [1, 2, 3, 4]

def times(number):
    return number * 2
    
result = map(times, numbers)

print(list(result))

# difference between map() and filter() is filter needs to be passed a function that returns True or False

# list comprehension instead of map

print([number * 2 for number in [1, 2, 3, 4]])

# same result - So its a list of something called number timesed by 2 for the loop variable called number in the list of integers 1 - 4.

# for loop
doubled = []
for number in [1, 2, 3, 4]:
    doubled.append(number * 2)
print(doubled)