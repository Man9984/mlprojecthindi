from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    ''' This Function will return a list of requirements'''

    reqirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        reqirements = [i.replace('\n', '') for i in requirements]

        if HYPEN_E_DOT in reqirements:
            reqirements.remove(HYPEN_E_DOT)        
        
        return requirements


setup(
name = 'ML_Project',
version = '0.0.1',
author = 'Manjeet Kumar Yadav',
author_email='manjeetyadav9984@gmail.com',
packages = find_packages(),
install_requires = get_requirements('requirements.txt')

)
