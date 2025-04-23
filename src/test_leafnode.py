import unittest

from leafnode import LeafNode


class TestTextNode(unittest.TestCase):

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        
    def test_leaf_to_html_p2(self):
        node = LeafNode("p", "Hello, world!", {"class": "paragraphstyles"})
        self.assertEqual(node.to_html(), '<p class="paragraphstyles">Hello, world!</p>')
        
    def test_leaf_to_html_div(self):
        node = LeafNode("div", "div value", {"class" : "w-2"})
        self.assertEqual(node.to_html(), '<div class="w-2">div value</div>')

if __name__ == "__main__":
    unittest.main()