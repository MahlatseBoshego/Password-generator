import random
import string

def create_password(min_length, numbers = True, special_characters=True):
    letters = string.ascii_letters
    special = string.punctuation
    digits = string.digits




    characters = letters

    #if numbers are included that means numbers = True, we add the numbers as part of our characters to use
    if numbers:
        characters += digits

    #if special characters(punctuation) are included that means special_characters= True, we add the special_characters as part of our characters to use
    if special_characters:
        characters += special

    pwd = ''
    meets_requirements = False
    inludes_special_char = False
    inludes_number = False

    #Loop to determine if password has atleats 1 number, 1 special character
    while not meets_requirements or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            inludes_number = True
        elif new_char in special:
            inludes_special_char = True

        meets_requirements = True
        if numbers:
            meets_requirements = inludes_number
        if special_characters:
            meets_requirements = meets_requirements and inludes_special_char

    return pwd
print("                                                                 WELCOME TO THE PASSWORD GENERATOR \n"
      "                              This program generates random strong passwords to help you get more secured on the internet!!\n"
      "              You have the privilige to choose how long you want your password to be and decide if you would like to include numbers and special characters. ")
while True:
    begin = input('Would you like to begin? Enter (y/n): ' ).lower()
    if begin == 'y':
        while True:
            try:
                min_length = int(input('Enter the minimum length of your desired password (at least 8): '))
                if min_length < 8:
                    print("Password length should be at least 8. Please try again.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter an integer.")



        inludes_number = input("Would you like to include a number? (y/n): ").lower() == "y"
        inludes_special_char = input("Would you like to include a special character? (y/n): ").lower() == "y"
        pwd = create_password(min_length, inludes_number, inludes_special_char)
        print('The generated password is:', pwd)
    else:
        print("Goodbye:)")
        quit()



