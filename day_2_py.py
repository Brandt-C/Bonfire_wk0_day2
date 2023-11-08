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

add(mult(3,5), 5)
# mult(add(3, 5), 5)












