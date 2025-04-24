import unittest

from htmlnode import HTMLNode, text_node_to_html_node
from textnode import TextNode, TextType


class TestHtmlNode(unittest.TestCase):
    
    def test_props_html(self):
        node = HTMLNode("p", "this is a paragraph element", props = {"class": "paragraph"})
        self.assertEqual(node.props_to_html(), ' class="paragraph"')
    
    def test_2_props_html(self):
        node = HTMLNode("div", "this is a div element",props = {"class": "width-100"} )
        self.assertEqual(node.props_to_html(), ' class="width-100"')
        
    def test_values(self):
        node = HTMLNode("div", "div content")
        
        self.assertEqual(
            node.tag,
            "div"
        )
        
        self.assertEqual(
            node.value,
            "div content"
        )
        
        self.assertEqual(
            node.children,
            None
        )
        
        self.assertEqual(
            node.props,
            None
        )
    
    def test_repr(self):
        node = HTMLNode("div", "div value", None, {"class": "primary"})
        expectedValue = 'HTMLNode(Tag: div, Value: div value, Children: None, Props: class="primary")'
        
        self.assertEqual(repr(node), expectedValue)
        
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
        
    def test_bold(self):
        node = TextNode("This is a text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_italic(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is a text node")
        
    def test_link(self):
        node = TextNode("This is a text node", TextType.LINK, "http://example.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a text node")
        self.assertEqual(html_node.props, {"href": "http://example.com"})
        
    def test_code(self):
        node = TextNode("This is a text node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a text node")

    
    
        


if __name__ == "__main__":
    unittest.main()