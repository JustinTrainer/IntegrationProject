"""
__author__ = Justin Trainer
This program is is an interactive experience that contains an age and
generation calculator, a random probability calculator, and a ballistic
range calculator.

I used the census bureau website for information on generations, the
Gerontology Research Group for information on the oldest living person and
knowledge I gained from the YouTube channel Forgotten Weapons. I also
used Python for Everybody and Professor Vanselow's instruction as a resource.
"""

import random

print(
        "Welcome to the project! I am Wesly the computer program and "
        + "I will be "
        + "guiding you through the project of Justin"
        + " Trainer. \nThere are many parts to this project, illustrating "
        + "the diverse nature of the learning done in the "
        + "classroom!")
# The above code greets the user and explains the purpose of the program.
print("Firstly, let's get to know each other a little better.")
print("What is your name?")
# The code above asks for the user's name.
name = input()  # This code receives the name.
print(
        "Well" + " " + name + ", great name by the way, welcome to the "
        + "project of Justin Trainer.\nThis project will "
        + "serve as an amalgamation of "
        + "all the things taught in the classroom.")
# The code above continues to explain the purpose.
print(
        "I would like to continue to get to know you, "
        + "however.\nPlease input the year "
        + "in which you were born so I can calculate your age. ")
# The code above introduces the age calculator and asks for the user's age.

bad_input = True
year_born = 0
while bad_input:  # This loops until a valid input is entered.
    try:
        year_born = int(input())
        if year_born < 1889:
            print("Please enter a non-negative, reasonable year.")
            continue  # This safeguards against negative numbers.
        bad_input = False
    except ValueError:  # This fires if the input fails.
        print("Please enter a whole number using integers")
# The code above takes the value of the year of birth, and allows for mistakes.
# Above is Professor Vanselow's model for error proofing code.

print("Now enter the current year.")
bad_input = True
year_current = 0
while bad_input:
    try:
        year_current = int(input())
        if year_current < 0:
            print("Please enter a non-negative, reasonable year.")
            continue
        bad_input = False
    except ValueError:
        print("Please enter a whole number using integers")
# The code above aks for the current year, and tolerates errors.
# Above is Professor Vanselow's model for error proofing an input.
age = year_current - year_born
# This code calculates the user's age.

print(name + ", " + "you are", age, "years old.")
# This reports the age to the user.

if year_born > 2001:
    print("You've yet to be classified by the PRB article.")
    print()
elif 2001 >= year_born >= 1983:
    print("You're in the New Boomers generation.")
    print()
elif 1982 >= year_born >= 1965:
    print("You're in the Generation X generation.")
    print()
elif 1964 >= year_born >= 1946:
    print("You're in the Baby Boomers generation.")
    print()
elif 1946 >= year_born >= 1929:
    print("You're in the Lucky Few generation.")
    print()
elif 1928 >= year_born >= 1909:
    print("Your in the Good Warriors generation.")
    print()
elif 1908 >= year_born >= 1890:
    print("You're in the Hard Timers generations.")
    print()
else:
    print("That is impossible. The world's oldest living person, "
          + "Kane Tanaka, was born in 1903.")
    print()


# The above code uses the user's birth year to determine their generation.
# Python for Everybody
# Source: http://supercentenarian-research-foundation.org/TableE.aspx
# This is the information on the oldest living person.
# Source: https://www.prb.org/20thcenturyusgenerations/
# This refers to the generation information.


def fortune_cookie():
    """
This function provides a random message for any input.
    """
    number = random.randint(0, 9)  # This picks a random message.
    if number == 9:
        print("It's sure to happen!")
    elif number == 8:
        print("It's probably going to happen.")
    elif number == 7:
        print("It could happen.")
    elif number == 6:
        print("There's a slight possibility.")
    elif number == 5:
        print("It's a fifty-fifty.")
    elif number == 4:
        print("There's a probably not going to happen.")
    elif number == 3:
        print("Don't bet on it.")
    elif number == 2:
        print("Its really not going to happen.")
    elif number == 1:
        print("Don't even think about it.")
    else:
        print("There's literally a zero percent chance.")


# Python for Everybody.
# The code above randomly selects a number that is correlated with a message.

print("Welcome,", name + ",",
      "to the random probability calculator!\nType "
      + "in a situation and "
      + "the computer will tell you how likely your situation is. "
      + "\nWARNING: Do NOT give credence to any"
      + " answers you get.")
# The code above introduces the random probability calculator.
condition = True
while condition:  # This runs until 'STOP' is entered
    user_situation = input(
        "Type out the situation here! Type STOP and we will "
        + "continue onward. Your situation: ")
    if user_situation == "STOP":
        break
    else:
        fortune_cookie()
# The code above takes inputs and gives outputs as many times as the user
# desires.  It will run until the user types STOP.
# Python for Everybody.
print()
print("Moving on!", name + ",",
      "have you ever wondered what caliber bullet you should use to shoot "
      + "a target from a distance?")


# The above code introduces the ballistic range calculator.
# Python for Everybody.


def gun_dist(range):
    """
This function takes in a distance and returns suggested caliber cartridge.
    :param range: The distance is an integer measured in yards.
    """
    if range >= 1000:
        print("You'll need either a .50 BMG cartridge or something bigger.")
    elif 1000 > range > 300:
        print("I think a 7.62 NATO cartridge will do the job.")
    elif 300 >= range > 100:
        print("5.56 NATO will do the trick.")
    else:
        print("A 9mm cartridge would do you well.")


# The code above will take in a parameter and return a message detailing
# what caliber should be chosen.
# Python for Everybody & Forgotten Weapons were used.


condition = True
while condition:
    try:
        range = int(input(  # The distance is entered.
            "What's the distance in yards of the target? When you want "
            + "to stop, set the distance"
            + " as a negative number. Distance: "))
    except ValueError:
        print(
                "Please put in a non-negative whole number, "
                + "using actual numbers.")
        continue
    if range < 0:  # This is the parameter that breaks the loop.
        break
    else:
        gun_dist(range)
# The code above loops until a negative value is entered.
# Python for Everybody.
print()
print("Adieu", name + "!")
