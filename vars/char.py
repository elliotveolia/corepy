from vars.string import valid_string

def valid_char(char: str) -> str:
    """
    Validate that input is a single character string.

    Args:
        char: The value to validate

    Returns:
        str: The validated single character

    Raises:
        TypeError: If input is not a string
        ValueError: If string is not exactly one character
    """
    if not isinstance(char, str):
        raise TypeError(
            f"Error: Argument {char} must be of type string, "
            f"instead got type of {type(char)}"
        )

    if len(char) != 1:
        raise ValueError(
            f"Error: Expected single character, got {len(char)} characters"
        )

    return char

def capitalize_first_letter(string: str) -> str:
    """
    Capitalize the first letter of a string.

    Note: This also lowercases the rest of the string.
    Example: "hELLO" becomes "Hello"

    Args:
        string: The string to capitalize

    Returns:
        str: String with first letter capitalized and rest lowercased

    Raises:
        TypeError: If input is not a string
        ValueError: If string is empty
    """
    string = valid_string(string)

    if not string:
        raise ValueError("Error: String cannot be empty")

    return string.capitalize()

def capitalize_all_words(string: str) -> str:
    """
    Capitalize the first letter of each word in a string.

    Args:
        string: The string to capitalize

    Returns:
        str: String with first letter of each word capitalized

    Raises:
        TypeError: If input is not a string
        ValueError: If string is empty
    """
    string = valid_string(string)

    if not string.strip():
        raise ValueError("Error: String cannot be empty or whitespace-only")

    return ' '.join(word.capitalize() for word in string.split())

def uppercase(string: str) -> str:
    """
    Convert a string to uppercase.

    Args:
        string: The string to convert

    Returns:
        str: String with all characters in uppercase

    Raises:
        TypeError: If input is not a string
        ValueError: If string is empty
    """
    string = valid_string(string)

    if not string:
        raise ValueError("String cannot be empty")

    return string.upper()

def lowercase_first_letter(string: str) -> str:
    """
    Lowercase the first letter of a string.

    Converts the first character to lowercase and leaves the rest unchanged.

    Args:
        string: The string to modify

    Returns:
        str: String with first letter lowercased

    Raises:
        TypeError: If input is not a string
        ValueError: If string is empty
    """
    string = valid_string(string)

    if not string:
        raise ValueError("Error: String cannot be empty")

    return string[0].lower() + string[1:]

def lowercase_all_words(string: str) -> str:
    """
    Lowercase the first letter of each word in a string.

    Args:
        string: The string to modify

    Returns:
        str: String with first letter of each word lowercased

    Raises:
        TypeError: If input is not a string
        ValueError: If string is empty
    """
    string = valid_string(string)

    if not string.strip():
        raise ValueError("Error: String cannot be empty or whitespace-only")

    return ' '.join(word[0].lower() + word[1:] if word else ''
                    for word in string.split())

def lowercase(string: str) -> str:
    """
    Convert a string to lowercase.

    Args:
        string: The string to convert

    Returns:
        str: String with all characters in lowercase

    Raises:
        TypeError: If input is not a string
        ValueError: If string is empty
    """
    string = valid_string(string)

    if not string:
        raise ValueError("Error: String cannot be empty")

    return string.lower()

def remove_first_char(string: str) -> str:
    """
    Remove the first character from a string.

    Args:
        string: The string to modify

    Returns:
        str: String with first character removed

    Raises:
        TypeError: If input is not a string
        ValueError: If string is empty
    """
    string = valid_string(string)

    if not string:
        raise ValueError("Error: String cannot be empty")

    return string[1:]

def remove_last_char(string: str) -> str:
    """
    Remove the last character from a string.

    Args:
        string: The string to modify

    Returns:
        str: String with last character removed

    Raises:
        TypeError: If input is not a string
        ValueError: If string is empty
    """
    string = valid_string(string)

    if not string:
        raise ValueError("Error: String cannot be empty")

    return string[:-1]

def remove_first_and_last(string: str) -> str:
    """
    Remove the first and last characters from a string.

    Args:
        string: The string to modify

    Returns:
        str: String with first and last characters removed

    Raises:
        TypeError: If input is not a string
        ValueError: If string has fewer than 2 characters

    """
    string = valid_string(string)

    if len(string) < 2:
        raise ValueError("Error: String must have at least 2 characters")

    return string[1:-1]

def replace_char(string: str, old_char: str, new_char: str) -> str:
    """
    Replace all occurrences of a character in a string.

    Args:
        string: The string to modify
        old_char: The character to replace
        new_char: The character to replace it with

    Returns:
        str: String with all occurrences replaced

    Raises:
        TypeError: If any argument is not a string
        ValueError: If old_char or new_char is not a single character,
                   or if old_char is not found in string
    """
    string = valid_string(string)
    old_char = valid_string(old_char)
    new_char = valid_string(new_char)

    if len(old_char) != 1:
        raise ValueError(f"Error: old_char must be single character, got '{old_char}'")

    if len(new_char) != 1:
        raise ValueError(f"Error: new_char must be single character, got '{new_char}'")

    if old_char not in string:
        raise ValueError(f"Error: Character '{old_char}' not found in string")

    return string.replace(old_char, new_char)

def remove_char(string: str, char: str) -> str:
    """
    Remove all occurrences of a character from a string.

    Args:
        string: The string to modify
        char: The character to remove

    Returns:
        str: String with all occurrences of character removed

    Raises:
        TypeError: If any argument is not a string
        ValueError: If char is not a single character or not found in string

    """
    string = valid_string(string)
    char = valid_string(char)

    if len(char) != 1:
        raise ValueError(f"Error: char must be single character, got '{char}'")

    if char not in string:
        raise ValueError(f"Error: Character '{char}' not found in string")

    return string.replace(char, '')

def add_space_before(string: str) -> str:
    """
    Add a space before a string.

    Args:
        string: The string to modify

    Returns:
        str: String with space added at the beginning

    Raises:
        TypeError: If input is not a string
        ValueError: If string is empty

    """
    string = valid_string(string)

    if not string:
        raise ValueError("Error: String cannot be empty")

    return ' ' + string

def add_space_after(string: str) -> str:
    """
    Add a space after a string.

    Args:
        string: The string to modify

    Returns:
        str: String with space added at the end

    Raises:
        TypeError: If input is not a string
        ValueError: If string is empty

    """
    string = valid_string(string)

    if not string:
        raise ValueError("Error: String cannot be empty")

    return string + ' '

def is_upper(string: str) -> bool:
    """
    Check if a string contains only uppercase characters.

    Returns True only if all cased characters are uppercase.
    Non-cased characters (numbers, symbols) are ignored.

    Args:
        string: The string to check

    Returns:
        bool: True if all cased characters are uppercase, False otherwise

    Raises:
        TypeError: If input is not a string
        ValueError: If string is empty

    """
    string = valid_string(string)

    if not string:
        raise ValueError("Error: String cannot be empty")

    return string.isupper()

def is_lower(string: str) -> bool:
    """
    Check if a string contains only lowercase characters.

    Returns True only if all cased characters are lowercase.
    Non-cased characters (numbers, symbols) are ignored.

    Args:
        string: The string to check

    Returns:
        bool: True if all cased characters are lowercase, False otherwise

    Raises:
        TypeError: If input is not a string
        ValueError: If string is empty

    """
    string = valid_string(string)

    if not string:
        raise ValueError("Error: String cannot be empty")

    return string.islower()

def is_single_char_upper(char: str) -> bool:
    """
    Check if a single character is uppercase.

    Args:
        char: Single character to check

    Returns:
        bool: True if character is uppercase, False otherwise

    Raises:
        TypeError: If input is not a string
        ValueError: If input is not exactly one character

    """
    char = valid_string(char)

    if len(char) != 1:
        raise ValueError(f"Error: Expected single character, got {len(char)} characters")

    return char.isupper()

def is_single_char_lower(char: str) -> bool:
    """
    Check if a single character is lowercase.

    Args:
        char: Single character to check

    Returns:
        bool: True if character is lowercase, False otherwise

    Raises:
        TypeError: If input is not a string
        ValueError: If input is not exactly one character

    """
    char = valid_string(char)

    if len(char) != 1:
        raise ValueError(f"Error: Expected single character, got {len(char)} characters")

    return char.islower()

def has_uppercase(string: str) -> bool:
    """
    Check if a string contains at least one uppercase character.

    Args:
        string: The string to check

    Returns:
        bool: True if string contains uppercase character, False otherwise

    Raises:
        TypeError: If input is not a string
        ValueError: If string is empty

    """
    string = valid_string(string)

    if not string:
        raise ValueError("Error: String cannot be empty")

    return any(char.isupper() for char in string)

def has_lowercase(string: str) -> bool:
    """
    Check if a string contains at least one lowercase character.

    Args:
        string: The string to check

    Returns:
        bool: True if string contains lowercase character, False otherwise

    Raises:
        TypeError: If input is not a string
        ValueError: If string is empty

    """
    string = valid_string(string)

    if not string:
        raise ValueError("Error: String cannot be empty")

    return any(char.islower() for char in string)
