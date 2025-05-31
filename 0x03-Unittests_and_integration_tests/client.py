#!/usr/bin/env python3
"""client.py - A client for GitHub organization APIs"""
import requests
from typing import List, Dict


def get_json(url: str) -> Dict:
    """Get JSON from URL"""
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
