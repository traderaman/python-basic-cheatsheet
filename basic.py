#BASIC
a = 'HACKERMAN'
b = '200.1'
print(len(b))
print(type(b))
print(a[2])

#INDEXING & SLICING
print(a[3:])
print(a[:6])
print(a[4:7])
print(a[::2])
print(a[::])

#ADDITION
c = '2'
d = '3'
print(c+d)
e = 2
f = 3
print(e+f)
g = 'A'
h = 'man'
print(g+h)

#SLICING ADDITION
name = 'Sam'
last_name = name[1:]
first_name = 'P'
print(first_name+last_name)

#SYNTAX MULTIPLICATION
i = 'Aman'
print(i*5)

#UPPER OR LOWER EDIT
print(i.upper())
print(i.lower())

#STRING PRINT FORMATTING
print('{} is a good boy'.format('Aman'))
print(f'{i} is a good boy')
j = 'Raman'
k = 'Suman'
l = 'Kamal'
print(f'{j}, {k}, {l}, are best friends.')
print('{}, {}, {} are brothers.'.format('Raman', 'Suman', 'Kamal'))
print('{z}, {x}, {y} are brothers.'.format(x = 'Raman',y = 'Suman', z = 'Kamal'))
result = r = 200/5
print(f'The result is {r}.Thankyou.')

#LIST
list = ['apple', 'mango', 'banana', 'cherry']
print(list[2])
list.append('guava')
print(list)
list.pop(2)
print(list)
list.sort()
print(list)
list.reverse()

#DICTIONARY
items = {'pencil':'₹5', 'notebook':'₹25', 'eraser': '₹3', 'crayon':'₹100'}
print(items['eraser'])
print(len(items))
print(type(items))
products = {'k1':'v1', 'k2':['v2','v3','v4']}
print(products['k2'])
print(products['k2'][1])
print(products['k2'][1].upper())
value = {'a':'1','b':'2'}
value['a'] = '5'
print(value)
value['c'] = '3'
print(value)
print(value.keys())
print(value.values())
print(value.items())

#TUPLES
t = ('a', 'b', 'c', 'a')
print(len(t))
print(t.count('a'))
print(t.index('b'))

#SETS
myset = set()
myset.add('a')
print(myset)
myset.add('b')
print(myset)
mylist = [1,1,1,1,2,2,2,3,3,3,]
print(set(mylist))

#BOOLEANS
print(1 > 2)
print(1 == 1)
print(1 != 2)
print(2<5<3)
print(1<2 and 4<2)
print('h' == 'h' or '1' == '2')
print(not 1 == 1)

#IF, ELIF, ELSE
if 3>2:
    print('Its True')
#
hungry = True
if hungry:
    print('Feed me!')
#
name = 'Frankie'
if name == 'Frankie':
    print('Hi Frankie')
elif name == 'Sammy':
    print('Hi Sammy')
else:
    print('What is you name?')

#FOR LOOP
mylist = [1,2,3]
for item in mylist:
    print(item)
for num in mylist:
    print('Hi')
#
list = [1,2,3,4,5,6,7,8,9,10]
for letter in list:
    if letter % 2 == 0:
        print(letter)
    else:
        print(f'Odd number: {letter} ')
#
mystring = 'Hello'
for letters in mystring:
    print(letters)
#
newlist = [(1,2),(3,4),(5,6)]
for a,b in newlist:
    print(a)
#
dic = {'k':'v','k2':'v2','k3':'v3'}
for item in dic:
    print(item)
for values in dic.values():
    print(values)

#WHILE LOOP
x = 0
while x < 5:
    print(f'The value of x is {x}')
    x = x + 1  #if not provided there will be unlimited loop, as 'x' has no value.
#
x = 0
while x < 5:
    print(f'The value of x is {x}')
    x = x + 1
else:
    print('x is not less than 5')

#PASS
x = [1,2,3]
for item in x:
    pass
print('end of script')

#CONTINUE
string = 'Sammy'
for letter in string:
    if letter == 'a':
        continue
    print(letter)

#BREAK
x = 0
while x < 5:
    if x == 2:
        break
    print(x)
    x = x+1

#RANGE FUNCTION
mylist = [1,2,3]
for num in range(10):
    print(num)
#
mylist = [1,2,3]
for num in range(3,10):
    print(num)
#
mylist = [1,2,3]
for num in range(3,11):
    print(num)

#ENUMERATE FUNCTION
count = 0
for letter in 'abcde':
    print('At index {} the letter is {}'.format(count,letter))
    count = count + 1
#
word = 'abcde'
for item in enumerate(word):
    print(item)

#ZIP FUNCTION
list1 = [1,2,3]
list2 = ['a','b','c']
for item in zip(list1,list2):
    print(item)

#IN
print('b' in ('x','y','z'))
print('mykey' in {'mykey':345})
#
d = {'mykey':345}
print(345 in d.values())

#MIN MAX
mylist = [10,20,30,40,50]
print(min(mylist))
print(max(mylist))

#IMPORT FUNCTIONS FROM LIBRARY
from random import shuffle

#INPUT
result = int(input('Your age is: '))  #int/float is used to take value as integer not as string
print(result)

#LIST COMPREHENSIONS
mylist = [x for x in range(0,11)]
print(mylist)
#
mynum = [x for x in range(0,11) if x%2 == 0]
print(mynum)

#SPLIT
string = 'I am a good boy'
print(string.split())

#JOIN
string = ['I', 'am', 'a', 'good', 'boy']
print(' '.join(string))

#DEF FUNCTION
def say_hello(name):
    return 'Hello ' + name
print(say_hello('Aman'))
#
def names(a,b,c = 'Aman'):
    return(a,b,c)  #or return (a,b,c)
print(names('Axe','Bobby'))
print(names('Axe','Bobby','Randy'))

# *ARGS or ARGUMENTS
def name(*args):
    return(args)
print(name('Aman','Alex','Bobby','Sandy'))

# **KWARGS or KEYWORD ARGUMENTS
def myfunc(**kwargs):
    return(kwargs)
print(myfunc(Name = 'Aman', Age = '21', Sex = 'Male'))

#REVERSE list or tuple
a = [1,2,3,4,5]
print(a[::-1])

#MAP
def square(num):
    return num**2
my_nums = [1,2,3,4,5]
for items in map(square,my_nums):
    print(items)
#for getting results in list format
result = list(map(square,my_nums))
print(result)
#
def splicer(mystring):
    if len(mystring) %2 == 0:
        return 'Even'
    else:
        return 'Odd'
names = ['Aman','Raman','Albert']
for c in map(splicer,names):
    print(c)

#FILTER
def check_even(num):
    return num%2 == 0
mynums = [1,2,3,4,5,6]
for w in filter(check_even,mynums):
    print(w)
#or
w = list(filter(check_even,mynums))
print(w)

#LAMBDA
square =lambda num: num**2
print(square(2))
#
f = lambda a,b: a+b
print(f(3,5))


#####END######
