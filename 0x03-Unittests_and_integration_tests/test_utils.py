# !/usr/bin/env python3
"""Test module for utils.memoize decorator."""
import unittest
from unittest.mock import patch
from utils import memoize


class TestMemoize(unittest.TestCase):
    """Test class for memoize decorator."""

    def test_memoize(self) -> None:
        """Test that memoize caches the result properly."""

        class TestClass:
            """Test class with memoized property."""

            def a_method(self) -> int:
                """Method to be mocked."""
                return 42

            @memoize
            def a_property(self) -> int:
                """Memoized property that calls a_method."""
                return self.a_method()

        # Create instance of test class
        test_instance = TestClass()

        # Patch a_method to track calls and return 42
        with patch.object(TestClass, 'a_method', return_value=42) as mock_method:
            # First call - should call a_method
            result1 = test_instance.a_property()
            # Second call - should use cached result
            result2 = test_instance.a_property()

            # Verify results are correct
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)

            # Verify a_method was called only once
            mock_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()
