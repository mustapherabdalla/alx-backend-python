#!/usr/bin/env python3

import requests
from typing import Dict, List


def get_json(url: str) -> Dict:
    """Get JSON from a URL"""
    response = requests.get(url)
    return response.json()


class GithubOrgClient:
    """A client for GitHub organization operations"""

    def __init__(self, org_name: str) -> None:
        """Initialize with organization name"""
        self._org_name = org_name

    @property
    def _public_repos_url(self) -> str:
        """URL for organization's public repos"""
        return f"https://api.github.com/orgs/{self._org_name}/repos"

    def public_repos(self) -> List[str]:
        """Get list of public repository names"""
        repos_data = get_json(self._public_repos_url)
        return [repo["name"] for repo in repos_data]

    def has_license(self, repo: Dict, license_key: str) -> bool:
        """
        Check if a repository has a specific license

        Args:
            repo: Dictionary containing repo information
            license_key: The license key to check for

        Returns:
            bool: True if the repo has the license, False otherwise
        """
        return repo.get("license", {}).get("key") == license_key
