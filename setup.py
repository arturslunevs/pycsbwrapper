from setuptools import setup, find_packages

from pathlib import Path

this_dir = Path(__file__).parent

with open(this_dir / "README.md", encoding="utf-8") as f:
    long_description = f.read()


setup(
    name='pycspwrapper',
    version='0.1.1',
    description="Python wrapper for Latvian official statistics portal API: https://stat.gov.lv/en/api-and-code-list-registry.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/vf42/pycspwrapper',
    author='Vadim Fedorov',
    author_email='vadim@vf42.com',
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
