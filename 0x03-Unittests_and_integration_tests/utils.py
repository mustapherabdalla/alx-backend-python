# !/usr/bin/env python3
"""Utility module containing memoization decorator.
This module provides a decorator for caching/memoizing function results.
"""

from functools import wraps
from typing import Any, Callable


def memoize(func: Callable) -> Callable:
    """Decorator that caches the result of a function call.

    Args:
        func: The function to be memoized

    Returns:
        A wrapped function that caches its results
    """
    cache = {}

    @wraps(func)
    def memoized_func(*args, **kwargs) -> Any:
        """The memoized wrapper function."""
        key = (args, frozenset(kwargs.items()))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]

    return memoized_func


if __name__ == '__main__':
    """Demonstration of memoize decorator."""


    class ExampleClass:
        def __init__(self):
            self.call_count = 0

        @memoize
        def example_method(self, x: int) -> int:
            """Example method that gets memoized."""
            self.call_count += 1
            return x * 2


    # Demonstration
    obj = ExampleClass()
    print(obj.example_method(2))  # First call - computes
    print(obj.example_method(2))  # Second call - cached
    print(f"Method was called {obj.call_count} times")  # Output: 1
