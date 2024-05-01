import shutil
import sys
import os
import pathlib
import time
from dotenv import load_dotenv
from datetime import datetime


### Settings
load_dotenv()
base_path = str(os.getenv('BASE_PATH'))
dest_path = str(os.getenv('DEST_PATH'))
move_file = os.getenv('MOVE_FILE').lower() in ('true','1','t')
matching_prefix = str(os.getenv('MATCH_PREFIX'))

## If you want to use os-based paths, you're free to comment the previous 
## block of settings and uncomment + tweak the following block:
# base_path = str(pathlib.Path.home() / "Downloads")
# dest_path = str (pathlib.Path.home() / "Documents/Bills")
# move_file = False
# matching_prefix = 'comprobante'

def main():
    print_config_set()

    directory = os.listdir(base_path)
    verify_path_exists(dest_path)

    print('Files found:')
    for fname in directory:
        if matching_prefix in fname.lower():
            print('     %s' %fname) 
            get_file_metadata(os.path.join(base_path,fname), fname, move_file)
def print_config_set():
    print("##############################")
    print("Executing bill-organizer v1.0.0")
    print("Created by: Marcos Barrera (@Markz7e on Github)")
    print("This is the configuration set:")
    print("------------------------------")
    print(f"Base path: {base_path}")
    print(f"Dest path: {dest_path}")
    print(f"Looking for files that match the word: '{matching_prefix}'")
    print(f"Operation mode: '{'Moving files' if move_file else 'Copying files'}'")
    print("------------------------------")
    print("##############################")
    print()
def verify_path_exists(path):
    if not os.path.exists(path):
        os.mkdir(path)
def get_file_metadata(baseFileDir, fileName, move): 
    ti_c = datetime.strptime(time.ctime(os.path.getctime(baseFileDir)), "%a %b %d %H:%M:%S %Y")

    verify_path_exists(os.path.join(dest_path,str(ti_c.year)))
    verify_path_exists(os.path.join(dest_path,str(ti_c.year),str(ti_c.month)))

    final_path = os.path.join(dest_path,str(ti_c.year),str(ti_c.month),fileName)
    shutil.move(baseFileDir,final_path) if move else shutil.copyfile(baseFileDir,final_path)
main()
exit()