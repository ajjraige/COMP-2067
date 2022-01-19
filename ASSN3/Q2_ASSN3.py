if __name__ == '__main__':
    total = 0 # initiated the variable
    while total<=100: #Loop for total addition
        i = float(input("Please enter a number: "))
        total += i # add total
        print("Current total:", total)
        if total > 100:
            break
    x = pow(total, 2)
    print("Square of total is", round(x, 1)) #square of total
    print("The total is", total) # Total print
