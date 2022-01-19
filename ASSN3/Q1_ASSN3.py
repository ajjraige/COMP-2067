if __name__ == '__main__':
    wordlist = ['hat', 'book', 'house', 'flower', 'tree', 'grass', 'cheetah', 'lion', 'tiger', 'car', 'boat']# initiated the data
    vowels = ['E', 'O', 'A', 'I', 'U']# initiated the data
    counter = 0# initiated the data
    for x in range(0, len(wordlist) - 1):
        counter = 0
        if x == 0 or x == 3 or x == 6 or x == 9: # check 0 3 6 9 words

            for i in wordlist[x].upper():
                if i in vowels:
                    counter += 1 #Calculating for number of vowels
                    if counter >= 3:
                        print(wordlist[x], "has", counter, "vowels")# Print if vowel exceeds 2
                        print(wordlist[x], "has over 3 vowels!!!")
                        exit(0)

            print(wordlist[x], "has", counter, "vowels") # prints number of vowels

    print("Did not find a string with 3 or more vowels") # List doesnt contain 3 vowel words
