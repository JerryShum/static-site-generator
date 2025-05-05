import os
from functions.markdownfunctions import *
from functions.extract_title import extract_title

def generate_page(from_path, template_path=None, dest_path=None):
    current_dir = os.path.dirname(os.path.abspath(__file__))  # location of generate_page.py
    project_root = os.path.abspath(os.path.join(current_dir, "../../.."))
    absolute_from_path = os.path.join(project_root, from_path)
    absolute_template_path = os.path.join(project_root, template_path)
    absolute_dest_path = os.path.join(project_root, dest_path)

    print(f"Generating page from {absolute_from_path} to {absolute_dest_path} using {absolute_template_path}")
    
    #! Read the md file 
    with open(absolute_from_path, "r", encoding="utf-8") as file:
        mdcontent = file.read()
    
    #! Read the template file
    with open(absolute_template_path, "r", encoding="utf-8") as file:
        template = file.read()
        
    builtHTML = ""
    htmlNode = markdown_to_html_node(mdcontent)
    title = extract_title(mdcontent)
    
   
    builtHTML += htmlNode.to_html()
        
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", builtHTML)
    
    #! Make the destination directory if it doesn't exist
    if not os.path.exists(os.path.dirname(absolute_dest_path)):
        os.makedirs(os.path.dirname(absolute_dest_path))
    
    
    
    with open(absolute_dest_path, "w", encoding="utf-8") as file:
        file.write(template)
        
    
        
    print(mdcontent)
    print(template)