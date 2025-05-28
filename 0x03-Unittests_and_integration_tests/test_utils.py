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
