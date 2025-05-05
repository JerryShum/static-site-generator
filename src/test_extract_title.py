import unittest

from functions.extract_title import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        md = "# Test Title\n\nThis is a test"
        self.assertEqual(extract_title(md), "Test Title")
        
    def test_extract_title_advanced(self):
        md = "# Test Title\n\nThis is a test \n\n # Test Title\n\nThis is a test"
        self.assertEqual(extract_title(md), "Test Title")

    def test_extract_title_fails(self):
        md = "This is a test"
        with self.assertRaises(Exception):
            extract_title(md)


if __name__ == "__main__":
    unittest.main()
