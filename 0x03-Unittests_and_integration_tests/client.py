#!/usr/bin/env python3
from functools import cached_property

class GithubOrgClient:
    """A client for interacting with GitHub organization APIs."""

    def __init__(self, org_name: str):
        """Initialize the client with a GitHub organization name."""
        self._org_name = org_name

    @property
    def org(self):
        """Fetch and return the organization's data (to be mocked in tests)."""
        raise NotImplementedError("This should be mocked in tests")

    @cached_property
    def _public_repos_url(self):
        """Return the repos_url from the organization's data (memoized)."""
        return self.org["repos_url"]
