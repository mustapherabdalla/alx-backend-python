# #!/usr/bin/env python3
# """Test module for utils.access_nested_map function.
# This module contains unit tests for the access_nested_map function
# which retrieves values from nested dictionaries using a path tuple.
# """
# import unittest
# from parameterized import parameterized
# from utils import access_nested_map
#
#
# class TestAccessNestedMap(unittest.TestCase):
#     """Test class for access_nested_map function.
#
#     This class contains test cases to verify the correct behavior
#     of the access_nested_map function with various nested dictionary
#     structures and path configurations.
#     """
#
#     @parameterized.expand([
#         ({"a": 1}, ("a",), 1),
#         ({"a": {"b": 2}}, ("a",), {"b": 2}),
#         ({"a": {"b": 2}}, ("a", "b"), 2),
#     ])
#     def test_access_nested_map(self, nested_map: dict, path: tuple, expected: any) -> None:
#         """Test access_nested_map returns the expected result.
#
#         Args:
#             nested_map: A nested dictionary to test
#             path: Tuple representing the path to the value
#             expected: The expected result from the function
#         """
#         self.assertEqual(access_nested_map(nested_map, path), expected)
#
#     @parameterized.expand([
#         ({}, ("a",), "a"),
#         ({"a": 1}, ("a", "b"), "b"),
#     ])
#     def test_access_nested_map_exception(self, nested_map, path, expected_key):
#         """Test access_nested_map raises KeyError with expected message."""
#         with self.assertRaises(KeyError) as context:
#             access_nested_map(nested_map, path)
#         self.assertEqual(str(context.exception), f"'{expected_key}'")
#
#
# if __name__ == '__main__':
#     unittest.main()
#
# !/usr/bin/env python3
"""Test module for utils.get_json function."""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import get_json


class TestGetJson(unittest.TestCase):
    """Test class for get_json function."""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url: str, test_payload: dict) -> None:
        """Test get_json returns the expected result without making actual HTTP calls.

        Args:
            test_url: URL to mock
            test_payload: Expected JSON response
        """
        # Create a mock response object
        mock_response = Mock()
        mock_response.json.return_value = test_payload

        # Patch requests.get to return our mock response
        with patch('requests.get', return_value=mock_response) as mock_get:
            # Call the function
            result = get_json(test_url)

            # Verify requests.get was called exactly once with test_url
            mock_get.assert_called_once_with(test_url)

            # Verify the result matches test_payload
            self.assertEqual(result, test_payload)


if __name__ == '__main__':
    unittest.main()
