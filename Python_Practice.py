# Variables
name = "Deepak"
age = 39
print(f"Hello, my name is {name}, and I am {age} years old.")

# Expression
sum = 1 + 20 - (3*4)

# Data Types
# String
name = "Deepak"
print("Data type of variable name: ", type(name))
print(type(name) == str)
print(isinstance(name, str))

# Integer
age = 39
print(isinstance(age, int))

# Class constructor
age2 = float(age)
print(isinstance(age2, float))

# String to integer
age3 = "20"
print(isinstance(int(age3), int))  # casting to integer


# Operators
# Assignment Operators
age = 10
age += 8
print("Age: ", age)

# Arithmetic Operators
# Addition
sum = 1 + 2
print("Sum: ", sum)
# Subtraction
sub = 10 - 5
print("Subtraction: ", sub)
# Multiplication
mul = 2 * 4
print("Multiplication: ", mul)

# Comparison Operators
# Equal to
a = 10
b = 26
print(a == b)
# Not equal to
print(a != b)

# IN Operator
name = "Deepak"
print("D" in name)
print("d" in name)

# Terenary Operator
age = int(input("Enter your age: "))

def check_age(age):
    if age >= 18:
        return True
    else:
        return False
    
result = "Eligible" if check_age(age) == True else "Not Eligible"
print(result)

# Strings in Python
# String Concatenation
first_name = "Deepak"
last_name = "Rai"
full_name = first_name + " " + last_name
print("Full name: ", full_name)
# print(full_name += " is my full name") # This will throw an error

# String Methods
# lower()
print("Lower Case name: ", full_name.lower())
print(full_name)

# len()
print(len(full_name))

# In Operator
print("Rai" in full_name)

# String Slicing
print(full_name[0:6])

# string formatting
name = "Deepak"
age = 39
print(f"Hello, my name is {name} and I am {str(age)} years old.")

# Boolean in Python
done = True

if done:
    print("task is done")
else:
    print("task is not done")

# Empty List, Dictionary or Strings are always False
lList = []
if lList:
    print("List is not empty")
else:
    print("List is emty")

# any() function
book_1_read = True
book_2_read = False

read_any_book = any([book_1_read, book_2_read])  # if any one of the value is True, it will retun True
print("Read any book :", read_any_book)

# all() function
read_all_books = all([book_1_read, book_2_read]) # if all the values are ture, it will return True
print("Read all books: ", read_all_books)

# Number data types
# Complex numbers
complex_num = 3 + 4j
print(type(complex_num))

num = complex(3, 4)
print(num.real, num.imag)

# Built-in functions
# abs() function
print(abs(-5.5))

# Round() function
print(round(5.5)) # round to the nearest integer
print(round(5.79, 1)) # round to the nearest 1 decimal point


# Constants
from enum import Enum

class State(Enum):
    INACTIVE = 0
    ACTIVE = 1
    
print(State.ACTIVE.value)
print(list(State))

# User Input
age = input("Enter your age: ")
print("Your age is: ", age)

# Control Statements
condition = True

if condition == True:
    print("Consition is True")
else:
    print("Condition is False")
    
print("Outside the if-else block")

# Lists
# String List
dogs = ["Roger", "Syd", "Buddy", "Rusty"]

print("Buzzo is in the list: ", "Buzzo" in dogs)
print(dogs[2])

# append a new item to the list
dogs.append("Buzzo")
print(dogs)

dogs[2] = "Meggy"
print(dogs)

# List indexing
print(dogs[-2])
print(dogs[1:3])
print(dogs[1:])
print(len(dogs))

# Add a item at the end of the list
dogs.extend(["Jr. Meggy", "Annie"])
print(dogs)

# Insert an item at a specific index
dogs.insert(1, "Scooby")
print(dogs)

# Remove an item from the list
dogs.remove("Roger")
print(dogs)

# Pop an item from the list
print(dogs.pop())
print(dogs)

# Sorting a list
dogs.sort()
print(dogs)

# Reverse a list
dogs.reverse()
print(dogs)

# work on a copy of the list
dogs_copy = dogs.copy()
dogs_copy.append("Annie")
print(dogs_copy)
print(dogs)

dogs_copy.sort(key=str.lower)
print(dogs_copy)

# sort() method
dogs_new = ["Buzzo", "Meggy", "Annie", "Scooby", "Jr. Meggy"]
print(dogs_new)

# sorted without modifying the original list
print(sorted(dogs_new, key=str.lower))
print(dogs_new)

# to know the index of an item
print(dogs_new.index("Annie"))

# Tuples
names = ("Rogger", "Syd", "Buddy", "Rusty")
names[0]
names.index("Buddy")
names[-1]
len(names)
print("Rusty" in names)
names[1:3]

# sorting tuples
sorted(names)
print(names)

# new tuple
newTuple = names + ("Deepak", "Ajay")
print(newTuple)
newTuple = newTuple + ("Priya",)
print(newTuple)

# Dictionary
dog = {"name": "Roger", "breed": "Labrador", "age": 5}
dog["name"]

# Change the value of a key
dog["name"] = "Scobby"
dog["name"]

# get method
print(dog.get("breed"))

# It return None if the key is not present
print(dog.get("color"))
# we could also assign a default value in case the key is not present
print(dog.get("color", "Brown"))

# pop method
dog.pop("name")
print(dog)

# popitem method
# removes the last item from the dictionary
dog.popitem()
print(dog)

# check a key in the dictionary using in operator
print("color" in dog)
print("breed" in dog)

# get all the keys in a dictionary
print(dog.keys())
print(list(dog.keys()))
# get all the values in a dictionary
print(dog.values())

# we could also get a list
print(list(dog.values()))

# get all the items in a dictionary
print(dog.items())
print(list(dog.items()))

# length of the dictionary
print(len(dog))

# adding a new key-value pair
dog["food"] = "Hills Dog Food"
print(list(dog.items()))

# delete an item in the dictionary
del dog["food"]
print(dog)

# copy a dictionary
dog_copy = dog.copy()
print(dog_copy)

dog_copy["color"] = "Brown"
print(dog_copy)
print(dog)

# Sets
# create a set
names = {"Roger", "Syd", "Buddy", "Rusty"}
print(names)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# intersection of two sets
print(set1.intersection(set2))

intersect = set1.intersection(set2)
print(intersect)

# Union of two sets (set only have uniqeue values)
print(set1.union(set2))

union = set1.union(set2)
print(union)

# Difference of two sets
print(set1.difference(set2))
print(sorted(set2.difference(set1)))

print(set1 > set2)

# creating a list from a set
print(list(set1))

# in operator
print(9 in set1)

# add an item to the set
set1.add(9)
print(set1)

# functions
# define a function
def greet():
    print("Hello, world")
    
greet()

# function with arguments
def sum(a, b):
    return a + b

print(sum(5, 3))
print(sum(5))

# function with default arguments
def sum(a, b=0):
    return a + b

print(sum(5))

def greet(name = "my friend"):
    print(f" Hello, {name}")
    
greet("Deepak")
greet()

# function with keyword arguments
def greet(name, age):
    print(f"Hello, {name}, you are {age} years old")
    
greet(age=39, name="Deepak")


# Variable Scope
# Global scope variable (outside the function)
name = "Deepak"

print(name)

# local scope variable (inside the function)
def greet():
    last_name = "Rai"
    return last_name

print(last_name) # this will throw an error

# Nested Functions
def talk(phrase):
    def say(word):
        print(word)
        
        words = phrase.split(' ')
        for word in words:
            say(word)
            
talk("I am learning Python")

# another example
def counter():
    count = 0
    
    def increment():
        nonlocal count # this will make the count variable nonlocal
        count += 1
        return count
    
    return increment

increment = counter()

print(increment())
print(increment())

for i in range(5):
    print(increment())
    
# object
# everything in Python is an object
# objects have attributes and methods

age = 8
print(age.real)
print(age.imag)
print(age.bit_length()) # length in binary notation

items = [1, 2, 3, 4]
items.append(5)
print(items)
items.pop()
print(items)
print(id(items)) # location in memory

# any modification to the list will change the id
age = 8
print(id(age))
age += 1
print(id(age)) # this will change the id

# loops
# for loop
for i in range(5):
    print(i)

# while loop
i = 0
while i < 5:
    print(i)
    i += 1 # this is important, otherwise it will go into infinite loop
    
    
# break and continue
for i in range(10):
    if i == 5:
        break # this will break the loop at i = 5
    print(i)
    
for i in range(10):
    if i == 5:
        continue # this will skip the iteration at i = 5
    print(i)
    
# print the index of a value in a list
# enumerate function
names = ["Roger", "Syd", "Buddy", "Rusty"]
for index, name in enumerate(names):
    print(index, name)

# Classes in Python
class Dog:
    def __init__(self, name, breed, age): # constructor method
        self.name = name
        self.breed = breed
        self.age = age
        
    def bark(self):
        print("Woof")
        

Buzzo = Dog("Buzzo", "Golden Retriever", 5)
print(Buzzo.name)
print(Buzzo.breed)
print(Buzzo.age)
Buzzo.bark()

# Inheritance
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")
        
    def speak(self):
        print("I don't know what to say")

class Cat(Pet):
    def speak(self):
        print("Meow")
        
class Dog(Pet):
    def speak(self):
        print("Woof")

Cat("Kitty", 3).show()
Cat("Kitty", 3).speak()
Pet("Kitty", 3).show()
Pet("Kitty", 3).speak()
Dog("Buzzo", 5).show()
Dog("Buzzo", 5).speak()

# Modules
# standard library
import random
print(random.random())
print(random.randint(1, 10))

import math
math.sqrt(16)
math.pi

# Importing from dog.py
import dog
dog.bark()

# Importing specific functions from dog.py
from dog import bark
bark()

from math import sqrt
sqrt(16)

# Arguments & Commandline
# accepting arguments
print("Hello")

import sys
name = sys.argv[1]
print(f"Hello, {name}")

print(sys.argv)


# lambda functions
# lambda functions are small anonymous functions
# lambda arguments: expression
exponential = lambda x: x**2
print(exponential(50))

# map, filter, reduce
# map function
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)

def add_one(x):
    return x + 1

added = list(map(add_one, numbers))
print(added)

# filter function
# filter out the even numbers
even = list(filter(lambda x: x % 2 == 0, numbers))
print(even)

# reduce function
# reduce function is not available in Python 3
# from functools import reduce
from functools import reduce
# sum of all the numbers
sum = reduce(lambda x, y: x + y, numbers)
print(sum)

# recursion in Python
def factorial(n):
    if n == 0 or n == 1: # base case
        return 1
    else:
        return n * factorial(n-1) # this is the recursive call

factorial(0)
factorial(1)
factorial(5)

# Decorators in Python
# Decorators are used to modify the behavior of a function
# without changing the function itself
# Decorators are functions that take another function as an argument
# and return another function
def decorator_function(func):
    def wrapper():
        print("This is the first line")
        func()
        print("This is the last line")
        
    return wrapper

def say_hello():
    print("Hello")
    
decorated_function = decorator_function(say_hello)
print(decorated_function())

# using the @ symbol
@decorator_function
def say_hello():
    print("Hello")
    
print(say_hello())

# doc string
# doc string is a string that is written at the beginning of a function
# to describe what the function does
def say_hello():
    """
    This function says hello
    """
    print("Hello")
    
print(say_hello.__doc__)

print(help(dog))

# Annotations
# Annotations are used to add metadata to a function
# Annotations are not enforced by Python
# Annotations are used to provide information about the type of the arguments
def add(a: int, b: int) -> int:
    return a + b

print(add(5, 3))

# Exceptions
# Exceptions are used to handle errors
# try, except, else, finally
try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Please enter a valid number")
except TypeError:
    print("Please enter a valid number")
else:
    print("Thank you for entering your age")
finally:
    print("This will always execute")
    
# another example
try:
    result = 2 / 0
except ZeroDivisionError:
    print("You cannot divide by zero")
else:
    print("The result is: ", result)
finally:
    print("This will always execute")
    
# raise an exception
age = -1
if age <= 0:
    raise Exception("Age cannot be zero or negative")

# Custom Exceptions
class DogNotFoundException(Exception):
    pass # pass is used to avoid an empty block

try:
    raise DogNotFoundException # this will raise an exception
except  DogNotFoundException:
    print("Dog not found")

# with statement
# with statement is used to open a file
# with statement will automatically close the file
with open("file.txt", "r") as file:
    content = file.read()
    print(content)


# Third party packages
# pip install package_name
# pip install numpy
# pip install pandas
# pip install matplotlib
# pip install requests
# Example
import requests
response = requests.get("https://api.github.com")
print(response.status_code)
print(response.json())

# !pip install -U numpy
# !pip install -U pandas
# !pip install -U requests

# !pip uninstall requests
# !pip show requests

# new pip version update
# !C:\Users\deepak\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\python.exe -m pip install --upgrade pip


# list compressions
# list comprehensions are used to create a new list
# from an existing list
# [expression for item in list]

numbers = [1, 2, 3, 4, 5]

numbers_power_2 = [n**2 for n in numbers] # this is list comprehension
print(numbers_power_2)

# long method
numbers_power_2 = []
for n in numbers:
    numbers_power_2.append(n**2)
    
print(numbers_power_2)

# Polymorphism
# Polymorphism is the ability to use a common interface
# for different data types
# Polymorphism is achieved by using the same method
# for different objects
# Polymorphism is used to make the code more flexible
# and reusable
# Example
class Dog:
    def speak(self):
        print("Woof")
        
class Cat:
    def speak(self):
        print("Meow")

animal1 = Dog()
animal2 = Cat()

animal1.speak()
animal2.speak()

# Operator Overloading
# Operator Overloading is the ability to define
# a custom behavior for operators
# Operator Overloading is achieved by defining
# special methods in a class
# Example
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __gt__(self, other):
        return True if self.age > other.age else False
    
dog1 = Dog("Roger", 5)
dog2 = Dog("Syd", 3)
print(dog1 > dog2)





    



