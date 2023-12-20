import pandas
import calculate

print("Hello World!")
#print(calculate.x)
print("Hi Again")

print("bye bye")
#---------------------------------------------------------------
# Get input from the user
user_input = input("Enter a number: ")

# Check if the input can be converted to an integer
try:
    number = int(user_input)
except ValueError:
    print("Please enter a valid integer.")
    exit()

# Check if the number is even or odd
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")
  #-------------------------------------------------------------