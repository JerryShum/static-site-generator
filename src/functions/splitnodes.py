from src.textnode import TextType, TextNode
from src.functions.extract_markdown import extract_markdown_images, extract_markdown_links


def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        # You only want to split a TEXT Node
        if old_node.text_type == TextType.TEXT:
            
            #! This should return a tuple of (alt, imageURL)
            results = extract_markdown_images(old_node.text)
            
            if results:
                texttosplit = old_node.text
                
                for tuple in results:
                    alt,imageURL = tuple
                    
                    #! split the original text into pieces based on the images that we find
                    # it splits the text at the specified "separator" (in this case the markdown image format)
                    # and only splits once into 2 sections (before and after the image)
                    
                    #@ beforesplit -> text that comes before the image (we can safely append this to our sections array to turn it into a textNode later)
                    #@ texttosplit -> both the original text and ALSO BECOMES the text that comes AFTER the image split 
                    # we want to split this part after for future images
                    beforeSplit, texttosplit = texttosplit.split(f"![{alt}]({imageURL})", 1)
                    print(beforeSplit)
                    print(alt, imageURL)
                    print(texttosplit)
                    
                    #! Now we can append them in order
                    # dont append empty string
                    if beforeSplit != "":
                        new_nodes.append(TextNode(beforeSplit,TextType.TEXT))
                    
                    new_nodes.append(TextNode(alt, TextType.IMAGE, imageURL))
                         
                #! Append the rest of the text after the splits
                # dont append an empty string
                if texttosplit != "":
                    new_nodes.append(TextNode(texttosplit, TextType.TEXT))
                
            else:
                new_nodes.append(old_node)
            
        else:
            raise Exception("node is not of type text")
        
    for node in new_nodes:
        print(repr(node))
        print(node.text_type, type(node.text_type))
    return new_nodes
            
    
    
def split_nodes_link(old_nodes):
    None