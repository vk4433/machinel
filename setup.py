from setuptools import find_packages,setup
from typing import List

text  = "-e ."

def get_requirements(file_path:str)->list[str]:
    requirements  = []
    with open (file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements = [req.replace("/n"," ") for req in requirements]

        if text in requirements:
            requirements.remove(text)
    return requirements





setup (
version="0.0.1",
name = "ml_pro",
auth_name="xyz",
mail = "poxxxxxxxx@gmail.com",
packages= find_packages(),
install_requirements = get_requirements("requirements.txt")

)