from setuptools import find_packages, setup

from typing import List

"""HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements"""

setup(
    name='DimondPricePrediction',
    version='0.0.1',
    author='Abhishek Jha',
    author_email='abhishekj380@gmail.com',
    python_requires='>=3.11.3',
    install_requires=["scikit-learn", "pandas", "numpy"],
    packages=find_packages()
)
