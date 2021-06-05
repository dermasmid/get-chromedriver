from setuptools import setup
import re


with open('README.md', encoding='utf-8') as f:
    readme = f.read()

with open('get_chromedriver.py', encoding= 'utf-8') as f:
    version = re.findall("__version__ = '(.+)'", f.read())[0]

with open("requirements.txt", encoding="utf-8") as f:
    requirements = [r.strip() for r in f]



setup(
    name = 'get_chromedriver',
    version = version,
    py_modules=['get_chromedriver'],
    license = 'MIT',
    url = 'https://github.com/dermasmid/get-chromedriver',
    long_description = readme,
    long_description_content_type = 'text/markdown',
    author = 'Cheskel Twersky',
    author_email= 'twerskycheskel@gmail.com',
    description = 'Get the latest chromedriver for the chrome installed on your system',
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
    install_requires = requirements,
    python_requires='>=3.6'
    )
