#!/usr/bin/env python3
import unittest
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test cases for GithubOrgClient"""

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test public_repos method with mocked get_json and _public_repos_url"""
        # Define the test payload
        test_payload = [
            {"name": "repo1", "license": {"key": "mit"}},
            {"name": "repo2", "license": {"key": "apache-2.0"}},
            {"name": "repo3", "license": None}
        ]

        # Mock get_json to return our test payload
        mock_get_json.return_value = test_payload

        # Define the expected repos list
        expected_repos = ["repo1", "repo2", "repo3"]

        # Mock the _public_repos_url property
        with patch.object(
                GithubOrgClient,
                '_public_repos_url',
                new_callable=PropertyMock,
                return_value="https://api.github.com/orgs/test-org/repos"
        ) as mock_public_repos_url:
            # Create an instance of GithubOrgClient
            client = GithubOrgClient("test-org")

            # Call the method under test
            repos = client.public_repos()

            # Assert that the returned repos match our expected list
            self.assertEqual(repos, expected_repos)

            # Assert that _public_repos_url property was called once
            mock_public_repos_url.assert_called_once()

            # Assert that get_json was called once
            mock_get_json.assert_called_once()

