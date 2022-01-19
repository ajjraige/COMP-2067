if __name__ == '__main__':
    L1 = [5, -34, 0, 98, -11, 244, 193, 28, -10, -20, 45, 67]# initiated the data
    size_array = len(L1) # initiated the data

    x = int(input("Enter a number between 0-11"))
    if 0 <= x <= len(L1): # Check if input is valid
        print("The element in the space", x, " is", L1[x])
        if x in L1: # if it is in L1
            print(x, "is in L1 at position", L1.index(x))
        else: # Not in L1
            print(x, "is not in L1")
        if x % 2 == 0 and x > 0: # If Even
            print("The element in the space", x, " is", L1[:x])
        elif x % 2 != 0: # If odd
            print(L1[-x:])
        elif x == 0: # If 0
            print([])
    else: # If input is invalid
        print("Input incorrect")
