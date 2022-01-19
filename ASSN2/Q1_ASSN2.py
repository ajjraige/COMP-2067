if __name__ == '__main__':
    x = input("Enter your first name\n")# initiated the data
    x = x.strip() # strip spaces

    if x[0].lower() == "a" or x[0].lower() == "e" or x[0].lower() == "o" or x[0].lower() == "i" or x[0].lower() == "y" or x[0].lower() == 'u': #finds vowel
        print("Your name starts with a vowel and starts with", x[0].upper())
    else:

        print("Your name starts with a constant and starts with", x[0].upper()) # if not a vowel
