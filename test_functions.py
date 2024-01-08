# Define a global flag to track whether a function in simp module has been called
simp_module_called = False

# Import the functions from the modules
from tools.simp import add_numbers  # Import a function from simp.py

# Call a function from the simp module
result = add_numbers(5, 3)  # Call the 'add_numbers' function
print(f"Result of your function: {result}")

# Set the flag to indicate that the simp module has been called
simp_module_called = True

# Now you can call functions from the comp module
from tools.comp import Sumofdigits, Ispal
from tools.col import myzip

# Test the Sumofdigits function
num1 = 234
print(f"Sum of digits of {num1} is {Sumofdigits(num1)}")

num2 = 121
print(f"Sum of digits of {num2} is {Sumofdigits(num2)}")

# Test the Ispal function
palindrome1 = 12321
print(f"{palindrome1} is a palindrome: {Ispal(palindrome1)}")

palindrome2 = 12345
print(f"{palindrome2} is a palindrome: {Ispal(palindrome2)}")

# Test the myzip function
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

zipped_result = myzip(list1, list2)
print(f"Zipped result: {zipped_result}")
