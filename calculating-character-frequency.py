# Write a function (charCount) that calculates the frequency of characters in a text. The function takes as an input a string and returns a dictionary with the frequency of characters.

def charCount(userInput):
    # Makes user input all lowercase
    fixedInput =  userInput.lower()
    dict = {}
    for i in fixedInput:
        key = dict.keys()
        # Adds frequencies for each character
        if i in key:
            dict[i] += 1
        else:
            dict[i] = 1
    # Prints the number of characters seen in the text (not the length of the text)
    print("Total number of characters including punctuation characters: ", len(key))
    return dict

# Asks user the enter in text
print("Please enter in any ammount of text: ")
userInput = input()

# Gets rid of whitespace
newUserInput = (userInput.replace(" ", ""))

# Prints the list of the characters and the number of the time it shows in the text
print(charCount(newUserInput))
