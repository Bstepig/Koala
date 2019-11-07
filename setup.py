from setuptools import setup, find_packages
from os.path import join, dirname


setup(
    name='koala',
    version='1.0',
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    package_dir={'koala': 'src'},
    entry_points={
        'console_scripts':
            ['koala = __main__']
        }, install_requires=['PyQt5']
)
