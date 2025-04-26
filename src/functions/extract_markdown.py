import re

def extract_markdown_images(text):
    alt = re.findall(r"!\[([^\[\]]*)\]", text)
    imageURL = re.findall(r"\(([^\(\)]*)\)", text)
    
    return list(zip(alt, imageURL))

def extract_markdown_links(text):
    alt = re.findall(r"\[([^\[\]]*)\]", text)
    linkURL = re.findall(r"\(([^\(\)]*)\)", text)
    
    return list(zip(alt, linkURL))
    
