# test_anchorearn.py
"""
Tests for AnchorEarn module.
"""

import unittest
from anchorearn import AnchorEarn

class TestAnchorEarn(unittest.TestCase):
    """Test cases for AnchorEarn class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AnchorEarn()
        self.assertIsInstance(instance, AnchorEarn)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AnchorEarn()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
