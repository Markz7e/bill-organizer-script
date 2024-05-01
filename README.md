# bill-organizer
A Python3-base script to automate the organization of bills (or any other file) based on the creation datetime from each matching file.

This script was created with the intention of being used with cron, Windows Task Manager or other tool that automate its execution.

## Setup
There's two ways to set up:
- By creating an .env file
- By setting up the configuration variables inside 'bill-organizer.py'

### Creating an .env file:
Create a new .env file at the same level of 'bill-organizer.py' script as the one bellow:
```
BASE_PATH = "C:/xxxx/yyyy/Downloads"
DEST_PATH = "C:/xxxx/yyyy/Documents/Bills"
MOVE_FILE = False
MATCH_PREFIX = "receipt"
```

The ```MATCH_PREFIX``` is the word that needs to match with the files you want to organize.

Please note, the ```MOVE_FILE``` variable is a boolean, which if set as TRUE, it will move the matching files to the specified ```DEST_PATH```, if is set as FALSE, the matching files will be copied instead.

### Setting up the configuration variables inside 'bill-organizer.py'
In order to use the configuration variables already declared, first, comment the following code block within ```bill-organizer.py```:

```
### Comment the following code
load_dotenv()
base_path = str(os.getenv('BASE_PATH'))
dest_path = str(os.getenv('DEST_PATH'))
move_file = bool(os.getenv('MOVE_FILE'))
matching_prefix = str(os.getenv('MATCH_PREFIX'))
### End of comment
```

Then, uncomment the following code block and update as you require:
```
## If you want to use os-based paths, you're free to comment the previous 
## block of settings and uncomment + tweak the following block:
# base_path = str(pathlib.Path.home() / "Downloads")
# dest_path = str (pathlib.Path.home() / "Documents/Bills")
# move_file = False
# matching_prefix = 'receipt'
```

## Run
You can run the script using ```python3 bill-organizer.py``` or setting it up on cron or Windows Task Manager.

## Contact me
For further support you can contact me via my email dev.mbarrera@gmail.com
Thank you.