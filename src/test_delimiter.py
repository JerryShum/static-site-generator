import unittest

from textnode import TextNode, TextType
from functions.delimiters import split_nodes_delimiter


class TestHtmlNode(unittest.TestCase):
    
    def test_single_code_block(self):
        node = TextNode("Hello `world`!", TextType.TEXT)
        expected = [
            TextNode("Hello ", TextType.TEXT),
            TextNode("world", TextType.CODE),
            TextNode("!", TextType.TEXT)
        ]
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(result, expected)
        
    def test_multiple_code_block(self):
        node = TextNode("Hello `world`!", TextType.TEXT)
        node2 = TextNode("Hello `world`!", TextType.TEXT)
        expected = [
            TextNode("Hello ", TextType.TEXT),
            TextNode("world", TextType.CODE),
            TextNode("!", TextType.TEXT),
            TextNode("Hello ", TextType.TEXT),
            TextNode("world", TextType.CODE),
            TextNode("!", TextType.TEXT),
        ]
        result = split_nodes_delimiter([node, node2], "`", TextType.CODE)
        self.assertEqual(result, expected)
    
    def test_bold_node(self):
        node = TextNode("Hello **world**!", TextType.TEXT)
        expected = [
            TextNode("Hello ", TextType.TEXT),
            TextNode("world", TextType.BOLD),
            TextNode("!", TextType.TEXT)
        ]
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(result, expected)
        
    def test_multiple_bold_node(self):
        node = TextNode("Hello **world**!", TextType.TEXT)
        node2 = TextNode("Hello **world**!", TextType.TEXT)
        expected = [
            TextNode("Hello ", TextType.TEXT),
            TextNode("world", TextType.BOLD),
            TextNode("!", TextType.TEXT),
            TextNode("Hello ", TextType.TEXT),
            TextNode("world", TextType.BOLD),
            TextNode("!", TextType.TEXT),
        ]
        result = split_nodes_delimiter([node, node2], "**", TextType.BOLD)
        self.assertEqual(result, expected)
    
    def test_multiple_words(self):
        node = TextNode("Hello **first world**! Hello **second world**!", TextType.TEXT)
        expected = [
            TextNode("Hello ", TextType.TEXT),
            TextNode("first world", TextType.BOLD),
            TextNode("! Hello ", TextType.TEXT),
            TextNode("second world", TextType.BOLD),
            TextNode("!", TextType.TEXT),
        ]
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(result, expected)
        
    
    def test_bold_and_italic(self):
        node = TextNode("**bold** and _italic_", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
        
        expected = [
            TextNode("bold", TextType.BOLD),
            TextNode(" and ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
        ]
        
        self.assertEqual(new_nodes, expected)
        
    
        


if __name__ == "__main__":
    unittest.main()