from setuptools import find_packages, setup #Automatically find all the packages in the entire ML application
from typing import List

HYPHEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
name='mlproject',
version='0.0.1', 
author='Sakshi',
author_email='sakshi.birman.s@gmail.com',
packages=find_packages(), #find all folders with __init__.py and consider the folder as a package and try to build it as a package.
install_requires=get_requirements('requirements.txt')
)