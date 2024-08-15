import os
from box.exceptions import BoxValueError
import yaml
from TextSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml:str) -> ConfigBox:
    """
    Reads a YAML file and returns a ConfigBox object.

    Args:
        path_to_yaml (str): Path to the YAML file.
    
    Raises:
        ValueError: If the YAML file is empty 
        e: empty file
    
    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f'yaml file {path_to_yaml} loaded successfully')
    except BoxValueError:
        raise ValueError(f'The YAML file is empty')
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_directories: list, verbose= True):
    """
    Creates list of directories

    Args:
        path_to_directories (list): List of paths to directories.
        ignore_log(bool, optional): ignore if multiple dir is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")

@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): Path to file.
    
    Returns:
        str: Size of file in KB
    """
    size_in_KB = round(os.path.getsize(path) / 1024)
    return f"~{size_in_KB} KB"