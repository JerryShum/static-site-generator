from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    # initiating the leaf node requires a tag and value (notice no children), props are optional
    def __init__(self, tag, value, props=None):
        # we are calling the HTMLNode constructor, tag = input tag, value = input value, children MUST BE NONE, props = None or input props
        super().__init__(tag, value, None, props)
    
    def props_to_html(self):
        return super().props_to_html()

    
    def to_html(self):
        if self.value == None:
            raise ValueError

        if self.tag == None:
            return f"{self.value}"
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

        
            