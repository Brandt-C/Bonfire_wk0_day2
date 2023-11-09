# this is a python comment
# we 
# could have any number
# of lines
# of code

# One unique thing about python comments is line ending comments
def function2(): #so you can have a comment here after funcitoning code
    pass

#Variables and a few notes
my_number = 5
print(my_number, type(my_number))

# Data types

#Numbers -->   Integer and Float  (complex is another type we won't commenly deal with)
# String ---> only type type for text!
# Lists, (also tuples but worry about that later)
# Dictionaries (may also be referred to as hashmaps)
# Sets --> you'll dig into those later
# Booleans -->  True  False
# NoneType --> None

# Nums
stringy = '456'
print(int(stringy))

print('\nNUMBER\'S')

num1 = 9
num2 =  15
num3 = 3
num4 =  10
print(type(num1))
print(type(num2))

#floats 
print(float(num1))

num5 = 56.394875
num6 = 33.67
print(num3)
print(int(num3), int(num3))

print('\nMATH OPERATORS')
#Math operators
# add   +
print('add\t',5 + 6)
print(num1 + num3)

#  subtract  -
print('SUB\t', num4 - num2)
#  multiply    *
print('MULT\t', num4 * num2)
#  divide       /
print('DIVIDE\t', num1 / num3)

#  floor divide    //
print(14//4)

#  modulo        %
print(13%4)
#THIS IS very important to remember for determining odd/even
#  a formula to remember --->   x % 2 == 0  --> if True than the number (x) is even
print(10 % 2 == 0) #--> True, EVEN
print(11 % 2 == 0)  #-->  False, ODD

#  10 divided by 2 does have a remainder
print(10 % 2 != 0)  #--> False, EVEN
print(11 % 2 != 0) # --> True, ODD

print('\nShowing Equality')
print('2' == 2)
print('2' != 2)

#  exponents    **

#notes
#   python already understands order of operations!
#   When using divide you will always get a float as the result
#   Modulo and floor division will result in integers

#  =    and     ==   and also NOT equal     !=
# single = is ASSIGNING a value where 
# double == is an equality CHECK; you can remember the double equals as checking equality of BOTH type and value
# 


# Strings
#  ALL text in python, strings ordered, IMMUTEABLE, and iterable!
st1 = 'This is a string!!!'
st2 = "So is THIS rig ht he er e rllak @#$U*&##@$% 2lkj234"
st3 = 'string example of escape chars"like" <-- that'
st4 = 'shorty'
st5 = "CAPS"

print('\nSTRINGS:')
print(st2[7].lower()) #just to show this is just a string. . . specifically the letter H

#concatenation -- a fancy word for saying we can add strings together
st10 = st1 + st2
print(st10)

st11 = 'THIS is my new string' + '\t' + '  ' + st5 + st10 + '  ' + str(23)
print(st11)

# Interpolation, an even fancier word for saying we can use python things in strings!
# most commonly the f-string

eff_st = f"This is an interpolated value --> {num5} .  There it is!"
print(eff_st)

print('replace example:')

rep_st = 'Oh look there\'s some more programming problems.'
print(rep_st.replace('o', 'a', 5))

mod_st = ''
for letter in rep_st:
    if letter.lower() == 'o':
        mod_st += 'a'
    else:
        mod_st += letter
print(mod_st)

# Methods VS Functions
# the main noticeable difference at first glance is the syntax
#function  -->   a_func()
#method   -->     data_type.method()


# LISTS
# lists are dynamic, ordered, muteable, and iterable
print('\nLISTS:')

my_list = [1, 2, 3, 4, 5]
print(my_list[2])
print(my_list)
my_list[2] = 3456
print(my_list)

print(min(my_list))
print(min(234,23465, 2345, 456 ,2345, 234, 456, 12 ))

# append
# adds on the the end of the list!
my_list.append(100)
print(my_list)
some_var = my_list.append(100)
print(my_list)
print(some_var)

#.pop()
# 'pops' off the end of the list. . it also returns the value
popped = my_list.pop(2) # position is an OPTIONAL parameter here, default removes the last item from the list
print(my_list, popped)

sort_var = my_list.sort(reverse=True)
print(my_list)
print(sort_var)


print('\nReturn vs print example:')
def add(a, b):
    return a + b

def mult(a, b):
    print(a * b)

add(3, 5)
mult(3, 5)

# add(mult(3,5), 5)  produces a NoneType err!!!!
# mult(add(3, 5), 5)

# Dictionary
# are a collection of key and value pairs separated by commas but split with a colon  -->   'key':'value'
# They are psuedo-ordered, muteable, iterable
#  ALSO to mention because of the shared curly braces for distinction:  
# SETS  - Kind of a cross between a list and a dictionary. . .   
# The difference is whether a key/value pair or just items separated by a comma
print('\n DICTIONARIES!!!')

my_dictionary = { 'key' : 'value', 'key2' : 'value'}

# ex_dic = {'key' : 'value', 2 : '2', '2' : 2, 'list': [5, 4, 456, 6575]}
ex_dic = {
    'key' : 'value', 
    2 : '2', 
    '2' : 2, 
    'list': [5, 4, 456, 6575]
}

num_list = [0, 1, 2]
num_dic = {
    '0':0,
    '1':1,
    '2':2
}
print(num_dic['0'])
print(num_list[0])

print(num_dic['1'])
print(num_list[1])

confused_dic = {
    0 : 983745345,
    'a string': [2, 'kjhsdf', [{'key':[{'secret':'nested!'}]}, 'second']]
}
# print(confused_dic)
# print(confused_dic['a string'])
# print(confused_dic['a string'][1])

print(confused_dic)
print(confused_dic['a string'])
print(confused_dic['a string'][2])
print(confused_dic['a string'][2][0])
print(confused_dic['a string'][2][0]['key'])
print(confused_dic['a string'][2][0]['key'][0])
print(confused_dic['a string'][2][0]['key'][0]['secret'])

print(confused_dic['a string'][2][1])

students = {
    'Ann': {
        'python': [100, 95, 100],
        'R' : [75, 80, 90, 100]
    },
    'Amanda' : {
        'python': [75, 55, 100],
        'R' : [90, 95, 100]
    }
}

print(students['Ann']['python'][1])
print(students['Amanda']['python'][1])

#conditionals
#  if  /  elif   /else
#  we can have ANY number of if statements
# following an if (or elif) there is some statement to evaluate as True or False
#  we use elif or else to evaluate the SAME thing against different parameters


age = 76

if age < 18:
    print('Kid!')
elif age >= 18:
    print('Adult')
elif age >= 65:
    print('Senior')

if age > 17 and age > 65:
    print('Senior')


#truth tree:
#  T + T --> True
# T + F  --> False
# F + F --> False

# T | T --> True
# T | F --> True
# F | F --> False

#input
#  grabbing user input as a string that is saved to a variable:
# user_string = input('What do you wanna do?')
#CREATE REMOVE VOWELS FUNCTION!!!

# ans_return = f"Awesome!  Let's go {user_string.upper()}"

# print(ans_return)

# Functions
#Syntax:
# def func_name(parameters):
#     this is the codeblock to execute
def rem_vow(string):
    vow = 'aeiou'
    ans = ''
    for s in string.lower():
        if s in vow:
            ans += 'X'
        else:
            ans += s
    return ans

print(rem_vow('This is a random string'))

#membership checks
# the in keyword in python will check within relevant datatype (strings, lists, dictionaries (keys at least))

#looping
# 3 basic types of loops in python
    # the for loop, the index loop, and the while loop

anum_list = [1, 2, 3, 4, 5]
abc_st = 'abcde'

#For loop-->   for item in items:
#                   codeblock to execute on ITEM

for num in anum_list:
    print(num *10)

for letter in abc_st:
    print(letter.upper())


# for num in anum_list:   ----> You can't change items in list, you CAN reassign an index in a list . . . 
#     num = 1
# print(anum_list)

# index loop
# BUT FIRST--- range()
# start, stop, step  . . .   only the stop is required
# print(range(10)) -->  this is a generator so it doesn't do anything until it has to
for x in range(10):
    print(x)
print('\n')
for x in range(5,10):
    print(x)
print('\n')
for x in range(10, 0, -1):
    print(x)

#back to INDEX loop
# for i in range(len(iterable)):
print(anum_list)
print('\nINDEX LOOP!')

# for a in anum_list:
for i in range(len(anum_list)):
    print(i, anum_list[i])
    anum_list[i] = 10
print(anum_list)

print('\nst:', abc_st)
for i in range(len(abc_st)):
    print(i, abc_st[i])


#while loop
# simple but complicated. . . user defined
# syntax -->  while <condition>
#  DON'T do infinite loops, they're bad!

while True:
    print('HELLLLLLOOOOOOOOOOOO Bonfire!')
    break

ex_str = 'HHHHHi there!'

flag = True
point = 0
while flag:
    vow = 'aeiou'
    print('flag is True')
    if ex_str[point] in vow:
        flag = False
    point += 1

#  Incrementing and decrementing:
#   +=   or  -=  or   *=    is short-hand for 
#  point = point + 1
#  point += 1
#  point +1  THIS is just a number

# Looping through dictionaries!!!
looper_dic = {
    'a' : 0,
    'b' : 1,
    'c' : 2,
    'd' : 3,
    'e' : 4
}

# basic loop gives you the keys
for l in looper_dic:
    print(l)

#  There are methods(attributes) for looping through dictionaries
#   .keys()    |    .values()    |   .items()

for l in looper_dic.keys(): #kinda redundant/worthless. . .  this is already what you get in a basic for loop
    print(l)

print('\n.values():')
for l in looper_dic.values():
    print(l)
print(looper_dic.values())
print(list(looper_dic.values()))

print('\n.items():')
for key, value in looper_dic.items():
    print(key, value)

for l in looper_dic:
    print(looper_dic[l])

























