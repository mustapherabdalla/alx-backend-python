#!/usr/bin/env python3
"""Utility functions for working with nested dictionaries.
This module provides functions to access and manipulate nested dictionary structures.
"""

from typing import Any, Dict, Sequence, Union


def access_nested_map(nested_map: Dict, path: Sequence) -> Any:
    """Access a value in a nested dictionary using a tuple path.

    Args:
        nested_map: The nested dictionary to access
        path: Sequence of keys representing the path to the value

    Returns:
        The value found at the specified path

    Example:
        >>> access_nested_map({"a": {"b": 2}}, ("a", "b"))
        2
    """
    current = nested_map
    for key in path:
        if key not in current:
            raise KeyError(key)
        current = current[key]
    return current
