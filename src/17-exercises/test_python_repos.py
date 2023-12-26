import unittest

import requests

import python_repos as pr

class TestPythonRepos(unittest.TestCase):
    """Tests for 'python_repos.py'."""

    def setUp(self):
        """Set up an API call."""
        self.r = pr.get_response()
        self.repo_dicts = pr.get_repo_dicts(self.r)
        self.response_dict = self.r.json()
        self.repo_dict_keys = self.response_dict['items'][0].keys()

    def test_get_response(self):
        """Test that we get a valid response."""
        self.assertEqual(self.r.status_code, 200)

    def test_num_repo_dicts(self):
        """Test that we get the data we think we are."""
        self.assertEqual(len(self.repo_dicts), 30)

    def test_keys_repo_dicts(self):
        """Test that repositories have the required keys."""
        required_keys = ['name', 'owner', 'stargazers_count', 'html_url']
        for key in required_keys:
            self.assertIn(key, self.repo_dict_keys)

    def test_incomplete_results(self):
        """Test that the results are complete."""
        self.assertTrue(not self.response_dict['incomplete_results'])


if __name__ == "__main__":
    unittest.main()