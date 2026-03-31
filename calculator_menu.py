# this function add two numbers
def add(a,b):
  return a+b

# this function subtract two numbers
def subtract(a,b):
  return a-b

# this function multiply two numbers
def multiply(a,b):
  return a*b

# this function divide two numbers
def divide(a,b):
  return a/b

  
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
  # take input from user
  choice = input("Enter Choice (1/2/3/4):")

  # check if choice is one of the four options
  if choice in ('1','2','3','4'):
    try:
      num1 = float(input("Enter first number:"))
      num2 = float(input("Enter second number:"))
    except ValueError:
      print("Invalid input. Please enter a number.")
      continue

    if choice == "1":
      print(num1, "+", num2, "=", add(num1,num2))

    elif choice == '2':
      print(num1, "-", num2, "=", subtract(num1,num2))

    elif choice == "3":
      print(num1, "*", num2, "=", multiply(num1,num2))
      
    elif choice == "4":
      print(num1, "/", num2, "=", divide(num1,num2))

    # check if user wants another calculation or not
    # break the while loop if user says no

    next_calculation = input("Let's do next calculation? (yes/no)")
    if next_calculation == "no":
      break
    else:
      print("Invalid input")
