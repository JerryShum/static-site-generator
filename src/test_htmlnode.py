import unittest

from htmlnode import HTMLNode


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

    
    
        


if __name__ == "__main__":
    unittest.main()