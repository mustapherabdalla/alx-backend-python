#!/usr/bin/env python3
"""Client for interacting with GitHub organizations API."""
from typing import Dict
from utils import get_json


class GithubOrgClient:
    """Client for fetching GitHub organization information."""

    def __init__(self, org_name: str) -> None:
        """Initialize with an organization name.

        Args:
            org_name: Name of the GitHub organization
        """
        self._org_name = org_name

    @property
    def org(self) -> Dict:
        """Fetch organization information.

        Returns:
            Dictionary containing organization data from GitHub API
        """
        url = f"https://api.github.com/orgs/{self._org_name}"
        return get_json(url)
