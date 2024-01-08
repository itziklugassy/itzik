def Sumofdigits(number):
    """
    Calculate the sum of digits of a given number.

    Args:
    number (int): The input number.

    Returns:
    int: The sum of digits.
    """
    if number < 0:
        number = -number  # Make sure we work with positive numbers
    return sum(int(digit) for digit in str(number))

def Ispal(number):
    """
    Check if a number is a palindrome.

    Args:
    number (int): The input number.

    Returns:
    bool: True if the number is a palindrome, False otherwise.
    """
    if number < 0:
        return False  # Negative numbers can't be palindromes
    number_str = str(number)
    return number_str == number_str[::-1]

# Example usage:
num1 = 234
print(f"Sum of digits of {num1} is {Sumofdigits(num1)}")
print(f"{num1} is a palindrome: {Ispal(num1)}")

num2 = 121
print(f"Sum of digits of {num2} is {Sumofdigits(num2)}")
print(f"{num2} is a palindrome: {Ispal(num2)}")
