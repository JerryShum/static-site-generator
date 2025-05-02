import unittest

from functions.markdownfunctions import markdown_to_blocks
from functions.markdownblocks import block_to_block_type, BlockType


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
   
    
 
    def test_paragraph(self):
        block = "This is a simple paragraph."
        self.assertEqual(block_to_block_type(block), BlockType.paragraph)
        
    def test_heading(self):
        # Test various heading levels
        self.assertEqual(block_to_block_type("# Heading 1"), BlockType.heading)
        self.assertEqual(block_to_block_type("## Heading 2"), BlockType.heading)
        self.assertEqual(block_to_block_type("###### Heading 6"), BlockType.heading)
        
        # Test invalid headings
        self.assertEqual(block_to_block_type("#Heading without space"), BlockType.paragraph)
        self.assertEqual(block_to_block_type("####### Too many #"), BlockType.paragraph)
        
    def test_code(self):
        self.assertEqual(block_to_block_type("```\ncode block\n```"), BlockType.code)
        # Test invalid code block
        self.assertEqual(block_to_block_type("```\ncode block without closing"), BlockType.paragraph)
        
    def test_quote(self):
        self.assertEqual(block_to_block_type(">This is a quote"), BlockType.quote)
        self.assertEqual(block_to_block_type(">Line 1\n>Line 2"), BlockType.quote)
        # Test invalid quote
        self.assertEqual(block_to_block_type(">Line 1\nLine 2 without >"), BlockType.paragraph)
        
    def test_unordered_list(self):
        self.assertEqual(block_to_block_type("- Item 1"), BlockType.unordered_list)
        self.assertEqual(block_to_block_type("- Item 1\n- Item 2"), BlockType.unordered_list)


if __name__ == "__main__":
    unittest.main()