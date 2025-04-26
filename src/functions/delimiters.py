from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    
    for old_node in old_nodes:
        
        #CHECK IF THE NODE IS TYPE TEXT (we only want to split text nodes -> no need to split other types)
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        
        if delimiter not in old_node.text:
            raise Exception("Delimiter not found, please specify a correct delimiter.")
        
        if old_node.text.count(delimiter) % 2 != 0:
            raise Exception("There must be pairs of delimiters in the text. There should be an opening delimiter and a  closing delimiter, no nesting delimiters.")
        
        splits = old_node.text.split(delimiter)
        
        for i, text in enumerate(splits):
            if i % 2 ==0:
                if text:
                    new_nodes.append(TextNode(text, old_node.text_type))
            
            else:
                if text:
                    new_nodes.append(TextNode(text, text_type))
    
    return new_nodes
            
                
                
        