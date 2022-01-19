if __name__ == '__main__':
    books = int(input("How many books would you like?"))# initiated the data
    boxes = float(books / 15)#Calculating for amount of boxes
    if boxes < 1: # reset books
        books = 1

    print("There are ", boxes, "box(es) needed to be used") #print solution
    print("You will need", int(boxes), "full boxes")
