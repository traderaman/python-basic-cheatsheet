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

#####END######
