import re
import textwrap

from textnode import TextNode, TextType
from htmlnode import HTMLNode, text_node_to_html_node
from parentnode import ParentNode
from functions.markdownblocks import block_to_block_type, BlockType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        images = extract_markdown_images(original_text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(
                TextNode(
                    image[0],
                    TextType.IMAGE,
                    image[1],
                )
            )
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes


def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches


def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches



def text_to_textnodes(text):
    new_nodes = []
    
    # Normalize line breaks to space
    normalized_text = re.sub(r"\s*\n\s*", " ", text.strip())
    
    new_nodes.append(TextNode(normalized_text, TextType.TEXT))
    
    new_nodes = split_nodes_delimiter(new_nodes, "**", TextType.BOLD)
    new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
    new_nodes = split_nodes_delimiter(new_nodes, "`", TextType.CODE)
    new_nodes = split_nodes_image(new_nodes)
    new_nodes = split_nodes_link(new_nodes)
    
    return new_nodes


def markdown_to_blocks(markdown):
    blockstoreturn = []
    
    for block in markdown.split("\n\n"):
        print("block:")
        print(block)
        if block.strip() != "":
            blockstoreturn.append(block.strip())
            
    return blockstoreturn

def text_to_children(text):
    children_nodes = []
    
    #@ Convert to text nodes first
    text_nodes = text_to_textnodes(text)
    
    #@ Convert text nodes to html nodes
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children_nodes.append(html_node)
        
           #@ Converting text to textnodes
                # # [TextNode("This is ", TEXT), TextNode("bold", BOLD), TextNode(" heading", TEXT)]
                
                # text_nodes = text_to_textnodes(after)
                
                # for text_node in text_nodes:
                #     #@ convert textnodes into html nodes
                #     # HTMLNode(None, "This is ")
                #     # HTMLNode("b", None, [HTMLNode(None, "bold")])
                #     # HTMLNode(None, " heading")

                    
                #     html_node = text_node_to_html_node(text_node)
                #     childrenNodes.append(html_node)
                    
                # headingBlockNode = HTMLNode(headingtag, None, childrenNodes)
                # # HTMLNode("h1", None, children = [HTMLNode(None, "This is "), HTMLNode("b", None, [HTMLNode(None, "bold")]), HTMLNode(None, " heading")])
        
    return children_nodes
        
        
def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    overallhtmlnodes = []
    
    for block in blocks:
        blockType = block_to_block_type(block)
        # Based on blocktype -> create associated htmlnode
        # Blocktypes: heading, code, quote, unordered_list, ordered_list, paragraph
        match(blockType):
            case BlockType.heading:
                #! find number of # in heading of block
                # ##### heading 1
                #@ Splits the heading into before and after (before is the ####, after is the rest after the space)
                # ["# This is **bold** heading", "This is a paragraph with _italic_ text."]
                before,after = block.split(" ", 1)
                
                headingtag = f"h{len(before)}"
                childrenNodes = text_to_children(after)
                headingBlockNode = HTMLNode(headingtag, None, childrenNodes)
                
     
                overallhtmlnodes.append(headingBlockNode)
                
                
            case BlockType.code:
                    # gets rid of the first 3 and last 3 characters (```), dedent code
                content = textwrap.dedent(block[3:-3]).strip() + "\n"
                
                text_node = TextNode(content, TextType.TEXT)
                code_node = text_node_to_html_node(text_node)
                
                code_html_node = HTMLNode("code", None, [code_node])
                structured_code_html_node = HTMLNode("pre", None, [code_html_node])
                overallhtmlnodes.append(structured_code_html_node)
                
            case BlockType.quote:
                # quotes have lines that start with >
                # strip all lines of the >
                lines = block.split("\n")
                quote_content = ""
                
                for line in lines:
                    if line.startswith(">"):
                        quote_content += line[1:].lstrip() + " "
                
                childrenNodes = text_to_children(quote_content.strip())
                
                #@ quote block node:
                quoteBlockNode = HTMLNode("blockquote", None, childrenNodes)
                overallhtmlnodes.append(quoteBlockNode)                    
                
            case BlockType.unordered_list:
                # unordered lists have lines that start with -
                # strip all lines of - and conver them to the appropriate text
                
                lines = block.split("\n")
                blockChildren = []
                
                for line in lines:
                    # handle the inline formatting (bold, italic, etc.)
                    if line.startswith("-"):
                        inlineHTML = text_to_children(line[1:].strip())
                        # wrap in li
                        blockChild = HTMLNode("li", None, inlineHTML)
                        blockChildren.append(blockChild)
                
                unordered_list_node = HTMLNode("ul", None, blockChildren)
                overallhtmlnodes.append(unordered_list_node)
                        
                
            case BlockType.ordered_list:
                # ordered lists start with number and . (1.)
                # strip all lines of 1. and convert them to inline children and then wrap
                
                lines = block.split("\n")
                blockChildren = []
                
                for line in lines:
                    # checks if the first char is a digit followed by a .
                    if re.match(r"^\d+\.\s", line):
                        inlinecontent = line[2:].strip()
                        inlineHTML = text_to_children(inlinecontent)
                        
                        # wrap in li
                        blockChild = HTMLNode("li", None, inlineHTML)
                        blockChildren.append(blockChild)
                
                ordered_list_node = HTMLNode("ol", None, blockChildren)
                overallhtmlnodes.append(ordered_list_node)
                        
                
            case BlockType.paragraph:
                
                inlineHTML = text_to_children(block.strip())
                
                paragraphNode = HTMLNode("p", None, inlineHTML)
                overallhtmlnodes.append(paragraphNode)
    
    parentNode = HTMLNode("div",None, overallhtmlnodes)
    return parentNode
        
    