# This are my notes from the course on https://www.youtube.com/watch?v=rfscVS0vtbw

print ('Hello World')

#This is a comment

from math import * 

name = "Dani"
my_age = 45
print("My name is " + name + " and my age is " + str(my_age))

boolean_var = False

my_age = 45.6
print("My new age\"is " + str(my_age))
print("My new age\nis " + str(my_age))

print(name.lower())
print(name.upper().isupper())
print(len(name))
print(name[2])
print(name.index('ni'))
print(name.replace('ni', "nny"))

remainder = -(10 % 3)
print(abs(remainder))
print(pow(9, 2))
print(max(9, 2))
print(min(9, 2))
print(round(4.7))

#to use these we need to import math
print(floor(4.7))
print(ceil(4.7))
print(sqrt(64))

#surname = input("Enter your surname: ")
#print("Your surname is " + surname + "!")

#num1 = input("Enter a number: ")
#num2 = input("Enter another number: ")
#print(float(num1) + float(num2))

#lists
friends = ["Pedro", "Pedro", "Raquel", "Miquel", 2, False]
print(friends[1])
print(friends[1:])
print(friends[1:3])
friends[2] = "Sandra"
print(friends)

array2 = [2, 4, 7, 1]
print(array2)
friends.extend(array2)
friends.append(145)
friends.insert(2, "Luisa")
friends.remove("Miquel")
#pop removes the last element
friends.pop()
print(friends)
array2.clear()
print(array2)

print(friends.index("Sandra"))
print(friends.count("Pedro"))

fruits = ["Banana", "Apple", "Melon", "Mango"]
fruits.sort()
array3 = [23, 12, 24, 26, 2]
array3.sort()
print(fruits)
print(array3)
friends.reverse()
print(friends)

friends2 = friends.copy()
print(friends2)

#tuples (are immutable)
coordinates = (4, 5)
print(coordinates[1])

mutable_list_of_immutable_tuples = [(3, 5),(12, 14),(60, -2)]

#functions
def say_hi(name):
    #needed identation
    print("Hello " + name)

#now we execute the function
say_hi("Pete")    

def cube(num):
    return num * num * num
    
result = cube(4)
print(result)

#if/else
is_male = False
is_tall = True
if is_male or is_tall:
    #needs identation
    print("You are a male or tall or both")
else:
    print("You neither male nor tall")


if is_male and is_tall:
    print("You are a tall male")
#this is else if
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and (is_tall):
    print("You are not a male but you're tall")
else:
    print("You are not male and not tall")


def max_number(num1, num2, num3):
    if num1 >= num2 and num1>= num3:
        return num1
    elif num2 >= num1 and num2>= num3:
        return num2
    else:
        return num3
        
print(max_number(3, 4, 5))
#to compare equality use ==
#to compare not equality use !=


#dictionaries are key/value pairs
#we can also use numbers as keys
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    121: "August",
    "Sep": "September",
    "Oct": "October",
    1578: "November",
    "Dec": "Devemeber"
}

print(monthConversions['Oct'])
print(monthConversions.get('Feb'))
print(monthConversions.get(121))
print(monthConversions.get('Fff', 'Not a valid key'))

#while

i = 1
while i <= 10:
    #identation needed
    print(i)
    i += 1
    
#now a little game
'''
secret_word = "python"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter you guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("You lose!")
else:
    print("You win!")
    
'''

#for
for letter in "This is a phrase":
    print(letter)

friends = ["Jim", "John", "Mary"]
for friend in friends:
    print(friend)
    
for index in range(3, 10):
    print(index)
    
for index in range(len(friends)):
    print(friends[index])
    
#example
def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(3, 4))

#2D lists
number_grid = [
    [1, 2], 
    [3, 4],
    [5, 12, 1],
    [0]
] 

print(number_grid[2] [1])

#nested loop
for row in number_grid:
    for column in row:
        print(column)
        

#exercise, translate any word with this condition: Any vowel gets converted into a "g"; any other letter remains the surname
'''
def translator(phrase):
    translation = ""
    for letter in phrase:
        #with "in" whe can do the trick
        if letter in "aeiouAEIOU":
            #we can add a string to a string like that
            translation = translation + "g" 
        else:
            translation = translation + letter
    return translation

print(translator(input("Enter a phrase: ")))
'''

'''
#use try except to avoid crashing the Code
try:
    number = int(input("Enter a number: "))
    print(number)
except:
    print("Invalid input")
    
#we can be more scpecific
try:
    value = 10/0;
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err: 
    print(err)
except ValueError:
    print("Invalid input")
'''

'''
#read from external files
#modes are r, w, a(append) and r+(read and write)
#it created the file if it doesn't exist
employee_file = open("name.txt", "r")
print(employee_file.readable())
print(employee_file.read())
print(employee_file.readline())
print(employee_file.readlines()[2])

for employee in employee_file.readlines():
    print(employee)

#if mode is a or w (write deletes what was in)
employee_file.write("\nWhatever")

employee_file.close()

'''

'''
#modules
import whatever_filename
#now we have access to functions, variables,...
whatever_filename.whatever_function()
#here there's a huge list of modules: https://docs.python.org/3/py-modindex.html

#"native" modules can be found in /Lib
# example of external module(pip is a package manager that comes with python 3):
pip install python.docx
#and now we have it in /Lib/site-packages
import docx
# to uninstall
pip uninstall python.docx   
'''
    
#classes and objects
class Student:
    #initialize function
    def __init__(self, name, major, score, is_on_probation):
        self.name = name
        self.major = major
        self.score = score
        self.is_on_probation = is_on_probation
        
#now we create the student(that's an object!, an instance of a class!)
student1 = Student("Jim", "Telecos", "6,5", False)
print(student1.name)

'''
#exercise
question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

questions = [
    Question(question_prompts[0], 'a'),
    Question(question_prompts[1], 'c'),
    Question(question_prompts[2], 'b'),
]

def run_test(questions):
    score = 0 
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got: " + str(score) + "/" + str(len(questions)) + " correct")  

run_test(questions)
'''

'''
#object functions
class NY_student:
    #initialize function
    def __init__(self, name, major, score):
        self.name = name
        self.major = major
        self.score = score
        
    def has_honors(self):
        if self.score >= 9:
            return True
        else:
            return False
            
student1 = NY_student("Jim", "Telecos", 9.5)
print(student1.has_honors())

#Inheritance
class Chef:
    def make_chicken(self):
        print("The chef can make chicken")
    def make_salad(self):
        print("The chef can make salad")
    def make_special_dish(self):
        print("The chef can make bbq ribs")
            
myChef = Chef()

class ChineseChef(Chef):
    def make_rice(self):
        print("The chef can make rice")
    #this overwrites the inherited make_special_dish
    def make_special_dish(self):
        print("The chef can make orange duck")

myChineseChef = ChineseChef()
        
myChineseChef.make_chicken()
myChineseChef.make_special_dish()
'''
#python interpreter
#just open a terminal and write python3
