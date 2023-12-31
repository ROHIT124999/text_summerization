import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(messsage)s')

project_name = "TextSummerizer"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transofmation.py",
    f"src/{project_name}/components/data_validation.py",
    f"src/{project_name}/components/data_evaluation.py",
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/prediction.py",
    f"src/{project_name}/pipeline/stage_01_data_ingestion.py",
    f"src/{project_name}/pipeline/stage_02_data_validation.py",
    f"src/{project_name}/pipeline/stage_03_data_transformation.py",
    f"src/{project_name}/pipeline/model_trainer.py",
    f"src/{project_name}/pipeline/model_evaluation.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml", #to store all model related parameters
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "exp/trials.ipynb",
    "test.py"


]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    
    if filedir !="":
        os.makedirs(filedir, exist_ok =True)
        logging.info(f"creting Directory: {filedir} for thr file {filename}")

    if (not os.path.exists(filepath) or (os.path.getsize(filepath)==0)):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"creating file: {filepath}")
    else:
        logging.info(f"{filepath} already exists")