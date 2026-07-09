import numpy as np

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
                f"Error: Argument {item}, is not a str type, "
                f"instead got type of {type(item)}."
            )

    return value

def remove_all_occurrences(lst: list, item: any) -> list:
    """
    Remove all occurrences of an item from a list.

    Creates a new list with all instances of the specified item removed.

    Args:
        lst: List to remove from
        item: Item to remove

    Returns:
        list: New list with all occurrences removed

    Raises:
        TypeError: If lst is not a list
    """
    lst = valid_list(lst)
    return [element for element in lst if element != item]

def list_to_array(lst: list) -> any:
    """
    Convert a list to a NumPy array.

    Converts a Python list into a NumPy array for numerical operations.

    Args:
        lst: List to convert

    Returns:
        numpy.ndarray: NumPy array created from the list

    Raises:
        TypeError: If input is not a list
    """

    lst = valid_list(lst)
    return np.array(lst)

def sort_ascending(lst: list) -> list:
    """
    Sort a list in ascending order.

    Returns a new sorted list in ascending order (smallest to largest).

    Args:
        lst: List to sort

    Returns:
        list: Sorted list in ascending order

    Raises:
        TypeError: If input is not a list
    """
    lst = valid_list(lst)
    return sorted(lst)

def sort_descending(lst: list) -> list:
    """
    Sort a list in descending order.

    Returns a new sorted list in descending order (largest to smallest).

    Args:
        lst: List to sort

    Returns:
        list: Sorted list in descending order

    Raises:
        TypeError: If input is not a list
    """
    lst = valid_list(lst)
    return sorted(lst, reverse=True)

def equal_length(lst_a: list, lst_b: list) -> bool:
    """
    Check if two lists have equal length.

    Compares the lengths of two lists and returns True if they are equal.

    Args:
        lst_a: First list to compare
        lst_b: Second list to compare

    Returns:
        bool: True if lists have equal length, False otherwise

    Raises:
        TypeError: If either argument is not a list
    """
    lst_a = valid_list(lst_a)
    lst_b = valid_list(lst_b)

    return len(lst_a) == len(lst_b)

def flatten(lst: list) -> list:
    """
    Flatten a nested list into a single level.

    Recursively flattens all nested lists into a single flat list.

    Args:
        lst: Nested list to flatten

    Returns:
        list: Flattened list with all elements at single level

    Raises:
        TypeError: If input is not a list
    """
    lst = valid_list(lst)

    flattened = []

    def _flatten_recursive(items):
        """Recursively flatten nested lists."""
        for item in items:
            if isinstance(item, list):
                _flatten_recursive(item)
            else:
                flattened.append(item)

    _flatten_recursive(lst)
    return flattened

def unique(lst: list) -> list:
    """
    Get unique elements from a list.

    Returns a new list containing only unique elements from the input list.
    Preserves the order of first occurrence.

    Args:
        lst: List to get unique elements from

    Returns:
        list: List containing only unique elements

    Raises:
        TypeError: If input is not a list
    """
    lst = valid_list(lst)

    seen = set()
    unique_list = []

    for item in lst:
        if item not in seen:
            try:
                seen.add(item)
                unique_list.append(item)
            except TypeError:
                # Item is unhashable, add it anyway
                if item not in unique_list:
                    unique_list.append(item)

    return unique_list

def find_index(lst: list, item: any) -> int:
    """
    Find the index of an element in a list.

    Returns the index of the first occurrence of the specified item.
    Returns -1 if the item is not found.

    Args:
        lst: List to search
        item: Item to find

    Returns:
        int: Index of the item, or -1 if not found

    Raises:
        TypeError: If lst is not a list
    """
    lst = valid_list(lst)

    try:
        return lst.index(item)
    except ValueError:
        return -1

def reverse(lst: list) -> list:
    """
    Reverse a list.

    Returns a new list with elements in reverse order.

    Args:
        lst: List to reverse

    Returns:
        list: Reversed list

    Raises:
        TypeError: If input is not a list
    """
    lst = valid_list(lst)
    return lst[::-1]

