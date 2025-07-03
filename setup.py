from setuptools import find_packages, setup

from typing import List

requirements:List[str] = []
def get_requirements()->List[str]:
    '''
    this function will return lsit of requirements
    '''
    try:
        with open('requirements.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                if requirement and requirement != '- e.':
                    requirements.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file is not found") 

    return requirements

setup(
    name = 'NetworkSecurity',
    version = '0.0.1',
    author = "sanjay",
    author_email="sanjaymullangi@gmail.com",
    packages=find_packages(),
    install_requirements = get_requirements()

)