#!/usr/bin/env python3
import requests
from typing import List, Dict


def get_json(url: str) -> Dict:
    """
    Get JSON data from a URL

    Args:
        url: The URL to fetch JSON data from

    Returns:
        A dictionary containing the JSON response
    """
    response = requests.get(url)
    return response.json()


class GithubOrgClient:
    """A client for GitHub organization operations"""

    def __init__(self, org_name: str) -> None:
        """
        Initialize the client with an organization name

        Args:
            org_name: Name of the GitHub organization
        """
        self._org_name = org_name

    @property
    def _public_repos_url(self) -> str:
        """
        Get the URL for the organization's public repositories

        Returns:
            The API URL for public repos
        """
        return f"https://api.github.com/orgs/{self._org_name}/repos"

    def public_repos(self) -> List[str]:
        """
        Get the list of public repository names for the organization

        Returns:
            List of repository names
        """
        repos_data = get_json(self._public_repos_url)
        return [repo["name"] for repo in repos_data]
