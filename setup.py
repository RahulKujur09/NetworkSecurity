from setuptools import setup, find_packages

def get_requirements(file_path):
    """the set.py file is an essential part of packing and distributing Python project. It is used by setuptools (or distutils in older Python versions) to define the configuration of your project, such as its metadata, dependencies, and more

    Args:
        file_path (_type_): N/A

    Returns:
        _type_: list[of requirements]
    """
    HYPEN_E_DOT = "-e ."
    with open(file_path, "r") as file_obj:
        req = file_obj.readlines()
        req = [requires.strip() for requires in req]
    if HYPEN_E_DOT in req:
        req.remove(HYPEN_E_DOT)
    return req


setup(
    name="Network Security",
    version="0.0.1",
    author="Rahul Kujur",
    author_email="rahulkjr9435@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(file_path="requirements.txt")
)