
def valid_string(string: str) -> str:
    """
    Validate that input is a string.

    Args:
        string: The value to validate

    Returns:
        str: The validated string

    Raises:
        TypeError: If input is not a string
    """
    if not isinstance(string, str):
        raise TypeError(
            f"Error: Argument {string} must be of type string, "
            f" instead got type of {type(string)}."
        )
    return string

def jws(*strings) -> str:
    """
    Join multiple strings together with spaces between them.

    Args:
        *strings: Variable number of string arguments

    Returns:
        str: Strings joined with spaces

    Raises:
        TypeError: If any argument is not a string
        ValueError: If any string is empty after validation
    """
    validated_strings = []

    for string in strings:
        validated = valid_string(string)  # Your validation function
        validated_strings.append(validated)

    return ' '.join(validated_strings)

def jwos(*strings) -> str:
    """
    Join multiple strings together without spaces between them.

    Args:
        *strings: Variable number of string arguments

    Returns:
        str: Strings joined without spaces

    Raises:
        TypeError: If any argument is not a string
        ValueError: If any string is empty after validation
    """
    validated_strings = []

    for string in strings:
        validated = valid_string(string)  # Your validation function
        validated_strings.append(validated)

    return ''.join(validated_strings)