from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='tryoutmanager',
    version='0.0.1',
    description='Tryout Manager',
    long_description=readme,
    author='Rodger Waldron',
    author_email='rwald@uocsclub.ca',
    url='https://github.com/uocsclub/tryoutmanager',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
