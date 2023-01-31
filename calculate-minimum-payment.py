# Finding the customer's minimum payment
def minPayment(userBalance):
  return round(min(userBalance, max(10, .021 * float(userBalance))), 2)

# Asking the user to input the the customer's balance
print("Please enter in customer's balance: ")
userBalance = float(input())

# Prints out the minimum payment
print("Minimum payment: ", minPayment(userBalance))
