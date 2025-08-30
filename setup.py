from setuptools import setup, find_packages
from typing import List
HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]: 
    '''
    this function will return the list of requirements
    '''
    requiremnts = []
    with open(file_path) as file_obj:
        reqirements = file_obj.readlines()
        requiremnts = [req.replace("\n", "") for req in requiremnts]
        if HYPHEN_E_DOT in requiremnts:
            requiremnts.remove(HYPHEN_E_DOT)
        return requiremnts
    
setup(
    name='mlproject',
    version='0.0.1',
    author='MANAA',
    author_email='youssefa700@gmail.com',
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt')

)