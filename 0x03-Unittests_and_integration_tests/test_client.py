#!/usr/bin/env python3
"""Integration tests for GithubOrgClient.public_repos"""
import unittest
from unittest.mock import patch, PropertyMock, Mock
from parameterized import parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


@parameterized_class([
    {
        "org_payload": TEST_PAYLOAD[0][0],
        "repos_payload": TEST_PAYLOAD[0][1],
        "expected_repos": TEST_PAYLOAD[0][2],
        "apache2_repos": TEST_PAYLOAD[0][3]
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient.public_repos"""

    @classmethod
    def setUpClass(cls):
        """Set up class fixtures before running tests"""
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        def side_effect(url):
            """Return different payloads based on URL"""
            if url == "https://api.github.com/orgs/google":
                return Mock(json=lambda: cls.org_payload)
            elif url == "https://api.github.com/orgs/google/repos":
                return Mock(json=lambda: cls.repos_payload)
            return None

        cls.mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        """Stop the patcher after running tests"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test public_repos without license filter"""
        client = GithubOrgClient("google")
        repos = client.public_repos()
        self.assertEqual(repos, self.expected_repos)
        
        # Verify the mock was called with the correct URLs
        self.assertEqual(self.mock_get.call_count, 2)
        expected_urls = [
            "https://api.github.com/orgs/google",
            "https://api.github.com/orgs/google/repos"
        ]
        actual_urls = [call[0][0] for call in self.mock_get.call_args_list]
        self.assertEqual(actual_urls, expected_urls)

    def test_public_repos_with_license(self):
        """Test public_repos with Apache 2.0 license filter"""
        client = GithubOrgClient("google")
        repos = client.public_repos(license="apache-2.0")
        self.assertEqual(repos, self.apache2_repos)
        
        # Verify only Apache-licensed repos are returned
        for repo in repos:
            self.assertIn(repo, ['repo1', 'repo3'])
        
