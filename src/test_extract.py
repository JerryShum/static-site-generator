import unittest

from functions.extract_markdown import extract_markdown_images, extract_markdown_links

class TestExtractURL(unittest.TestCase):
    
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
        
    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://www.boot.dev)"
        )
        self.assertListEqual([("link", "https://www.boot.dev")], matches)
    
        
    def test_extract_markdown_images_with_multiple(self):
        matches = extract_markdown_images(
            """
            This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)
            and another ![image2](https://i.imgur.com/Vb7Ht4V.png)
            """
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png"), 
                              ("image2", "https://i.imgur.com/Vb7Ht4V.png")], matches)
        
    def test_extract_markdown_links_with_multiple(self):
        matches = extract_markdown_links(
            """
            This is text with a [link](https://www.boot.dev)
            and another [link2](https://www.google.com)
            """
        )
        self.assertListEqual([("link", "https://www.boot.dev"), 
                              ("link2", "https://www.google.com")], matches)
   
   
        


if __name__ == "__main__":
    unittest.main()