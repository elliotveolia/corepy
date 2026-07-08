
def valid_list(value: list) -> list:
    """
    Validate that input is a list.

    Args:
        value: The value to validate

    Returns:
        list: The validated list

    Raises:
        TypeError: If input is not a list
    """
    if not isinstance(value, list):
        raise TypeError(
            f"Error: Argument {value}, is not of type list, "
            f"instead got type of {type(value)}."
        )
    return value

def validate_numeric_list(value: list, integer_only: bool = False) -> list:
    """
    Validate that a list contains only numeric values.

    Checks that all elements in the list are numbers (int or float).
    Can optionally require all elements to be integers only.

    Args:
        value: List to validate
        integer_only: If True, only integers allowed (default: False)

    Returns:
        list: The validated list

    Raises:
        TypeError: If input is not a list or contains non-numeric values
    """
    value = valid_list(value)

    if integer_only:
        valid_type = int
    else:
        valid_type = (int, float)

    for item in value:
        if not isinstance(item, valid_type):
            raise TypeError(
                 f"Error: Argument {item}, is not of type "
                f"{valid_type}, instead got type {type(item)}."
            )

    return value

def validate_string_list(value: list) -> list:
    """
    Validate that a list contains only strings.

    Checks that all elements in the list are strings.

    Args:
        value: List to validate

    Returns:
        list: The validated list

    Raises:
        TypeError: If input is not a list or contains non-string values
    """
    value = valid_list(value)

    for item in value:
        if not isinstance(item, str):
            raise TypeError(
                f"Error: Argument {inpt[i]}, is not a str type, "
                f"instead got type of {type(inpt[i])}."
            )

    return value

