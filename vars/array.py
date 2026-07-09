import numpy as np
from vars.num import valid_int

def valid_array(value: any) -> any:
    """
    Validate that input is a NumPy array.

    Args:
        value: The value to validate

    Returns:
        numpy.ndarray: The validated NumPy array

    Raises:
        TypeError: If input is not a NumPy array
    """

    if not isinstance(value, np.ndarray):
        raise TypeError(
            f"Error: Argument {value}, is not an array, "
            f"instead got type of {type(value)}"
        )
    return value

def single_array(arr: any) -> any:
    """
    Validate that input is a 1-dimensional NumPy array.

    Checks that the array has exactly one dimension.

    Args:
        arr: Array to validate

    Returns:
        numpy.ndarray: The validated 1D array

    Raises:
        TypeError: If input is not a NumPy array
        ValueError: If array is not 1-dimensional
    """
    arr = valid_array(arr)

    if arr.ndim != 1:
        raise ValueError(
            "Error: Argument is not a single length, "
            f" instead got dimension {arr.ndim}."
        )

    return arr

def array_dimensions(arr: any) -> int:
    """
    Get the number of dimensions of a NumPy array.

    Returns the dimensionality of the array (1D, 2D, 3D, etc.).

    Args:
        arr: Array to check

    Returns:
        int: Number of dimensions

    Raises:
        TypeError: If input is not a NumPy array
    """
    arr = valid_array(arr)
    return arr.ndim

def validate_numeric_array(arr: any) -> any:
    """
    Validate that a 1D array contains only numeric values.

    Checks that all elements in the 1D array are numeric (int or float).
    Supports both Python and NumPy numeric types.

    Args:
        arr: 1D array to validate

    Returns:
        numpy.ndarray: The validated numeric array

    Raises:
        TypeError: If input is not a 1D array or contains non-numeric values
    """

    arr = single_array(arr)

    numeric_types = (int, float, np.integer, np.floating)

    for index, item in enumerate(arr):
        if not isinstance(item, numeric_types):
            raise TypeError(
                f"Error: Entry index {index}; {item}, is not of type "
                f"int or float, instead got type of {type(item)}."
            )

    return arr

def validate_string_array(arr: any) -> any:
    """
    Validate that a 1D array contains only strings.

    Checks that all elements in the 1D array are strings.

    Args:
        arr: 1D array to validate

    Returns:
        numpy.ndarray: The validated string array

    Raises:
        TypeError: If input is not a 1D array or contains non-string values
    """
    arr = single_array(arr)

    for index, item in enumerate(arr):
        if not isinstance(item, str):
            raise TypeError(
                f"Error: Entry index {index}; {item}, is not of type "
                f"string, instead got type of {type(item)}."
            )

    return arr

def validate_bool_array(arr: any) -> any:
    """
    Validate that a 1D array contains only booleans.

    Checks that all elements in the 1D array are booleans.
    Supports both Python and NumPy boolean types.

    Args:
        arr: 1D array to validate

    Returns:
        numpy.ndarray: The validated boolean array

    Raises:
        TypeError: If input is not a 1D array or contains non-boolean values
    """

    arr = single_array(arr)

    bool_types = (bool, np.bool_)

    for index, item in enumerate(arr):
        if not isinstance(item, bool_types):
            raise TypeError(
                f"Error: Entry index {index}; {item}, is not of type "
                f"bool, instead got type of {type(item)}."
            )

    return arr

def equal_array_length(*arrays: any) -> bool:
    """
    Check if multiple 1D arrays have equal length.

    Compares the lengths of multiple 1D arrays and returns True if they are all equal.

    Args:
        *arrays: Variable number of 1D arrays to compare

    Returns:
        bool: True if all arrays have equal length, False otherwise

    Raises:
        TypeError: If any argument is not a 1D array
        ValueError: If fewer than 2 arrays provided
    """
    if len(arrays) < 2:
        raise ValueError("At least two arrays must be provided")

    validated_arrays = [single_array(arr) for arr in arrays]
    lengths = [len(arr) for arr in validated_arrays]

    return all(length == lengths[0] for length in lengths)

def print_array(arr: any, show_index: bool = False) -> None:
    """
    Print array elements, optionally with their indices.

    Prints each element of a 1D array on a separate line.
    Can optionally display the index of each element.

    Args:
        arr: 1D array to print
        show_index: If True, display index with each element (default: False)

    Returns:
        None

    Raises:
        TypeError: If input is not a 1D array
    """
    arr = single_array(arr)

    for index, item in enumerate(arr):
        if show_index:
            print(f"{item}, {index}.")
        else:
            print(item)

    return

def sort_array_ascending(arr: any) -> any:
    """
    Sort a 1D array in ascending order.

    Returns a new sorted array in ascending order (smallest to largest).

    Args:
        arr: 1D array to sort

    Returns:
        numpy.ndarray: Sorted array in ascending order

    Raises:
        TypeError: If input is not a 1D array
    """

    arr = single_array(arr)
    return np.sort(arr)

def sort_array_descending(arr: any) -> any:
    """
    Sort a 1D array in descending order.

    Returns a new sorted array in descending order (largest to smallest).

    Args:
        arr: 1D array to sort

    Returns:
        numpy.ndarray: Sorted array in descending order

    Raises:
        TypeError: If input is not a 1D array
    """

    arr = single_array(arr)
    return np.sort(arr)[::-1]

def first_element(arr: any) -> any:
    """
    Get the first element of a 1D array.

    Returns the element at index 0.

    Args:
        arr: 1D array to get element from

    Returns:
        any: First element of the array

    Raises:
        TypeError: If input is not a 1D array
        IndexError: If array is empty
    """
    arr = single_array(arr)

    if len(arr) == 0:
        raise IndexError("Error: Cannot get first element of empty array")

    return arr[0]

def last_element(arr: any) -> any:
    """
    Get the last element of a 1D array.

    Returns the element at index -1.

    Args:
        arr: 1D array to get element from

    Returns:
        any: Last element of the array

    Raises:
        TypeError: If input is not a 1D array
        IndexError: If array is empty
    """
    arr = single_array(arr)

    if len(arr) == 0:
        raise IndexError("Error: Cannot get last element of empty array")

    return arr[-1]

def array_length(arr: any) -> int:
    """
    Get the length of a 1D array.

    Returns the number of elements in the array.

    Args:
        arr: 1D array to get length from

    Returns:
        int: Number of elements in the array

    Raises:
        TypeError: If input is not a 1D array
    """
    arr = single_array(arr)
    return len(arr)

def remove_at_index(arr: any, index: int = 0) -> any:
    """
    Remove an element at a specific index from a 1D array.

    Returns a new array with the element at the specified index removed.

    Args:
        arr: 1D array to remove from
        index: Index of element to remove (default: 0)

    Returns:
        numpy.ndarray: New array with element removed

    Raises:
        TypeError: If input is not a 1D array or index is not an integer
        IndexError: If index is out of bounds
    """
    import numpy as np

    arr = single_array(arr)
    index = valid_int(index)

    if index < -len(arr) or index >= len(arr):
        raise IndexError(
            f"Error: Index {index} out of bounds for array of length {len(arr)}"
        )

    return np.delete(arr, index)

def remove_first_element(arr: any) -> any:
    """
    Remove the first element from a 1D array.

    Returns a new array with the first element removed.

    Args:
        arr: 1D array to remove from

    Returns:
        numpy.ndarray: New array with first element removed

    Raises:
        TypeError: If input is not a 1D array
        IndexError: If array is empty
    """
    arr = single_array(arr)

    if len(arr) == 0:
        raise IndexError("Cannot remove from empty array")

    return remove_at_index(arr, 0)

def remove_last_element(arr: any) -> any:
    """
    Remove the last element from a 1D array.

    Returns a new array with the last element removed.

    Args:
        arr: 1D array to remove from

    Returns:
        numpy.ndarray: New array with last element removed

    Raises:
        TypeError: If input is not a 1D array
        IndexError: If array is empty
    """
    arr = single_array(arr)

    if len(arr) == 0:
        raise IndexError("Cannot remove from empty array")

    return remove_at_index(arr, -1)
