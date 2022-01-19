if __name__ == '__main__':
    myint = int(input("Enter A number between 20-50"))  # input for var
    if myint<20: # if its less tan 20
        print(myint, "is less than minimum acceptable value")
    elif myint>50: # more than 50
        print("<myint > is higher than maximum acceptable")
    else: # good input and calculating
        print(myint, " is within the acceptable range") #Print variable
        result = pow(myint,3)/7.351 # result calc
        print(result) #Print result
        result2 = int(result)
        print(result2) #prints result 2
    print(" The remainder of myint",myint," when divided by 5 is ", myint % 5) # remainer of 5