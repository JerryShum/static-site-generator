import unittest

from functions.markdownfunctions import markdown_to_blocks


class TestMarkdownBlocks(unittest.TestCase):
    
    def test_markdown_to_blocks(self):
        md = """This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
    """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
    
    def test_markdown_to_blocks2(self):
        md = """This is the first block with a **bolded** piece of text

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

This is the third block in the markdown

- This is a list
- with items

This is the last and final block
with a second line
        """
        
        expected = [
            "This is the first block with a **bolded** piece of text",
            "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
            "This is the third block in the markdown",
            "- This is a list\n- with items",
            "This is the last and final block\nwith a second line"
        ]
        
        self.assertEqual(markdown_to_blocks(md), expected)
   
    
        


if __name__ == "__main__":
    unittest.main()