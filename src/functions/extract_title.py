def extract_title(markdown):
    lines = markdown.split("\n")
    marker = False
    
    for line in lines:
        strip_line = line.strip()
        if strip_line.startswith("# "):
            marker = True
            return strip_line[2:]
        
    if marker == False:
        raise Exception("No title found in markdown")
    

