import math
import random

def valid_num(num: int | float) -> int | float:
    """
    Validate that input is a number (int or float).

    Args:
        num: The value to validate

    Returns:
        int | float: The validated number

    Raises:
        TypeError: If input is not an int or float
    """
    if not isinstance(num, (int, float)):
        raise TypeError(
            f"Error: Argument {num} is not of type int or float, "
            f"instead got type of {type(num)}."
        )
    return num

def valid_int(num: int) -> int:
    """
    Validate that input is an integer.

    Args:
        num: The value to validate

    Returns:
        int: The validated integer

    Raises:
        TypeError: If input is not an int
    """
    if not isinstance(num, int):
        raise TypeError(
            f"Error: Argument {num} is not of type int, "
            f"instead got type of {type(num)}."
        )
    return num

def valid_float(num: int | float) -> float:
    """
    Validate that input is a float or int (convertible to float).

    Args:
        num: The value to validate

    Returns:
        float: The validated float

    Raises:
        TypeError: If input is not an int or float
    """
    if not isinstance(num, (int, float)):
        raise TypeError(
            f"Error: Argument {num} is not of type float, "
            f"instead got type of {type(num)}."
        )
    return num

def add(*numbers: int | float) -> int | float:
    """
    Add multiple numbers together.

    Args:
        *numbers: Variable number of int or float arguments

    Returns:
        int | float: Sum of all numbers

    Raises:
        TypeError: If any argument is not a number
        ValueError: If no numbers provided
    """
    if not numbers:
        raise ValueError("At least one number must be provided")

    validated_numbers = [valid_num(num) for num in numbers]
    return sum(validated_numbers)

def sub(*numbers: int | float) -> int | float:
    """
    Subtract multiple numbers from the first number.

    Subtracts all subsequent numbers from the first number.
    Example: sub(10, 2, 3) = 10 - 2 - 3 = 5

    Args:
        *numbers: Variable number of int or float arguments

    Returns:
        int | float: Result of subtraction

    Raises:
        TypeError: If any argument is not a number
        ValueError: If fewer than 2 numbers provided
    """
    if len(numbers) < 2:
        raise ValueError("At least two numbers must be provided")

    validated_numbers = [valid_num(num) for num in numbers]

    # Start with first number, subtract all others
    result = validated_numbers[0]
    for num in validated_numbers[1:]:
        result -= num

    return result

def multiply(*numbers: int | float) -> int | float:
    """
    Multiply multiple numbers together.

    Args:
        *numbers: Variable number of int or float arguments

    Returns:
        int | float: Product of all numbers

    Raises:
        TypeError: If any argument is not a number
        ValueError: If no numbers provided
    """
    if not numbers:
        raise ValueError("At least one number must be provided")

    validated_numbers = [valid_num(num) for num in numbers]

    result = 1
    for num in validated_numbers:
        result *= num

    return result

def divide(*numbers: int | float) -> float:
    """
    Divide the first number by all subsequent numbers.

    Divides the first number by each subsequent number in sequence.
    Example: divide(100, 2, 5) = 100 / 2 / 5 = 10.0

    Args:
        *numbers: Variable number of int or float arguments

    Returns:
        float: Result of division

    Raises:
        TypeError: If any argument is not a number
        ValueError: If fewer than 2 numbers provided or any divisor is zero
    """
    if len(numbers) < 2:
        raise ValueError("At least two numbers must be provided")

    validated_numbers = [valid_num(num) for num in numbers]

    # Check for zero divisors
    for divisor in validated_numbers[1:]:
        if divisor == 0:
            raise ValueError("Divisor cannot be zero")

    # Divide first by all others
    result = validated_numbers[0]
    for divisor in validated_numbers[1:]:
        result /= divisor

    return result

def deg_to_rad(degrees: int | float) -> float:
    """
    Convert degrees to radians.

    Args:
        degrees: Angle in degrees

    Returns:
        float: Angle in radians

    Raises:
        TypeError: If input is not a number
    """
    degrees = valid_num(degrees)
    return math.radians(degrees)

def rad_to_deg(radians: int | float) -> float:
    """
    Convert radians to degrees.

    Args:
        radians: Angle in radians

    Returns:
        float: Angle in degrees

    Raises:
        TypeError: If input is not a number
    """
    radians = valid_num(radians)
    return math.degrees(radians)

def power(x: int | float, n: int | float = 2) -> int | float:
    """
    Raise a number to a power.

    For negative bases, only odd exponents are allowed to keep results real.

    Args:
        x: The base number
        n: The exponent (default: 2)

    Returns:
        int | float: Result of x raised to power n

    Raises:
        TypeError: If either argument is not a number
        ValueError: If base is negative and exponent is even
    """
    x = valid_num(x)
    n = valid_num(n)

    # Check for invalid case: negative base with even exponent
    if x < 0 and isinstance(n, float) and n % 2 == 0:
        raise ValueError(
            "Cannot raise negative number to an even power (results in complex number)"
        )

    return x ** n

def is_even(number: int | float) -> bool:
    """
    Check if a number is even.

    Args:
        number: The number to check

    Returns:
        bool: True if number is even, False otherwise

    Raises:
        TypeError: If input is not a number
    """
    number = valid_num(number)
    return number % 2 == 0

def is_odd(number: int | float) -> bool:
    """
    Check if a number is odd.

    Args:
        number: The number to check

    Returns:
        bool: True if number is odd, False otherwise

    Raises:
        TypeError: If input is not a number
    """
    number = valid_num(number)
    return number % 2 != 0

def dice_roll(num_dice: int = 1) -> list[int]:
    """
    Roll one or more dice and return the results.

    Args:
        num_dice: Number of dice to roll (default: 1)

    Returns:
        list[int]: List of roll results (1-6 for each die)

    Raises:
        TypeError: If input is not an integer
        ValueError: If num_dice is less than 1
    """
    num_dice = valid_int(num_dice)

    if num_dice < 1:
        raise ValueError("Number of dice must be at least 1")

    return [random.randint(1, 6) for _ in range(num_dice)]

def factorial(n: int) -> int:
    """
    Calculate the factorial of a number.

    Factorial of n (n!) = n × (n-1) × (n-2) × ... × 1

    Args:
        n: Non-negative integer

    Returns:
        int: Factorial of n

    Raises:
        TypeError: If input is not an integer
        ValueError: If n is negative
    """
    n = valid_int(n)

    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")

    result = 1
    for i in range(1, n + 1):
        result *= i

    return result
