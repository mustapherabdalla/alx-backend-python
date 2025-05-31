"""Test fixtures for integration tests"""
TEST_PAYLOAD = [
    (
        {"login": "google", "id": 1342004},  # org_payload
        [  # repos_payload
            {"name": "repo1", "license": {"key": "apache-2.0"}},
            {"name": "repo2", "license": {"key": "mit"}},
            {"name": "repo3", "license": {"key": "apache-2.0"}}
        ],
        ["repo1", "repo2", "repo3"],  # expected_repos
        ["repo1", "repo3"]  # apache2_repos
    )
]
