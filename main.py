# import neccessary modules
import random
from re import A


# opening file in read mode
file = open(
    "data.txt",
    'r'
    )

data = file.readline()

list_of_digits = []


# function for generating password
def password_generator():
    for digits in data:
        list_of_digits.append(
            digits
            )

    generated_password = ""

    for i in range(13):
        generated_password = generated_password + random.choice(list_of_digits)
        
        
    return generated_password #returning value