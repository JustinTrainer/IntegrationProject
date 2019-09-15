#Justin Trainer
#This program will serve as an amalgamation of our class learning and will be a generally riveting program.
print("Welcome to the project! I am Wesly the computer program and I will be guiding you through the project of Justin Trainer. \nThere are many parts to this project, illustrating the diverse nature of the learning done in the classroom!")
print("Firstly, let's get to know each other a little better. What is your name?")
name = input()
print("Well," +" " + name + ", great name by the way, welcome to the project of Justin Trainer.\nThis project will serve as an amalgamation of all the things taught in the classroom.")
print("I would like to continue to get to know you, however.\nPlease input the year in which you were born so I can calculate your age. ")
yearBorn = int(input())
print("Now enter the current year.")
yearCurrent = int(input())
age = yearCurrent - yearBorn
print(name + ", " + "you are",age,"years old.")
if(age>=40):
    print("You got to live through the '70s. What a peaceful time.")
if(age<=40):
    print("Darn! You missed small-town America in the '70's.")
if(age>30):
    print("Also, you're not a millenial. Good job!")
if(age<30):
    print("Also, you're a millenial.")



