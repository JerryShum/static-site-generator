import unittest

from parentnode import ParentNode
from leafnode import LeafNode


class TestHtmlNode(unittest.TestCase):
    
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_to_html_with_multiplechildren(self):
        child_node = LeafNode("b", "child")
        child_node2 = LeafNode("b", "child2")
        parent_node = ParentNode("div", [child_node, child_node2], {"className": "w-2 bg-black"})
        
        self.assertEqual(
            parent_node.to_html(),
            '<div className="w-2 bg-black"><b>child</b><b>child2</b></div>'
        )
        
    def test_to_html_with_no_children(self):
        parent_node = ParentNode("div", [])
        with self.assertRaises(ValueError):
            parent_node.to_html()
    

        
        
    
        


if __name__ == "__main__":
    unittest.main()