if __name__ == '__main__':
    x = float(input("x:"))# initiated the variable
    y = float(input("y:"))# initiated the variable
    z = float(input("z:"))# initiated the variable
    top = pow(3,y)-(x+y) #Calculating for top of equation
    bot = (x-y)*z #Calculating for bottom of equation
    tot = top/bot #Calculating for total
    print("Result:", tot) # total print
