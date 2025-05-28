#!/usr/bin/env python3
"""Test module for utils.access_nested_map function.
This module contains unit tests for the access_nested_map function
which retrieves values from nested dictionaries using a path tuple.
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Test class for access_nested_map function.

    This class contains test cases to verify the correct behavior
    of the access_nested_map function with various nested dictionary
    structures and path configurations.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map: dict, path: tuple, expected: any) -> None:
        """Test access_nested_map returns the expected result.

        Args:
            nested_map: A nested dictionary to test
            path: Tuple representing the path to the value
            expected: The expected result from the function
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b"),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_key):
        """Test access_nested_map raises KeyError with expected message."""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), f"'{expected_key}'")


if __name__ == '__main__':
    unittest.main()

