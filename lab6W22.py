def multiply_lists(list1, list2):
    products = []  # return list

    for f in list1:  # loop for calculation
        for g in list2:
            products.append(g * f)  # Add to return list

    return products  # return list


if __name__ == '__main__':
    counter = 0  # initiation
    sevtwo_Flag = False # 72 flag
    list1 = [4, 2, 7] # lists
    list2 = [3, 1, 9, 2]
    print("List 1", list1)# lists print
    print("List 2", list2)
    prod_list = multiply_lists(list1, list2) # run both list into definition
    print("Sum is :", sum(prod_list)) #Sum print
    for i in prod_list: # check for 4 exist and 72 flag

        if i == 4:
            counter += 1
        elif i == 72:
            sevtwo_Flag = True
    print("4 occurs", counter, "times") # print 4 occurence
    print("72 is in prod_list:", sevtwo_Flag) # print 72 flag
    print(sorted(prod_list))# sorted list print
