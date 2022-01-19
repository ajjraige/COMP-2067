if __name__ == '__main__':
    km = 440000# initiated the data
    time = 7# initiated the data
    kmPerHour = float(km / time) / 1000 #Calculating for kmPerHour
    mPerSecond = int((float(km/time) / 60) / 60) #Calculating for mPerSecond

    print("Your speed is:", "{:.2f}".format(round(kmPerHour, 2)), "or", mPerSecond) # Print solution
