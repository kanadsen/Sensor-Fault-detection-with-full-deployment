from setuptools import find_packages,setup

from typing import List

REQUIREMENT_FILE_NAME="requirements.txt"
HYPHEN_E_DOT = "-e ." # to trigger the custom code setup file

def get_requirements()->List[str]: # Read each line of python file
    
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
    requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]
    
    if HYPHEN_E_DOT in requirement_list:
        requirement_list.remove(HYPHEN_E_DOT)
    return requirement_list



setup(
    name="sensor",
    version="0.0.1",
    author="Kanad sen",
    author_email="kanadsen01@gmail.com",
    packages = find_packages(), # creates packages of python sensor file. any folder containing .py extension will be made into a package
    install_requires=get_requirements(), # When setup.py is run it automatically installs requirements
)

