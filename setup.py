from setuptools import setup, find_packages

with open("requirements.txt", "r") as fp:
    req = [el.strip() for el in fp.readlines() if not el.startswith("#")]

setup(
    name='riffusion',
    version='1.0.1',
    url='https://github.com/heardsounds/riffusion.git',
    packages=find_packages(),    
    install_requires=req,
)
