#In this file we are creating Project Structure templates and also logging the details of its!
import logging
import os,sys
from datetime import datetime
from pathlib import Path

project = "NEFT50"
timestamp = datetime.now().strftime(format = "%d_%m_%Y_%H_%M_%S")

FORMAT = f"[%(asctime)s]-%(lineno)d-%(message)s"


#creating an object of basicConfig class of logging module!!
logging.basicConfig(
    filename=f"{project}_{timestamp}.log",
    filemode="w",
    format = FORMAT,
    level=logging.INFO
)


#creating a list of file which was used in this project structure!!!
files = [
    ".github/workflows/.gitkeep",
    "config/config.yaml",
    "param.yaml",
    "Dockerfile",
    "main.py",
    "research/trials.ipynb",
    f"src/{project}/__init__.py",
    f"src/{project}/Exception.py",
    f"src/{project}/loggers.py",
    f"src/{project}/Components/__init__.py",
    f"src/{project}/Constants/__init__.py",
    f"src/{project}/Config/__init__.py",
    f"src/{project}/Config/configuration.py",
    f"src/{project}/Utils/__init__.py",
    f"src/{project}/Utils/common.py",
    f"src/{project}/Pipelines/__init__.py",
    f"src/{project}/Pipelines/training.py",
    f"src/{project}/Pipelines/prediction.py",
   
]

#iterating the list of file and creating directories and file init 
for filepath in files:

    #changing the filepath according windows system using path class of pathlib module
    filepath = Path(filepath)

    #spltting the filepath along with directory and filename
    dirname,filename = os.path.split(filepath)

    #now checking the directories exist or not if not then creating directories
    if dirname!= "":
        os.makedirs(dirname,exist_ok=True)
        logging.info(f"Directory {dirname} created for this filename {filename}")

    #now creating files in this directories checking exist or not and also checking size of path
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"wb") as file:
            pass  #this line create empty file in directory
        logging.info(f"File {filepath} created for this project")

    else:
        logging.info(f"File {filepath} already exist in this project")