import inquirer
import re
"""
questions = [
    inquirer.Text('name', message="What's your name"),
    inquirer.Text('surname', message="what's your surname"),
    inquirer.Text('phone', message="What's your phone number"),
  
answers = inquirer.prompt(questions)

print(answers[3])
"""


"""
#Prompt the user for their name
name = input("Please enter your name:")

#Print a greeting using the entered name
print(f"Hello, {name}!")

#Prompt the user for their age
age_str = input("Please enter your age")

#Convert the age to an integer (as input() returns a string)
try:
    age = int(age_str)
    print(f"You are {age} years old.")
except ValueError:
    print("Invalid age entered. Please enter a number.")
"""



#this method works but doesn't allow for decimals
"""
v1_str = input("What is the initial velocity (m/s)? ")
v1 = int(v1_str)

a_str = input("What is the acceleration (m/s^2)? ")
a = int(a_str)  

t_str = input("What is the time (s)? ")
t = int(t_str)

v2 = v1 + a*t

print(f"Final velocity is {v2} (m/s).")
"""


#this method allows for decimals
"""
v1 = float(input("What is the initial velocity (m/s)? "))

a = float(input("What is the acceleration (m/s^2)? "))

t = float(input("What is the time (s)? "))

v2 = v1 + a*t

print(f"Final velocity is {v2} (m/s).")
"""
from pprint import pprint

questions = [
    inquirer.List(
        "Solving for",
        message="What are you solving for?",
        choices=["Final Velocity", "Initial Velocity", "Acceleration", "Time"]
    ),
]          

answers = inquirer.prompt(questions)
pprint(answers)


if answers["Solving for"] == "Final Velocity":
    v1 = float(input("What is the initial velocity (m/s)? "))

    a = float(input("What is the acceleration (m/s^2)? "))

    t = float(input("What is the time (s)? "))

    v2 = v1 + a*t

    
    print(f"Final velocity is {v2} (m/s).")



if answers["Solving for"] == "Initial Velocity":
    v2 = float(input("What is the final velocity (m/s)? "))
    
    a = float(input("What is the acceleration (m/s^2)? "))

    t = float(input("What is the time (s)? "))

    v1 = v2 - a*t
    
    print(f"Initial velocity is {v1} (m/s).")



if answers["Solving for"] == "Acceleration":
    v2 = float(input("What is the final velocity (m/s)? "))
    
    v1 = float(input("What is the initial velocity (m/s)? "))

    t = float(input("What is the time (s)? "))

    a = (v2 - v1)/t
    
    print(f"Acceleration is {a} (m/s^2).")



if answers["Solving for"] == "Time":
    v2 = float(input("What is the final velocity (m/s)? "))
    
    v1 = float(input("What is the initial velocity (m/s)? "))

    a = float(input("What is the acceleration (m/s^2)? "))

    t = (v2 - v1)/a
    
    print(f"Time is {t} (m/s^2).")