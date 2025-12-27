from setuptools import setup, find_packages

def get_requirements(file_path):
    HYPEN_E_DOT = "#-e ."
    with open(file_path) as file_obj:
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
    packages=find_packages("requirements.txt"),
    install_requires=get_requirements(file_path="requirements.txt")
)