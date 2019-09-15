#Justin Trainer
#This program will serve as an amalgamation of our class learning and will be a generally riveting program.
print("Welcome to my project! \nThere are many parts to this project,\nillustrating the diverse nature of our classroom learning!")
print("For the first part, we will make a age claculator!\nSimply input the year your were born!")
yearBorn = int(input())
print("Now enter the current year.")
yearCurrent = int(input())
age = yearCurrent - yearBorn
print("You are",age,"years old.")
if(age>=50):
    print("You got to live through the '70s. What a peaceful time.")
if(age<=50):
    print("Darn! You missed small-town America in the '70's.")
if(age>30):
    print("Also, you're not a millenial. Good job!")
if(age<30):
    print("Also, you're a millenial.")



