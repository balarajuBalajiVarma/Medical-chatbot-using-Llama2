import os
from pathlib import Path
import logging # it will show logs while trmplate python scriprs works

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s:')


list_of_files=[

    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "setup.py",
    "research/trails.ipynb",
    "app.py",
    "store_index.py",
    "static/.gitkeep",
    "templates/chat.html"
]

for filepath in list_of_files:

    #to make path as windows 
    filepath=Path(filepath)

    #Split filedir and filepath using split function
    filedir, filename=os.path.split(filepath)
    if filedir !='':
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the filename {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating an empty file: {filepath}")
    else:
        logging.info(f'File name already exists')


