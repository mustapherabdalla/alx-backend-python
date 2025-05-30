#!/usr/bin/env python3
import unittest
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient

class TestGithubOrgClient(unittest.TestCase):
    def test_public_repos_url(self):
        """Test that _public_repos_url returns the correct value."""
        # Known payload to be returned by the mocked org property
        test_payload = {"repos_url": "https://api.github.com/orgs/test_org/repos"}

        # Use patch as a context manager to mock the org property
        with patch('client.GithubOrgClient.org', new_callable=PropertyMock) as mock_org:
            # Set the return value of the mocked org property
            mock_org.return_value = test_payload

            # Create an instance of GithubOrgClient
            client = GithubOrgClient("test_org")

            # Call the _public_repos_url property and assert the result
            self.assertEqual(
                client._public_repos_url,
                test_payload["repos_url"],
                "_public_repos_url did not return the expected URL"
            )

            # Ensure the org property was accessed (since it's a property)
            mock_org.assert_called_once()
