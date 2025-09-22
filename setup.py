from setuptools import setup, find_packages

from pathlib import Path

this_dir = Path(__file__).parent

with open(this_dir / "README.md", encoding="utf-8") as f:
    long_description = f.read()


setup(
    name='pycsbwrapper',
    version='0.0.1',
    description="Python wrapper for Central Bureau of Statistics Republic of Latvia pxweb API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/arturslunevs/pycsbwrapper',
    author='Arturs Lunevs',
    author_email='arturs.lunevs@gmail.com',
    license='MIT',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    packages=find_packages(),
    install_requires=[
        'requests>=2.21.0',
    ]
)
