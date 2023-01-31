# Write a function (stringCal) that takes as an input a list of names and returns a tuple of (string, integer, and list).

def stringCal(userList):
  # Finds the longest string in the list
  print("Longest String: ", max(userList, key = len))
  # Counts the amount of strings that are longer than five characters
  print("Count of strings having longer than five characters: ", len([name for name in userList if len(name) > 5]))
  # Prints a list of names that start wth the letter 'J' and is five characters or less
  print("List of names starting with J and have five characters or less: ", ([name for name in userList if len(name) <= 5 and (name[0] in 'J')]))

# Asks the user to enter in names that will be put into a list
print("Please enter names separated by space: ")
userInput = input();
# Puts names in a list and separates them by commas
userList = userInput.split()
print('Original list: ', userList)
# Reads back the longest string, strings longer than 5 characters, and strings 5 and shorter and starting with 'J'
stringCal(userList)
