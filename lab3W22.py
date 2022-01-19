if __name__ == '__main__':
    list1 = ['windsor', 'toronto', 'ottawa', 'montreal', 'vancouver'] # lis
    print(list1[0][0:3]) #Print variable
    cityName = input("enter a name of a city") # cityname input
    list1.append(cityName) #append into list
    list1.sort() #sort list
    minVal = list1[0] #find lowest value
    yearBirth = int(input("Enter birth year"))# birth year input
    sumOfAll = yearBirth + len(list1) #sum of all
    print("Sum of all is", yearBirth, "+ sum of list indexes is :", sumOfAll) #Print result
