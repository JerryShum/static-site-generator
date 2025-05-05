import os
import shutil

def copy_static(targetdirectory, sourcedirectory):
    base_dir = os.path.dirname(os.path.abspath(__file__))  # this is /absolute/path/to/src
    project_root = os.path.abspath(os.path.join(base_dir, "../..")) #moves up one directory
 
    target = os.path.join(project_root, targetdirectory)
    source = os.path.join(project_root, sourcedirectory)
    
    if os.path.exists(target):
    
        #! Getting rid of the target contents
        entries = os.listdir(target)
        # name of the file/directory (index.css), (/files)
        
        for entry in entries:
            full_path = os.path.join(target, entry)
            # /public/index.css
            print("deleting:")
            print(full_path)
            
            if os.path.isfile(full_path):
                os.remove(full_path)
            
            elif os.path.isdir(full_path):
                shutil.rmtree(full_path)
        
        #! Copying content from one source to target directory
        
        sourceEntries = os.listdir(source)
        
        for entry in sourceEntries:
            full_path = os.path.join(source, entry)
            
            print("copying:")
            print(full_path)
            
            if os.path.isfile(full_path):
                shutil.copy(full_path, target)
            
            elif os.path.isdir(full_path):
                shutil.copytree(full_path, os.path.join(target, entry))
        
        
    else:
        raise Exception("targetdirectory does not exist")