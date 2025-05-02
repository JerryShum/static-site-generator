from textnode import TextType

class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        
    def to_html(self):
    # If no tag, just return the value (text content)
        if self.tag is None:
            return self.value or ""
        
        # Create opening tag with properties
        html = f"<{self.tag}{self.props_to_html()}>"
        
        # Add value or children content
        if self.value is not None:
            html += self.value
            
        if self.children is not None:
            # If children is a single node (not in a list)
            if not isinstance(self.children, list):
                html += self.children.to_html()
            else:
                # If children is a list of nodes
                for child in self.children:
                    html += child.to_html()
            
        
        # Close the tag
        html += f"</{self.tag}>"
        
        return html

    def props_to_html(self):
        if self.props == None or len(self.props) < 1:
            return ""
        
        propsList = []
        for key in self.props:
            propsList.append(f' {key}="{self.props[key]}"')
            
        return "".join(propsList)
    
    def __repr__(self):
            return f"HTMLNode(Tag: {self.tag}, Value: {self.value}, Children: {self.children}, Props:{self.props_to_html()})"
    

def text_node_to_html_node(text_node):
    from leafnode import LeafNode
    match text_node.text_type:
            case TextType.TEXT:
                return LeafNode(None, text_node.text)
            case TextType.BOLD:
                return LeafNode("b", text_node.text)
            case TextType.ITALIC:
                return LeafNode("i", text_node.text)
            case TextType.CODE:
                return LeafNode("code", text_node.text)
            case TextType.LINK:
                return LeafNode("a", text_node.text, {"href": text_node.url})
            case TextType.IMAGE:
                return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
                   
            
        