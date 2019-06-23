readme = f"""
----------------------------------------------------------------------------------------------------------------------
First exercise from: https://www.w3resource.com/python-exercises/python-basic-exercises.php

1. Write a Python program to print the following string in a specific format (see the output). Go to the editor
Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, 
Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are" Output :

###################################

Twinkle, twinkle, little star,
    How I wonder what you are! 
        Up above the world so high,   		
        Like a diamond in the sky. 
Twinkle, twinkle, little star, 
    How I wonder what you are

###################################

----------------------------------------------------------------------------------------------------------------------
"""


def twinkle_twinkle():
    verse = ("Twinkle, twinkle, little star,",      # 0
             "How I wonder what you are!",          # 1
             "Up above the world so high,",         # 2
             "Like a diamond in the sky.")          # 3

    print("\nExercise Output:\n")
    print("###################################\n")
    print(f"{verse[0]}\n\t{verse[1]}\n\t\t{verse[2]}\n\t\t{verse[3]}\n{verse[0]}\n\t{verse[1]}")
    print("\n###################################")
    print("\n")


if __name__ == "__main__":
    print(f"{readme}")
    twinkle_twinkle()
