#!/usr/bin/env python3

"""client.py - GitHub API client implementation"""
import requests
from typing import List, Dict, Optional


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

    def public_repos(self, license: Optional[str] = None) -> List[str]:
        """
        Get list of public repository names, optionally filtered by license
        
        Args:
            license: Optional license key to filter by
            
        Returns:
            List of repository names
        """
        repos_data = get_json(self._public_repos_url)
        
        if license:
            return [
                repo["name"] for repo in repos_data
                if repo.get("license", {}).get("key") == license
            ]
        return [repo["name"] for repo in repos_data]
    
