from setuptools import setup, find_packages

setup(
    name='ds_helper',
    version='1.0.0',
    author='Nirmala Rathod',
    description='A mini data science helper library with text cleaning, visualization, and column detection utilities.',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'matplotlib',
        'numpy',
    ],
)