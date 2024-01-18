import random

def num_guessing():
    opportunities = 5

    random_number = random.randint(1,5)

    while(opportunities > 0):
        answer = int(input("I think that number is "))

        if answer != random_number:

            opportunities -= 1
        else:
            print("Great, yes you are right. The unknown number was " + str(random_number))
            break

    if opportunities == 0:
        print("You could not guess the number. If it is interesting, try again. And the unknown number was " + str(random_number))



num_guessing()