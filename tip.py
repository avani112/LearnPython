# import random so that it could randomly give tip from 15%, 18% and 20%
import random

# block of random tips
random_amount=[15,18,20]

# taking input of the bill amount 
bill= int(input("Enter the bill amount "))

# choosing from random tips percentage
tip= random.choice(random_amount);

#printing the random percentage of tip given over the bill
print(f"Your tip is {tip}% ")

# calculating the amount of tip
tip_amount = (tip/100)*bill

#printing the tip amount
print(tip_amount)

