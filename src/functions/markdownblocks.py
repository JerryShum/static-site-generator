from enum import Enum

BlockType = Enum('BlockType', ["paragraph", "heading", "code", "quote", "unordered_list", "ordered_list"])

def block_to_block_type(block):
    if block.startswith(("#", "##", "###", "####", '#####', '######')):
        # check if theres a space after the #s
        if " " in block and block.index(" ") <= 6:
        
            #! Splits the string into before and after (before is the ####, after is the rest after the space)
            before, after = block.split(" ", 1)
            
            #! Check if all characters in before are #
            if len(before) >= 1 and all(char == "#" for char in before):
                
                #! Check if the length of before is between 1 and 6
                if 1 <= len(before) <= 6:
                    return BlockType.heading
    elif block.startswith("```"):
        if block.endswith("```"):
            return BlockType.code
     
    elif block.startswith(">"):
        lines = block.split("\n")
        
        if all(line.startswith(">") for line in lines):
            return BlockType.quote
        
    elif block.startswith("- "):
        lines = block.split("\n")
        
        if all(line.startswith("- ") for line in lines):
            return BlockType.unordered_list
        
    elif block[0].isdigit():
        lines = block.split("\n")
        isValidOrderedList = True
        
        for i, line in enumerate(lines, 1):
            expected_prefix = f"{i}. "
            
            if not line.startswith(expected_prefix):
                isValidOrderedList = False
                break
                
        if isValidOrderedList:
            return BlockType.ordered_list

    else:
        return BlockType.paragraph
    
    return BlockType.paragraph
        
    
