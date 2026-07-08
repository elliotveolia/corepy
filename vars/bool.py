def valid_bool(value: bool) -> bool:
    """
    Validate that input is a boolean.

    Args:
        value: The value to validate

    Returns:
        bool: The validated boolean

    Raises:
        TypeError: If input is not a boolean
    """
    if not isinstance(value, bool):
        raise TypeError(
            f"Error: Argument {value} needs to be a boolean type, "
            f"instead type of {type(value)}."
        )
    return value

def logic_and(a: bool, b: bool) -> bool:
    """
    Perform logical AND operation on two booleans.

    Args:
        a: First boolean value
        b: Second boolean value

    Returns:
        bool: Result of a AND b

    Raises:
        TypeError: If either argument is not a boolean
    """
    valid_bool(a)
    valid_bool(b)
    return a and b

def logic_nand(a: bool, b: bool) -> bool:
    """
    Perform logical NAND operation on two booleans.

    NAND returns False only when both inputs are True,
    otherwise returns True.

    Args:
        a: First boolean value
        b: Second boolean value

    Returns:
        bool: Result of NAND operation

    Raises:
        TypeError: If either argument is not a boolean
    """
    valid_bool(a)
    valid_bool(b)
    return not (a and b)

def logic_or(a: bool, b: bool) -> bool:
    """
    Perform logical OR operation on two booleans.

    OR returns True if at least one input is True,
    otherwise returns False.

    Args:
        a: First boolean value
        b: Second boolean value

    Returns:
        bool: Result of OR operation

    Raises:
        TypeError: If either argument is not a boolean
    """
    valid_bool(a)
    valid_bool(b)
    return a or b

def logic_xor(a: bool, b: bool) -> bool:
    """
    Perform logical XOR operation on two booleans.

    XOR returns True if the inputs are different,
    otherwise returns False.

    Args:
        a: First boolean value
        b: Second boolean value

    Returns:
        bool: Result of XOR operation

    Raises:
        TypeError: If either argument is not a boolean
    """
    valid_bool(a)
    valid_bool(b)
    return a != b

def logic_not(a: bool) -> bool:
    """
    Perform logical NOT operation on a boolean.

    NOT returns the opposite of the input value.

    Args:
        a: Boolean value to negate

    Returns:
        bool: Negated boolean value

    Raises:
        TypeError: If argument is not a boolean
    """
    valid_bool(a)
    return not a

def logic_nor(a: bool, b: bool) -> bool:
    """
    Perform logical NOR operation on two booleans.

    NOR returns True only when both inputs are False,
    otherwise returns False.

    Args:
        a: First boolean value
        b: Second boolean value

    Returns:
        bool: Result of NOR operation

    Raises:
        TypeError: If either argument is not a boolean
    """
    valid_bool(a)
    valid_bool(b)
    return not (a or b)

def logic_xnor(a: bool, b: bool) -> bool:
    """
    Perform logical XNOR operation on two booleans.

    XNOR returns True if the inputs are the same,
    otherwise returns False.

    Args:
        a: First boolean value
        b: Second boolean value

    Returns:
        bool: Result of XNOR operation

    Raises:
        TypeError: If either argument is not a boolean
    """
    valid_bool(a)
    valid_bool(b)
    return a == b
