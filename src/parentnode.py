from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag,None, children, props)
        
    def props_to_html(self):
        return super().props_to_html()
    
    def to_html(self):
        if not self.tag:
            raise ValueError

        if not self.children:
            raise ValueError("Missing Children Value")
        
        childHTML = []
            
        for childNode in self.children:
            childHTML.append(childNode.to_html())
        
        return f"<{self.tag}{self.props_to_html()}>{''.join(childHTML)}</{self.tag}>"
