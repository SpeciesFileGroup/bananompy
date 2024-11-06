import codecs
from setuptools import setup
from setuptools import find_packages

with codecs.open("README.md", "r", "utf-8") as f:
    readme = f.read().replace("\r", '')

with codecs.open("CHANGELOG.md", "r", "utf-8") as f:
    changes = f.read().replace("\r", '')
changes = changes.replace(":issue:", "")
long_description = readme + "\n\n" + changes

setup(
    name="bananompy",
    version="0.0.1",
    description="Python client for Bionomia",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Geoff Ower",
    author_email="gdower@illinois.edu",
    url="http://github.com/speciesfilegroup/bananompy",
    download_url="https://github.com/speciesfilegroup/bananompy/archive/refs/tags/v0.0.1.tar.gz",
    license="MIT",
    packages=find_packages(exclude=["test-*"]),
    install_requires=[
        "requests>2.7",
        "beautifulsoup4>4.9.0",
        "lxml>4.4.3"
    ],
    extras_require={
        "dev": [
            "codecov", 
            "pytest", 
            "pytest-cov",
            "python-dateutil",
            "sphinx>7.2.0", 
            "sphinx_issues", 
            "sphinx-rtd-theme", 
            "twine",
            "vcrpy",
            "wheel"],
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12"
    ],
    keywords = ['bionomia', 'biodiversity', 'collectors', 'specimens', 'API', 'web-services', 'species', 'natural history', 'taxonomists', 'biologists'],
)
