# import os
# from pathlib import path
# import logging
# logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# project_name="mlproject"

# list_of_files= [
#     f"src/{project_name}/__init__.py",
#     f"src/{project_name}/components/__init__.py",
#     f"src/{project_name}/utils__init__.py",
#     f"src/{project_name}/utils/common.py",
#     f"src/{project_name}/config/__init__.py",
#     f"src/{project_name}/config/configuration.py",
#     f"src/{project_name}/pipeline/__init__.py",
#     f"src/{project_name}/entity/__init__.py",
#     f"src/{project_name}/entity/config_entity.py",
#     f"src/{project_name}/constants/__init__.py",
#     "config?config.yaml",
#     "params.yaml",
#     "schema.yaml",
#     "main.py",
#     "app.py",
#     "requirements.txt",
#     "setup.py",
#     "research/trials.ipynb",
#     "template/index.html",
# ]
# for filepath in list_of_files:
#     filepath=path(filepath)
#     filedir, filename = os.path.split(filepath)

#     if filedir !="":
#      os.markdirs(filedir, exist_ok=True)
#      logging.info(f"Creating directory; {filedir} for the file: {filename}")

#     if(not os.path.exists(filepath)) or (os.path.getsize(filepath)== 0):
#         with open(filepath, "w") as f:
#             pass
#             logging.info(f"Creating empty file: {filepath}")



#     else:
#         logging.info(f"{filename} is already exists")
import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "mlproject"

list_of_files = [
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",  # Corrected typo in filename
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",  # Fixed the typo in the path
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "template/index.html",
]

for filepath in list_of_files:
    filepath = Path(filepath)  # Use pathlib.Path to handle file paths
    filedir, filename = os.path.split(filepath)

    # Create the directory if it does not exist
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    # Create the file if it does not exist or if it is empty
    if not filepath.exists() or filepath.stat().st_size == 0:
        with open(filepath, "w"):
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")
