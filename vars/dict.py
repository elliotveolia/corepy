from vars.string import valid_string

def valid_dict(value: dict) -> dict:
    """
    Validate that input is a dictionary.

    Args:
        value: The value to validate

    Returns:
        dict: The validated dictionary

    Raises:
        TypeError: If input is not a dictionary
    """
    if not isinstance(value, dict):
        raise TypeError(
            "Error: Argument provided must be of type dict, "
            f"instead got type of {type(input)}."
        )
    return value

def recursive_items(dictionary: dict):
    """
    Recursively extract all key-value pairs from a nested dictionary.

    Yields all key-value pairs from the dictionary and any nested dictionaries,
    flattening the structure to access all leaf values.

    Args:
        dictionary: Dictionary to extract items from (can be nested)

    Yields:
        tuple: (key, value) pairs from all levels of the dictionary

    Raises:
        TypeError: If input is not a dictionary
    """
    dictionary = valid_dict(dictionary)

    for key, value in dictionary.items():
        if isinstance(value, dict):
            yield from recursive_items(value)
        else:
            yield key, value

def all_keys(dictionary: dict) -> tuple[list, list]:
    """
    Extract all keys and values from a nested dictionary.

    Recursively extracts all keys and values from the dictionary and any
    nested dictionaries, returning them as separate lists.

    Args:
        dictionary: Dictionary to extract from (can be nested)

    Returns:
        tuple[list, list]: Tuple of (keys_list, values_list)

    Raises:
        TypeError: If input is not a dictionary
    """
    dictionary = valid_dict(dictionary)

    items = list(recursive_items(dictionary))
    keys = [key for key, _ in items]
    values = [value for _, value in items]

    return keys, values

def sort_alpha(dictionary: dict, reverse: bool = False) -> dict:
    """
    Sort dictionary by keys alphabetically.

    Sorts the dictionary by keys in alphabetical order.
    Can optionally reverse the sort order (Z to A).

    Args:
        dictionary: Dictionary to sort
        reverse: If True, sort in reverse alphabetical order (default: False)

    Returns:
        dict: Dictionary sorted by keys

    Raises:
        TypeError: If input is not a dictionary
    """
    dictionary = valid_dict(dictionary)
    return {key: value for key, value in sorted(dictionary.items(), reverse=reverse)}

def sort_numerical(dictionary: dict, reverse: bool = False) -> dict:
    """
    Sort dictionary by values numerically.

    Sorts the dictionary by values in numerical order (ascending or descending).
    Non-numeric values are placed at the end.

    Args:
        dictionary: Dictionary to sort
        reverse: If True, sort in descending order (default: False)

    Returns:
        dict: Dictionary sorted by values

    Raises:
        TypeError: If input is not a dictionary
    """
    dictionary = valid_dict(dictionary)
    return {key: value for key, value in sorted(dictionary.items(), key=lambda item: item[1], reverse=reverse)}

def key_list(dictionary: dict) -> list:
    """
    Get all keys from a dictionary as a list.

    Extracts all keys from the dictionary and returns them as a list.

    Args:
        dictionary: Dictionary to extract keys from

    Returns:
        list: List of all keys in the dictionary

    Raises:
        TypeError: If input is not a dictionary
    """
    dictionary = valid_dict(dictionary)
    return list(dictionary.keys())

def merge_dicts(*dictionaries: dict) -> dict:
    """
    Merge multiple dictionaries into one.

    Combines all provided dictionaries into a single dictionary.
    If keys overlap, later dictionaries overwrite earlier ones.

    Args:
        *dictionaries: Variable number of dictionaries to merge

    Returns:
        dict: Merged dictionary containing all key-value pairs

    Raises:
        TypeError: If any argument is not a dictionary
        ValueError: If no dictionaries provided
    """
    if not dictionaries:
        raise ValueError("Error: At least one dictionary must be provided")

    merged = {}

    for dictionary in dictionaries:
        dictionary = valid_dict(dictionary)
        merged.update(dictionary)

    return merged

def get_nested(dictionary: dict, path: str, separator: str = ".") -> any:
    """
    Get a value from a nested dictionary using a path.

    Retrieves a value from a nested dictionary by following a dot-separated
    path of keys. Returns None if the path doesn't exist.

    Args:
        dictionary: Dictionary to search
        path: Dot-separated path to the value (e.g., "user.address.city")
        separator: Character separating keys in path (default: ".")

    Returns:
        any: The value at the specified path, or None if not found

    Raises:
        TypeError: If dictionary is not a dictionary or path is not a string
        ValueError: If path is empty
    """
    dictionary = valid_dict(dictionary)
    path = valid_string(path)

    if not path:
        raise ValueError("Error: Path cannot be empty")

    keys = path.split(separator)
    current = dictionary

    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return None

    return current

def flatten_dict(dictionary: dict, separator: str = ".") -> dict:
    """
    Flatten a nested dictionary into a single level.

    Converts a nested dictionary into a flat dictionary with dot-separated keys.
    Nested keys are joined with the separator to create new keys.

    Args:
        dictionary: Nested dictionary to flatten
        separator: Character to join nested keys (default: ".")

    Returns:
        dict: Flattened dictionary with dot-separated keys

    Raises:
        TypeError: If input is not a dictionary
    """
    dictionary = valid_dict(dictionary)

    flattened = {}

    def _flatten(obj, parent_key=""):
        """Recursively flatten nested dictionaries."""
        if isinstance(obj, dict):
            for key, value in obj.items():
                new_key = f"{parent_key}{separator}{key}" if parent_key else key
                _flatten(value, new_key)
        else:
            flattened[parent_key] = obj

    _flatten(dictionary)
    return flattened

def invert_dict(dictionary: dict) -> dict:
    """
    Invert a dictionary by swapping keys and values.

    Creates a new dictionary where the original values become keys
    and the original keys become values. Values must be hashable.

    Args:
        dictionary: Dictionary to invert

    Returns:
        dict: Inverted dictionary with swapped keys and values

    Raises:
        TypeError: If input is not a dictionary
        ValueError: If any value is not hashable
    """
    dictionary = valid_dict(dictionary)

    inverted = {}

    for key, value in dictionary.items():
        try:
            inverted[value] = key
        except TypeError:
            raise ValueError(
                f"Error: Cannot invert dictionary: value '{value}' of type "
                f"{type(value)} is not hashable"
            )

    return inverted

