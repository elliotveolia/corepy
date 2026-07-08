import validators

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

def slash_check(string: str) -> str:
    """
    Ensure string contains a slash (/ or \\), and then terminates it with a slash.

    Args:
        string: The string to validate

    Returns:
        str: String with trailing slash added if missing

    Raises:
        ValueError: If string contains no slashes
    """
    string = valid_string(string)

    # If already ends with slash, return as-is
    if string.endswith(('/', '\\')):
        return string

    # Find which slash type is in the string
    if '/' in string:
        return jwos(string, '/')
    elif '\\' in string:
        return jwos(string, '\\')
    else:
        raise ValueError(
            "Error: No slash was found in this string: "
                f"{string}, please try again."
        )

def web_check(url: str) -> str:
    """
    Validate and normalize a URL.

    Ensures URL has proper protocol (https://) and trailing slash.

    Args:
        url: The URL to validate

    Returns:
        str: Valid, normalized URL

    Raises:
        ValueError: If URL is invalid
    """
    url = valid_string(url)

    # Normalize URL format
    if url.startswith('https://'):
        pass
    elif url.startswith('www.'):
        url = 'https://' + url
    else:
        url = 'https://www.' + url

    # Ensure trailing slash
    if not url.endswith('/'):
        url += '/'

    # Validate URL
    if not validators.url(url):
        raise ValueError(
            f"Error: An the URL provided, {url},"
            " is invalid, please try again."
        )

    return url

def split(string: str, delimiter: str = " ") -> list[str]:
    """
    Split a string by a delimiter.

    Args:
        string: The string to split
        delimiter: Single character to split on (default: space)

    Returns:
        list[str]: List of split strings

    Raises:
        ValueError: If delimiter is not exactly one character
    """
    string = valid_string(string)
    delimiter = valid_string(delimiter)

    if len(delimiter) != 1:
        raise ValueError(
            f"Delimiter must be a single character, got: '{delimiter}'"
        )

    return string.split(delimiter)

def is_float(string: str) -> bool:
    """
    Check if a string can be converted to a float.

    Args:
        string: The string to validate

    Returns:
        bool: True if string is a valid float, False otherwise
    """
    string = valid_string(string)

    try:
        float(string)
        return True
    except ValueError:
        return False
