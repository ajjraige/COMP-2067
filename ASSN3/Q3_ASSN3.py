if __name__ == '__main__':

    x = 0# initiated the data
    y = 1# initiated the data
    total = 0# initiated the data
    totalList = []# initiated the data

    for i in range(19):
        if i == 1:
            totalList.append(total) # Adds to list
        totalList.append(total)

        total = x + y#Calculating for
        x = y#Calculating for
        y = total#Calculating for

    print("the first 20 numbers of the Fibonacci sequence are:", totalList, "") # Prints full list
