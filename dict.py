
user={'name':'teja','age':24,'skills':['python','sql']}
user1=dict(name='teja', age=24)
squares={n:n*n for n in range(5)}
print(user['name'])
print(user.get('city'))

print(user.get('city','not found'))
print('age' in user)

user['age']='25'
print(user)

user.update({'age':26,'city':'bangalore'})
print(user)

removed=user.pop('age',None)
print(removed)
print(user)

del user['city']
print(user)

for key in user:
    print(key,user[key])
    
for value in user.values():
    print(value)
    
for key,value in user.items():
    print(key,value)
    
    user={'name':'teja','age':24,'skills':['python','sql']}
user1=dict(name='teja', age=24)
squares={n:n*n for n in range(5)}
print(user['name'])
print(user.get('city'))

print(user.get('city','not found'))
print('age' in user)

user['city']='hyderabad'
print(user)

user.update({'age':25,'city':'bangalore'})
print(user)

removed=user.pop('age',None)
print(removed)
print(user)

del user['city']
print(user)

user={'name':'teja','age':24,'skills':['python','sql']}
user1=dict(name='teja', age=24)
squares={n:n*n for n in range(5)}
print(user['name'])
print(user.get('city'))

print(user.get('city','not found'))
print('age' in user)

user['city']='hyderabad'
print(user)

user.update({'age':25,'city':'bangalore'})
print(user)

removed=user.pop('age',None)
print(removed)
print(user)

del user['city']
print(user)


a = {'x': 1, 'y': 2}
b = {'y': 99, 'z': 3}
merged = {**a, **b}     # {'x': 1, 'y': 99, 'z': 3}  later wins
# 'merged = a | b    '      # same result, Python 3.9+
print(merged)

emp=[{'id':1,'name':'teja','address': {'city': 'Hyderabad'}},
{'id':2,'name':'sai','address': {'city': 'Pune'}}]

employee={'id':[1,2,3],'name':['teja','sai','kumar'],'loc':['hyd','madhapur','banjara']}

by_id={1:{'name':'teja','loc':'madhapur'},2:{'name':'sai','loc':'hyd'}}


city = emp[0]['address']['city']                  # crashes if anything is missing
city = emp[0].get('address', {}).get('city', 'N/A')   # safe cha

print(city)

from collections import defaultdict
students = [
    {'name': 'Alice', 'grade': 'A'},
    {'name': 'Bob', 'grade': 'B'},
    {'name': 'Charlie', 'grade': 'A'}
]
groups=defaultdict(list)
for s in students:
    groups[s['grade']].append(s['name'])
    
print(dict(groups))

sorted_students = sorted(students, key=lambda x: x['name'])    
print(sorted_students)


from collections import Counter
Counter('banana')            # Counter({'a': 3, 'n': 2, 'b': 1})
Counter(words).most_common(3)

import copy

orig = {
    'name': 'teja',
    'skills': ['python']
}

# Assignment
equal = orig
equal['skills'].append('sql')

print("Assignment:", orig)
print("Equal Object:", equal)

# Shallow Copy
shallow = orig.copy()
shallow['skills'].append('django')

print("Shallow:", orig)
print("Shallow Object:", shallow)

# Deep Copy
deep = copy.deepcopy(orig)
deep['skills'].append('flask')

print("Deep:", orig)
print("Deep Object:", deep)

Assignment creates a new reference to the existing object. Both variables point to the same memory location, so changes through one variable are reflected in the other.



A shallow copy creates a new top-level object while sharing references to nested objects. Changes to nested mutable objects affect both the original and the copied object

I use deepcopy() when an object contains nested mutable structures such as lists or dictionaries and I need a completely independent copy so that modifications do not affect the original object.




For interviews, don't just memorize syntax. Understand the theory, why it exists, complexity, use cases, advantages, limitations, and common questions.

Here's an interview-focused cheat sheet for Dicts & Nested Data.

1. What is a Dictionary?
Definition

A dictionary is a built-in Python data structure that stores data as key-value pairs.

student = {
    "name": "Teja",
    "age": 23
}

Interview Answer

A dictionary is a mutable mapping data structure that stores data in key-value pairs. It provides average O(1) lookup, insertion, and deletion using a hash table implementation.

2. Why Dictionaries Are Fast

Example:

student["name"]


Python doesn't search every element.

Instead:

Hashes the key
Finds memory location
Retrieves value
Complexity
Operation	AverageLookup	O(1)
Insert	O(1)
Delete	O(1)
Traversal	O(n)
Interview Question

Why is dictionary lookup O(1)?

Answer:

Python dictionaries use hash tables. The key is hashed to determine where the value is stored, allowing direct access instead of sequential searching.

3. Hashable vs Non-Hashable
Hashable

Can be dictionary keys.

str
int
float
bool
None
tuple


Example:

d = {
    "name": "Teja",
    1: "One",
    (1, 2): "Tuple"
}

Non-hashable

Cannot be keys.

list
dict
set


Example:

d[[1,2]] = "Hello"


Output:

TypeError:
unhashable type: 'list'

Why?

Because these objects are mutable and their hash could change.

Interview Answer

Dictionary keys must be hashable and immutable so that their hash value remains stable throughout their lifetime.

4. Dictionary is Mutable
employee = {}

employee['name'] = 'Teja'
employee['age'] = 23


You can:

✅ Add

✅ Remove

✅ Modify

5. Insertion Order

Since Python 3.7:

d = {
    'a': 1,
    'b': 2,
    'c': 3
}


Output order remains:

a
b
c

Interview Question

Does a dictionary maintain insertion order?

Answer:

Yes. Since Python 3.7 insertion order is guaranteed.

6. Accessing Data
Direct Access
user['name']


Output:

Teja


Danger:

user['city']


Output:

KeyError

Safe Access
user.get('city')


Output:

None

Interview Tip

Use:

.get()


when you're not sure whether the key exists.

7. Nested Data

Real APIs rarely return flat structures.

Example:

user = {
    'name': 'Teja',
    'address': {
        'city': 'Hyderabad',
        'state': 'TG'
    }
}


Dictionary inside dictionary.

Access Nested Values
user['address']['city']


Output:

Hyderabad

Safe Access
user.get('address', {}).get('city')

Interview Answer

Nested dictionaries allow hierarchical representation of complex data such as API responses and JSON structures.

8. List of Dictionaries

Most common JSON structure.

users = [
    {'id':1,'name':'Teja'},
    {'id':2,'name':'Sai'}
]

Appears in
APIs
Databases
REST Services
JSON responses
Loop
for user in users:
    print(user['name'])

Interview Answer

A list of dictionaries is commonly used to represent collections of records where each dictionary represents one entity or row.

9. Dict of Lists
data = {
    'name':['Teja','Sai'],
    'age':[23,25]
}


Looks like columns.

Used heavily in:

NumPy
Pandas
10. Dict of Dicts
employees = {
    101: {'name':'Teja'},
    102: {'name':'Sai'}
}


Fast lookup by ID.

employees[101]


Output:

{'name':'Teja'}

11. Dictionary Comprehension
Syntax
{key:value for item in iterable}


Example:

squares = {n:n*n for n in range(5)}


Output:

{
0:0,
1:1,
2:4,
3:9,
4:16
}

Interview Question

What is dictionary comprehension?

Answer:

Dictionary comprehension is a concise way to create dictionaries from iterables using a single expression.

12. Looping Through Dictionaries
Keys
for key in user:
    print(key)

Values
for value in user.values():
    print(value)

Both
for key,value in user.items():
    print(key,value)


Most commonly used.

13. Merging Dictionaries
a = {'x':1}
b = {'x':99,'y':2}

merged = a | b


Output:

{
 'x':99,
 'y':2
}

Rule

Later dictionary wins.

14. Group By Pattern

Super common interview question.

Input:

students = [
    {'name':'Teja','dept':'IT'},
    {'name':'Sai','dept':'HR'},
    {'name':'Kumar','dept':'IT'}
]


Output:

{
 'IT':['Teja','Kumar'],
 'HR':['Sai']
}


Solution:

from collections import defaultdict

groups = defaultdict(list)

for s in students:
    groups[s['dept']].append(s['name'])

Interview Answer

defaultdict automatically creates missing keys, making grouping operations simple and efficient.

15. Sorting List of Dictionaries
sorted(users,key=lambda u:u['name'])

Theory

lambda tells Python what field to use for comparisons.

Descending
sorted(users,key=lambda u:u['age'],reverse=True)

16. Counter

Counts frequency.

from collections import Counter

Counter("banana")


Output:

{
'a':3,
'n':2,
'b':1
}

Interview Answer

Counter is a specialized dictionary subclass used for counting hashable objects efficiently.

17. Shallow vs Deep Copy

Most asked theory question.

Assignment
b = a


No copy created.

Same object.

Shallow Copy
b = a.copy()


Creates:

✅ New outer dictionary

❌ Nested data shared

Deep Copy
import copy

b = copy.deepcopy(a)


Creates:

✅ New dictionary

✅ New nested lists

✅ New nested dictionaries

Everything independent.

18. Common Interview Questions
Q1. Difference between dict and list?

Dict

Key-value pair
O(1) lookup

List

Index-based
O(n) search
Q2. Why can't lists be dictionary keys?

Answer:

Lists are mutable and therefore unhashable. Dictionary keys must be hashable and immutable.

Q3. Difference between get() and []?
d['x']


Raises KeyError.

d.get('x')


Returns None/default value.

Q4. What does in check?
'name' in d


Checks keys.

Not values.

Q5. Most common dictionary methods?
get()
keys()
values()
items()
update()
pop()
setdefault()
copy()

Final Interview Definitions (Memorize)

Dictionary

A mutable mapping that stores data as key-value pairs using a hash table, providing average O(1) lookup, insertion, and deletion.

Nested Dictionary

A dictionary that contains other dictionaries or collections as values to represent hierarchical data.

Hashable Object

An object whose hash value remains constant during its lifetime and can therefore be used as a dictionary key.

Shallow Copy

Copies only the top-level object while sharing references to nested objects.

Deep Copy

Recursively copies the entire object hierarchy, creating completely independent objects.

If you can explain these 5 definitions confidently with small examples, you'll handle most Python dictionary interview questions successfully.







































