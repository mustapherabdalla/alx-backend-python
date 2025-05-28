#!/usr/bin/env python3
"""Test module for client.GithubOrgClient class."""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test class for GithubOrgClient."""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name: str, mock_get_json: Mock) -> None:
        """Test that GithubOrgClient.org returns correct value without making HTTP calls.

        Args:
            org_name: Name of the organization to test
            mock_get_json: Mocked get_json function
        """
        # Set up the mock return value
        test_payload = {"name": org_name, "id": 123}
        mock_get_json.return_value = test_payload

        # Create client instance and call org property
        client = GithubOrgClient(org_name)
        result = client.org

        # Verify get_json was called exactly once with correct URL
        expected_url = f"https://api.github.com/orgs/{org_name}"
        mock_get_json.assert_called_once_with(expected_url)

        # Verify the result matches the test payload
        self.assertEqual(result, test_payload)


if __name__ == '__main__':
    unittest.main()
