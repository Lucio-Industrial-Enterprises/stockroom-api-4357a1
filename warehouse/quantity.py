"""Parse pick-list quantities."""


def parse_quantity(value: str) -> int:
    """Return a non-negative integer quantity parsed from *value*.

    Raises ValueError for values that are not valid positive integers,
    including zero and negative numbers.
    """
    quantity = int(value.strip())
    if quantity <= 0:
        raise ValueError(f"Quantity must be a positive integer, got {quantity}")
    return quantity
