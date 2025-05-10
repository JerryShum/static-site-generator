import os
from functions.markdownfunctions import *
from functions.extract_title import extract_title

def generate_page_recursive(from_path, template_path, dest_path):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(current_dir, "../../.."))

    absolute_from_path = os.path.join(project_root, from_path)
    absolute_template_path = os.path.join(project_root, template_path)
    absolute_dest_root = os.path.join(project_root, dest_path)

    # Read the template file once
    with open(absolute_template_path, "r", encoding="utf-8") as file:
        template_content = file.read()

    # Walk through every subdirectory in content/
    for root, dirs, files in os.walk(absolute_from_path):
        if "index.md" in files:
            md_path = os.path.join(root, "index.md")

            # Get relative path from /content
            relative_dir = os.path.relpath(root, absolute_from_path)
            
            # Destination directory: public/ + relative path
            output_dir = os.path.join(absolute_dest_root, relative_dir)
            output_file_path = os.path.join(output_dir, "index.html")

            # Read markdown
            with open(md_path, "r", encoding="utf-8") as f:
                mdcontent = f.read()

            # Convert to HTML
            html_node = markdown_to_html_node(mdcontent)
            title = extract_title(mdcontent)
            body_html = html_node.to_html()

            # Fill template
            final_html = template_content.replace("{{ Title }}", title)
            final_html = final_html.replace("{{ Content }}", body_html)

            # Ensure output directory exists
            os.makedirs(output_dir, exist_ok=True)

            # Write final HTML
            with open(output_file_path, "w", encoding="utf-8") as f:
                f.write(final_html)

            print(f"✅ Generated: {output_file_path}")
