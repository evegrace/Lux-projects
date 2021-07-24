"""Use Python script to generate a random password of 8 characters. Each time the program is run, a new password will be 
generated randomly. The passwords generated will be 8 characters long and will have to 
include the following characters in any order:
2 uppercase letters from A to Z,
2 lowercase letters from a to z,
2 digits from 0 to 9,
2 punctuation signs such as !, ?, “, # """

import random
import string

upper = string.ascii_uppercase
lower = string.ascii_lowercase
digits = string.digits
signs = string.punctuation

#helper function
def get_random(s):
    random_s = ""
    for i in range(2):
        random_s += random.choice(s)
    return random_s

#getting the characters
characters = get_random(upper) + get_random(lower) + get_random(digits) + get_random(signs)

#generating random 8 characters
password_1 = random.sample(characters, 8)
password = ''.join(password_1)
print(password)
