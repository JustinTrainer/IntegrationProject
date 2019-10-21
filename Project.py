#Justin Trainer
#This program will serve as an amalgamation of our class learning and will be a generally riveting program.
import math
import random
print("Welcome to the project! I am Wesly the computer program and I will be guiding you through the project of Justin Trainer. \nThere are many parts to this project, illustrating the diverse nature of the learning done in the classroom!")
print("Firstly, let's get to know each other a little better. What is your name?")
name = input()
print("Well," +" " + name + ", great name by the way, welcome to the project of Justin Trainer.\nThis project will serve as an amalgamation of all the things taught in the classroom.")
print("I would like to continue to get to know you, however.\nPlease input the year in which you were born so I can calculate your age. ")
try:
    yearBorn = int(input())
except:
    print("Please enter a whole number using integers")
    yearBorn = int(input("Re-enter the year you were born in numbers."))
print("Now enter the current year.")
try:
    yearCurrent = int(input())
except:
    print("Please enter a whole number using integers")
    yearCurrent = int(input("Re-enter the current year in numbers."))
age = yearCurrent - yearBorn
print(name + ", " + "you are",age,"years old.")
if yearBorn > 2001:
    print("You've yet to be classified by PRB.")
elif yearBorn <= 2001 and yearBorn >= 1983:
    print("You're in the New Boomers generation.")
elif yearBorn <= 1982 and yearBorn >= 1965:
    print("You're in the Generation X generation.")
elif yearBorn <= 1964 and yearBorn >= 1946:
    print("You're in the Baby Boomers generation.")
elif yearBorn <= 1946 and yearBorn >= 1929:
    print("You're in the Lucky Few generation.")
elif yearBorn <= 1928 and yearBorn >= 1909:
    print("Your in the Good Warriors generation.")
elif yearBorn <= 1908 and yearBorn >= 1890:
    print("You're in the Hard Timers generations.")
else:
    print("You've seen a significant portion of history and I want to talk to you.")
#Source https://www.prb.org/20thcenturyusgenerations/
#It refers to the censuse bureau on the website.
def fortuneCookie():
    number = random.randint(0,9)     #sets number to something random
    if number == 9:                      #these are the random options
        print("It's sure to happen!")
    elif number == 8:
        print("It's probably going to happen")
    elif number == 7:
        print("It could happen")
    elif number == 6:
        print("There's a slight possibility")
    elif number == 5:
        print("Its a fifty-fifty")
    elif number == 4:
        print("There's a probably not going to happen")
    elif number == 3:
        print("Don't bet on it")
    elif number == 2:
        print("Its really not going to happen")
    elif number == 1:
        print("Don't even think about it")
    else:
        print("There's literally a zero percent chance")
print("Wecome", name + ",", "to the random probability calculator!\nHow it works is you will type in a situation and the computer will tell you if its likely to happen \nDon't actually pay any attention to any of theanswers you get.")
condition = True
while condition == True:           #runs till 'STOP' is entered
    throwAway = input("Type out the situation here! Type 'STOP' and we will continue onward. Your situation: ")
    if throwAway == "STOP":
        break
    else:
        fortuneCookie()

print("Moving on!", name +",", "have you ever wondered what caliber bullet you should use to take out a terrorist?")
def gunDist(range):
    if range >= 1000:
        print("You'll need either a .50 BMG cartridge or something bigger.")
    elif range < 1000 and range > 300:
        print("I think a 7.62 NATO cartridge will do ya.")
    elif range <= 300 and range > 100:
        print("5.56 NATO will do the trick")
    else:
        print("A 9mm cartridge would do you well")
condition = True
while condition == True:
    try:
        range = int(input("What's the distance in yards of this bad guy? When you want to move on, set the distance to -90. Distance: "))
    except:
        print("Please put in a non-negative whole number, using actual numbers.")
        continue
    if range == -90:
        break
    else:
        gunDist(range)
