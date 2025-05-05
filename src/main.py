from textnode import TextNode
from functions.copy_static import copy_static
from functions.pagegeneration.generate_page import generate_page

def main():    
    copy_static("public", "static")
    generate_page("content/index.md", "template.html", "public/index.html")

    
    
    

main()