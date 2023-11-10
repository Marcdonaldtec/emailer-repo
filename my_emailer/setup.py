from setuptools import setup, find_packages

setup(
    name='my-emailer',
    version='0.1.0',
    packages=find_packages(),
    install_python_requires = '>=3.10',
    entry_points={
        'console_scripts': [
            'my-emailer=my_emailer.emailer:main',
        ],
    },
    author='Marc Donald Omeus and Denes Jean Baptiste',
    description='A simple emailer library',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Marcdonaldtec/emailer-repo'
    
)
