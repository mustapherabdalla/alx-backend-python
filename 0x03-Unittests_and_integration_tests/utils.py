#!/usr/bin/env python3
"""Utility functions for working with nested dictionaries.
This module provides functions to access and manipulate nested dictionary structures.
"""

from typing import Any, Sequence


def access_nested_map(nested_map: dict, path: Sequence) -> Any:
    """Access a value in a nested dictionary using a tuple path."""
    current = nested_map
    for key in path:
        if not isinstance(current, dict) or key not in current:
            raise KeyError(key)
        current = current[key]
    return current
