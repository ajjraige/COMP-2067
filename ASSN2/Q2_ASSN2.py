if __name__ == '__main__':
    while 1:
        x = int(input("Enter a positive integer\n")) # initiated the data
        if x > 0: # Not valid input

            break
        print("Not valid input!")

if x % 2 == 0: # IF even number
    print("You have entered a even integer")
    exit(0)
if x % 7 == 0 and not x % 2 == 0: # IF odd number that is a multiple of 7"
    print("You entered an odd number that is a multiple of 7")
else:
    print("You entered an odd number that is NOT a multiple of 7") # IF odd number that is NOT a multiple of 7
