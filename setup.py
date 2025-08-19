'''
The setup.py file is an essential part of packaging and 
distributing Python projects. It is used by setuptools 
(or distutils in older Python versions) to define the configuration 
of your project, such as its metadata, dependencies, and more
'''

from setuptools import find_packages, setup
from typing import List

def get_requirements() -> list[str]:
    """
    This function return list of requirements
    """
    lib_name_list:List[str] = []
    try:
        with open('requirements.txt', 'r') as req_file:
            libraries = req_file.readlines()
            for library in libraries:
                lib_name = library.strip()
                if lib_name and lib_name != '-e .':
                    lib_name_list.append(lib_name)
    except FileNotFoundError:
        print("requirements.txt not found ")

    return lib_name_list

setup(
    name = 'Network Security',
    version = '0.0.1',
    description = "",
    author = 'Bharath',
    author_email = 'bharath.vasanthkumar@gmail.com',
    maintainer = 'Bharath',
    maintainer_email = 'bharath.vasanthkumar@gmail.com',
    long_description = 'Network Security on Phising Data',
    long_description_content_type = 'E2E datascience project on Network Security on Phising Data',
    packages = find_packages(),
    install_requires = get_requirements()

)
print(get_requirements())