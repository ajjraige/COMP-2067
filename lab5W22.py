if __name__ == '__main__':
    counter = 0 # counter for loop
    x = int(input("input an integer between 0 and 8.")) # input x var
    while x < 50: # while loop for looping
        counter += 1 # counter +1
        print(x) # update x for user

        if x % 9 == 0: # if remainer is 9
            print("Found multiple of 9")
            break # break loop
        x += 10 # added +10 for var

print("Final value of x is", x) # final value print
print("The loop was entered", counter, "times") # looped through print