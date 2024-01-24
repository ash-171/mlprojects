from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str) -> List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        # in requirements.text after each package name
        # \n will be there. The following line is to remove it.
        #  -e . in requirements.txt is to trigger the setup.py file
        requirements = [req.replace('\n',"") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements
        

setup(
    name='mlproject',
    version='1.0.0',
    author='Aswathi',
    author_email='mailaswathits@gmail.com',
    # url='https://github.com/ash-171/mlproject',
    license='MIT',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)