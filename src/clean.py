import shutil
from pathlib import Path

from collections import Counter

class CleanDirectory:
    def __init__(self, directory):
        self.directory = Path(directory)
        if not self.directory.exists():
            raise FileNotFoundError(f"{self.directory} does not exists")
        
    
    file_type_dest = {
    '.png': 'image',
    '.mp3': 'music',
    '.pdf': 'document',
    '.txt': 'document',
    '.jpg': 'image',
    '.json': 'data',
    '.mp4': 'movie',
    '.enc': 'data',
    '.ogg': 'data',
    '.exe': 'data',
    '.jpeg': 'image',
    '.ini': 'data',
    '.JPG': 'image'}
        
    
    DIR_PATH = Path('/mnt/c/Users/Mat/Documents')
    
    file_extensions = []
    for file_path in DIR_PATH.iterdir():
        
        #ignore directories
        if file_path.is_dir():
            continue
            
        #ignore hidden files
        if file_path.name.startswith('.'):
            continue
        
        #get all file types
        file_extensions.append(file_path.suffix)
        
        #move files
        if file_path.suffix not in file_type_dest:
            DEST_DIR = DIR_PATH / 'others'
        else:
            DEST_DIR = DIR_PATH / file_type_dest[file_path.suffix]
        
        DEST_DIR.mkdir(exist_ok=True)

        # if not DEST_DIR.sexists():
        #     DEST_DIR.mkdir()

        print(f'{file_path.suffix:10} {DEST_DIR}')
        shutil.move(str(file_path), str(DEST_DIR))
   
   
   
if __name__ == "__main__":
    org_files = CleanDirectory('/mnt/c/Users/Mat/Documents') 