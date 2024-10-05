
# 1. Common Python Functions

# print()
print("Hello, World!")

# input()
# Uncomment the following line if running interactively
# name = input("Enter your name: ")

# len()
print(len([1, 2, 3]))  # Output: 3

# type()
print(type(42))  # Output: <class 'int'>

# range()
for i in range(0, 5):
    print(i)  # Output: 0, 1, 2, 3, 4

# int(), float(), str()
print(int("123"))  # Output: 123
print(float("12.34"))  # Output: 12.34
print(str(42))  # Output: "42"

# sum(), min(), max(), sorted()
numbers = [1, 2, 3]
print(sum(numbers))  # Output: 6
print(min(numbers))  # Output: 1
print(max(numbers))  # Output: 3
print(sorted([3, 1, 2]))  # Output: [1, 2, 3]


# 2. List Methods

lst = [1, 2, 3]

# append()
lst.append(4)
print(lst)  # Output: [1, 2, 3, 4]

# insert()
lst.insert(1, 2.5)
print(lst)  # Output: [1, 2.5, 2, 3, 4]

# remove()
lst.remove(2.5)
print(lst)  # Output: [1, 2, 3, 4]

# pop()
lst.pop()
print(lst)  # Output: [1, 2, 3]

# clear()
lst.clear()
print(lst)  # Output: []

# index()
lst = [1, 2, 3]
print(lst.index(2))  # Output: 1

# count()
lst = [1, 2, 2, 3]
print(lst.count(2))  # Output: 2

# sort() and reverse()
lst = [3, 1, 2]
lst.sort()
print(lst)  # Output: [1, 2, 3]
lst.reverse()
print(lst)  # Output: [3, 2, 1]


# 3. Dictionary Methods

dct = {"a": 1, "b": 2}

# get()
print(dct.get("a"))  # Output: 1

# keys(), values(), items()
print(dct.keys())  # Output: dict_keys(['a', 'b'])
print(dct.values())  # Output: dict_values([1, 2])
print(dct.items())  # Output: dict_items([('a', 1), ('b', 2)])

# pop()
print(dct.pop("a"))  # Output: 1
print(dct)  # Output: {'b': 2}

# update()
dct.update({"c": 3})
print(dct)  # Output: {'b': 2, 'c': 3}

# clear()
dct.clear()
print(dct)  # Output: {}


# 4. String Methods

text = "Hello"

# lower() and upper()
print(text.lower())  # Output: "hello"
print(text.upper())  # Output: "HELLO"

# strip()
print("  Hello  ".strip())  # Output: "Hello"

# split()
print("a,b,c".split(","))  # Output: ['a', 'b', 'c']

# replace()
print("Hello".replace("H", "J"))  # Output: "Jello"

# find()
print("hello".find("e"))  # Output: 1

# join()
print(",".join(["a", "b", "c"]))  # Output: "a,b,c"


# 5. Control Flow Syntax

x = 4

# if, elif, else
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")  # Output: x is less than 5

# for loop
for i in range(3):
    print(i)  # Output: 0, 1, 2

# while loop
while x < 5:
    print(x)  # Output: 4
    x += 1

# break
for i in range(5):
    if i == 3:
        break
    print(i)  # Output: 0, 1, 2

# continue
for i in range(5):
    if i == 2:
        continue
    print(i)  # Output: 0, 1, 3, 4

# try/except
try:
    x = 1 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")  # Output: Cannot divide by zero!
