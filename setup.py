from setuptools import find_packages
from typing import List
from setuptools import setup


HYPHER_E_DOT = "-e ."
def get_requirements(file_path:str)->List[str]:

    # requirements.txt installation

    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", " ") for req in requirements]

        if HYPHER_E_DOT in requirements:
            requirements.remove(HYPHER_E_DOT)

    return requirements            

setup(
    name = 'mlproject',
    version = '0.0.1',
    author = 'Cypher',
    author_email = 'pateladitya2004@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)