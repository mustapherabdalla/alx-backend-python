#!/usr/bin/env python3
"""Integration tests for GithubOrgClient"""
import unittest
from unittest.mock import patch
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
    """Integration tests for GithubOrgClient"""

    @classmethod
    def setUpClass(cls):
        """Set up class fixtures before running tests"""
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        def side_effect(url):
            """Side effect function to return different payloads based on URL"""
            if url.endswith('/orgs/google'):
                return cls.mock_response(cls.org_payload)
            elif url.endswith('/orgs/google/repos'):
                return cls.mock_response(cls.repos_payload)
            return None

        cls.mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        """Stop the patcher after running tests"""
        cls.get_patcher.stop()

    @classmethod
    def mock_response(cls, payload):
        """Create a mock response with json method"""
        mock_resp = unittest.mock.Mock()
        mock_resp.json.return_value = payload
        return mock_resp

    def test_public_repos(self):
        """Test public_repos integration"""
        client = GithubOrgClient("google")
        repos = client.public_repos()
        self.assertEqual(repos, self.expected_repos)

    def test_public_repos_with_license(self):
        """Test public_repos with license filter"""
        client = GithubOrgClient("google")
        repos = client.public_repos(license="apache-2.0")
        self.assertEqual(repos, self.apache2_repos)
