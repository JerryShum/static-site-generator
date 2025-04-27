import unittest

from functions.markdownfunctions import text_to_textnodes
from textnode import TextNode, TextType


class Test_Text_To_Node(unittest.TestCase):
    def test_text_to_textnodes_simple(self):
        text = "This is plain text"
        nodes = text_to_textnodes(text)
        expected = [
            TextNode("This is plain text", TextType.TEXT),
        ]
        self.assertEqual(nodes, expected)
        
    def test_text_to_textnodes_complex(self):
        text = "This is plain text with **bold** and _italic_"
        nodes = text_to_textnodes(text)
        expected = [
            TextNode("This is plain text with ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" and ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
        ]
        self.assertEqual(nodes, expected)
    
    def test_text_to_textnodes_complex2(self):
        text = "This is plain text with **bold** and _italic_ and `code`"
        nodes = text_to_textnodes(text)
        expected = [
            TextNode("This is plain text with ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" and ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" and ", TextType.TEXT),
            TextNode("code", TextType.CODE),
        ]
        self.assertEqual(nodes, expected)


if __name__ == "__main__":
    unittest.main()
