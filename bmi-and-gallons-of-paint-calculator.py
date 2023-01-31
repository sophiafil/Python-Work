# Function to calculate the BMI using the inputted height and weight
def bmiFormula(userHeight, userWeight):
  bmi = ((userWeight * 703)/(userHeight * userHeight))
  return bmi

# Function to calculate the gallons of paint needed to paint a room based on the length, width, and height of the room and the amount of doors and windows
def paintRoom(length, width, height, num_of_doors, num_of_windows):
  num_of_gals = ((((2 * width * height) + (2 * length * height)) - ((25 * num_of_doors) + (10 * num_of_windows)))/315)
  return num_of_gals

# The dialouge for the Paint Room option. This is where the program asks the user for the room's length, width, height, number of windows, and number of doors, and the user puts in their input.
def paintRoomDialouge():
  print("\nWelcome to the paint needed caluculator")
  print("Enter the length of the room")
  length = float(input())
  print("Enter the width of the room")
  width = float(input())
  print("Enter the height of the room")
  height = float(input())
  print("How many doors are in the room?")
  num_of_doors = int(input())
  print("How many windows are in the room?")
  num_of_windows = int(input())

  # Calculating the gallons
  num_of_gallons = paintRoom(length, width, height, num_of_doors, num_of_windows)

  # Printing back to the user
  print("\n",round(num_of_gallons, 2), " gallons of paint are needed to paint a room ", width," feet wide by ", length, " feet long by ", height, " feet high with ", num_of_doors," doors and ", num_of_windows, " windows.\n")

  # Sends user back to the menu
  menu()

# The dialouge for the BMI Index option. This is where the program asks for the user's weight and height, and the user puts in their input
def bodyMassIndexDialouge():
  print("\nWelcome to the Body Mass Index (BMI) calculator.")
  print("Enter your weight in pounds: ")
  userWeight = float(input())
  print("Enter your height in inches: ")
  userHeight = float(input())

  # Calculaing the BMI value
  bmi = bmiFormula(userHeight, userWeight)

  # Checking the see what range the BMI value is in terms of weight
  if bmi < 18.5:
    bmiValue = "underweight"
  elif (bmi <= 24.9):
    bmiValue = "normal"
  elif (bmi <= 29.9):
    bmiValue = "overweight"
  else:
    bmiValue = "obese"
  
  # Printing back to the user
  print("\nYour BMI is ",round(bmi, 2),". According to the NIH, you are ",bmiValue,".\n")

  # Sends user back to the menu
  menu()

# The menu to choose which caluclator the user wants to use
def menu():  
  print("Welcome to the Python Program.\nMenu options are: \n\tEnter 1 for calculatng gallons of paint needed to paint a room.\n\tEnter 2 for caluclating Body Mass Index\n\tEnter any other value to quit the program")
  print("Enter menu option")
  userInput = input()

  # Checking the user's menu input
  if userInput == "1":
    paintRoomDialouge()
  elif userInput == "2":
    bodyMassIndexDialouge()
  else:
    SystemExit()

# The menu
menu()
