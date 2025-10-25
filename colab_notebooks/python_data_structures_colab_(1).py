# -*- coding: utf-8 -*-
# Python Data Structures — Fixed & Runnable Script

print("# Tuples — create & index")
tup = (1, 2, 3)
print(tup[0])  # 1

print("\n# Tuples — nested & unpack")
numbers = (1, 2, (3, 4))
a, b, (c, d) = numbers
unpacked = (a, b, c, d)
print(unpacked)  # (1, 2, 3, 4)

print("\n# Elements can be accessed with square brackets (0-indexed)")
tup = (10, 20, 30)
print(tup[0])  # 10

print("\n# Tuples are immutable — demo with try/except (no crash)")
tup = (1, 2, 3)
try:
    tup[0] = 99  # will raise
except TypeError as e:
    print("TypeError:", e)

print("\n# Concatenate tuples with +")
t1 = (1, 2, 3)
t2 = (3, 4)
print(t1 + t2)  # (1, 2, 3, 3, 4)

print("\n# Multiply tuple by int")
t = (1, 2)
print(t * 3)  # (1, 2, 1, 2, 1, 2)

print("\n# Assign & unpack")
pt = (5, 6)
x, y = pt
print(x, y)  # 5 6

print("\n# Nested unpack")
numbers = (1, 2, (3, 4))
a, b, (c, d) = numbers
print(a, b, c, d)  # 1 2 3 4

print("\n# Unpack first two, keep rest")
values = (1, 2, 3, 4)
first, second, *rest = values
print(first, second)  # 1 2
print("rest:", rest)  # [3, 4]

print("\n# Use *_ to discard unwanted values")
values = (10, 20, 30, 40, 50)
first, *_ = values
print(first)  # 10

print("\n#### Exercise — flat last-3 of each inner tuple")
tup = ((1,2,3,4,5), (6,7,8,9,10), (11,12,13,14,15))
# for-loop approach
result_list = []
for inner in tup:
    result_list.extend(inner[-3:])
flat = tuple(result_list)
print(flat)  # (3, 4, 5, 8, 9, 10, 13, 14, 15)

print("\n## Lists — basics")
x = [1, 'a', 2, 'b']
print(type(x))  # <class 'list'>

print("\n# list() conversion")
myList = list((1, 2, 3))
print(myList)  # [1, 2, 3]

print("\n# membership with in")
myList = list((1, 2, 3))
print(3 in myList)  # True

print("\n# list concatenation with +")
print([4, None, 'A'] + [7, 8, (9, 10)])  # [4, None, 'A', 7, 8, (9, 10)]

print("\n**Manipulating Lists**")
print("\n# append")
myList = [1, 2, 3]
myList.append(4)
print(myList)  # [1, 2, 3, 4]

print("\n# insert at index")
myList.insert(0, 0)
print(myList)  # [0, 1, 2, 3, 4]

print("\n# pop returns removed element")
print(myList.pop(0))  # 0
print(myList.pop(0))  # 1
print(myList)         # [2, 3, 4]

print("\n# remove by value (first occurrence)")
myList.append(2)      # [2, 3, 4, 2]
print(myList)
myList.remove(2)      # remove first 2
print(myList)         # [3, 4, 2]

print("\n# extend to add multiple elements")
x = [4, None, 'A']
x.extend([1, 2, 3])
print(x)  # [4, None, 'A', 1, 2, 3]

print("\n# sort in place")
a = [6, 5, 4, 3, 2, 1]
a.sort()
print(a)  # [1, 2, 3, 4, 5, 6]

print("\n**Exercise — split & sort strings/ints**")
list1 = [5, "D", 2, "C", 4]
list2 = [3, "A", 1, "B", 6]
merged = list1 + list2
ints, strs = [], []
for item in merged:
    (ints if isinstance(item, int) else strs).append(item)
ints.sort()
strs.sort()
print(ints)  # [1, 2, 3, 4, 5, 6]
print(strs)  # ['A', 'B', 'C', 'D']

print("\n### Slicing Lists")
seq = [1, 2, 3, 4, 5, 6, 7]
print(seq[1:3])  # [2, 3]

print("\n# omit start")
seq = [1, 2, 3, 4, 5, 6, 7]
print(seq[:3])   # [1, 2, 3]

print("\n# omit end")
seq = [1, 2, 3, 4, 5, 6, 7]
print(seq[3:])   # [4, 5, 6, 7]

print("\n# negative indices")
seq = [1, 2, 3, 4, 5, 6, 7]
print(seq[-3:])     # [5, 6, 7]
print(seq[-4:-2])   # [4, 5]

print("\n# slice with a step")
seq = [0, 1, 2, 3, 4]
print(seq[::2])  # [0, 2, 4]

print("\n# reverse list/tuple with step -1")
seq = [0, 1, 2, 3, 4]
print(seq[::-1])  # [4, 3, 2, 1, 0]
t = (1, 2, 3, 4)
print(t[::-1])    # (4, 3, 2, 1)

print("\n### Exercise — odd vs even indices sums (using slicing)")
seq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_odd_idx = sum(seq[1::2])  # indices 1,3,5,7,9 → values 2,4,6,8,10
sum_even_idx = sum(seq[0::2]) # indices 0,2,4,6,8 → values 1,3,5,7,9
print("odd-index sum:", sum_odd_idx)
print("even-index sum:", sum_even_idx)
print("odd-index > even-index ?", sum_odd_idx > sum_even_idx)

print("\n# same logic with for loop + enumerate (fixed i++)")
sum_odd_idx = sum_even_idx = 0
for ix, val in enumerate(seq):
    if ix % 2 == 1:
        sum_odd_idx += val
    else:
        sum_even_idx += val
print("odd-index sum:", sum_odd_idx)
print("even-index sum:", sum_even_idx)

print("\n### Enumerate basic demo")
i = 0
for value in [1, 2, 3, 4]:
    print("value:", value)
    print("index:", i)
    i += 1  # fixed; Python has no i++

print("\n# enumerate idiomatic")
for ix, value in enumerate([1, 2, 3, 4]):
    print("value:", value, "index:", ix)

print("\n### Strings as lists (indexing/slicing)")
x = 'This is a string'
print(x[0])    # 'T'
print(x[0:1])  # 'T'
print(x[0:2])  # 'Th'

print("\n## zip Built-in Method")
seq1 = ['A', 'B', 'C']
seq2 = [1, 2, 3]
zipped = list(zip(seq1, seq2))
print(zipped)  # [('A', 1), ('B', 2), ('C', 3)]

print("\n# zip stops at shortest")
seq3 = [True, False]
print(list(zip(seq1, seq2, seq3)))  # [('A',1,True), ('B',2,False)]

print("\n### Exercise — students with >=60 in both quizzes via zip")
studentIds = [1, 2, 3, 4, 5, 6]
quiz1 = [80, 30, 35, 90, 60, 80]
quiz2 = [70, 20, 95, 80, 75, 20]
wholeData = zip(studentIds, quiz1, quiz2)
passed = [sid for sid, q1, q2 in wholeData if q1 >= 60 and q2 >= 60]
print("Students with >=60 in both:", passed)  # [1, 4, 5]

print("\n## Dictionaries (dict)")
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}

print("\n# set/insert values")
my_dict["gender"] = "female"
print(my_dict)

print("\n# membership on keys")
print('name' in my_dict)  # True

print("\n# delete / pop")
del my_dict['gender']
print(my_dict)
age = my_dict.pop('age')
print("popped age:", age)
print(my_dict)

print("\n# keys / values")
print(list(my_dict.keys()))
print(list(my_dict.values()))

print("\n# update merges/overwrites")
my_dict.update({'age': 30, 'gender': 'female'})
print(my_dict)
my_dict.update({'gender': 'male'})
print(my_dict)

print("\n### Exercise — build nested dict from three lists")
studentIds = [1, 2, 3, 4, 5, 6]
quiz1 = [80, 30, 35, 90, 60, 80]
quiz2 = [70, 20, 95, 80, 75, 20]
studentGrades = {}
for sid, q1, q2 in zip(studentIds, quiz1, quiz2):
    studentGrades[str(sid)] = {'quiz1': q1, 'quiz2': q2}
print(studentGrades)
print(studentGrades['3']['quiz1'])  # 35

print("\n## set Data Structure")
print(set([1, 1, 1, 2, 2, 3]))  # {1, 2, 3}
a = {1, 1, 1, 2, 2, 3}
print(a)  # {1, 2, 3}
b = {3, 4, 5, 6}
print(a.intersection(b))  # {3}
print(a.union(b))         # {1, 2, 3, 4, 5, 6}
print(a - b)              # {1, 2}

print("\n## Lambda Expressions")
square = lambda x: x * x

def square_fn(x):
    return x * x

print(square(5))     # 25
print(square_fn(5))  # 25

print("\n## List Comprehensions")
numbers = [1, 2, 3, 4, 5]
squares = [x * x for x in numbers]
print(squares)  # [1, 4, 9, 16, 25]

print("\n# filter evens (fixed condition)")
numbers = [1, 2, 3, 4, 5]
evens = [x for x in numbers if x % 2 == 0]
print(evens)  # [2, 4]

print("\n# replace 'banana' with 'orange', keep others")
fruits = ["apple", "banana", "cherry", "banana"]
replaced = ["orange" if f == "banana" else f for f in fruits]
print(replaced)  # ['apple', 'orange', 'cherry', 'orange']

print("\n# strings to uppercase with length > 3 (fixed > sign)")
words = ["a", "abc", "abcd", "python"]
print([word.upper() for word in words if len(word) > 3])  # ['ABCD', 'PYTHON']

print("\n# convert all strings to uppercase")
words = ["hello", "world", "python"]
uppercase_words = [word.upper() for word in words]
print(uppercase_words)  # ['HELLO', 'WORLD', 'PYTHON']

print("\n# list of tuples (name, len)")
names = ["Alice", "Bob", "Charlie"]
name_lengths = [(name, len(name)) for name in names]
print(name_lengths)  # [('Alice', 5), ('Bob', 3), ('Charlie', 7)]

print("\n## Dictionary Comprehensions")
numbers = [1, 2, 3, 4, 5]
square_dict = {x: x * x for x in numbers}
print(square_dict)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

print("\n# swap keys and values (note collisions keep last seen key)")
original_dict = {'apple': 'fruit', 'banana': 'fruit', 'carrot': 'vegetable'}
swapped = {v: k for k, v in original_dict.items()}
print(swapped)  # {'fruit': 'banana', 'vegetable': 'carrot'}

print("\n### Exercise — averages via comprehension")
midterm1 = [30, 60, 80]
midterm2 = [80, 95, 85]
averages = [(a + b) / 2 for a, b in zip(midterm1, midterm2)]
print(averages)  # [55.0, 77.5, 82.5]

print("\n### Exercise — build grades dict via comprehension")
studentIds = [1, 2, 3, 4, 5, 6]
quiz1 = [80, 30, 35, 90, 60, 80]
quiz2 = [70, 20, 95, 80, 75, 20]
studentGrades_comp = {
    str(sid): {"quiz1": q1, "quiz2": q2}
    for sid, q1, q2 in zip(studentIds, quiz1, quiz2)
}
print(studentGrades_comp)
