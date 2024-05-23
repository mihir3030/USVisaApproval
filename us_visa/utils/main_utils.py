import os
import yaml
from us_visa.logger import logging


def read_yaml(file_path: str) -> dict:
    try:
        with open(file_path, "rb") as yaml_file:
            logging.info(f"yaml file loded from {file_path}")
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise e

def write_yaml_file(file_path: str, content: object, replace: bool =False) -> None:
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as file:
            yaml.dump(content, file)
            logging.info(f"yaml file succefully edited at {file_path}")
    except Exception as e:
        raise e
