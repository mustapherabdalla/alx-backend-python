#!/usr/bin/env python3
"""Utility functions for working with nested dictionaries and JSON APIs.
This module provides functions to access nested dictionary structures and
fetch JSON data from web APIs.
"""

from typing import Any, Dict, Sequence, Union
import requests


def access_nested_map(nested_map: Dict, path: Sequence) -> Any:
    """Access a value in a nested dictionary using a tuple path.

    Args:
        nested_map: The nested dictionary to access
        path: Sequence of keys representing the path to the value

    Returns:
        The value found at the specified path

    Raises:
        KeyError: If a key in the path does not exist
    """
    current = nested_map
    for key in path:
        if not isinstance(current, dict) or key not in current:
            raise KeyError(key)
        current = current[key]
    return current


def get_json(url: str) -> Dict:
    """Fetch JSON data from a given URL.

    Args:
        url: The URL to fetch JSON data from

    Returns:
        A dictionary containing the JSON response
    """
    response = requests.get(url)
    return response.json()


if __name__ == '__main__':
    """Demonstration of the utility functions."""
    # Example usage of access_nested_map
    nested = {"a": {"b": {"c": 1}}}
    print(access_nested_map(nested, ("a", "b", "c")))  # Output: 1

    # Example usage of get_json
    # Note: In practice, you'd mock this for testing
    # print(get_json("https://example.com/api/data"))
