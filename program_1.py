
# Program #1: Random Dice
# Write a "randDice" function (with no input) that randomly chooses two numbers between 1 and 6 (inclusive) and then adds them (this is to simulate the rolling of 2 dice).  
# The dice sum will be the output of this function.
import random
def randDice():
    # Write your logic to generate 2 numbers between 1 and 6 here
    number1=random.randint(1,6)
    number2=random.randint(1,6)
    # Sum 2 numbers
    sum=(number1+number2)
    # return sum to calling function
    return sum

#########
# Then write a mainline that calls the "randDice" function 100 times in a for loop.  
total=0
for x in range(100):
    add_sum=randDice()
    total=(total+add_sum)

final=total/100
print('The average of 100 rolls is', format(final,'.2f'))
# The mainline then prints the average of the 100 rolls, rounded to the nearest 0.01.
