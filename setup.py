"""Installation script for the 'test_fld' python package."""

from setuptools import setup, find_packages

# Minimum dependencies required prior to installation
INSTALL_REQUIRES = [
    "isaacgym",
    "matplotlib",
    "onnx",
    "numpy>=1.16.4,<=1.22.4",
    "setuptools==59.5.0",
    "gym>=0.17.1",
    "GitPython",
]

# Installation operation
setup(
    name="test_fld",
    version="1.0.0",
    author="Yuxuan Xie",
    packages=find_packages(),
    author_email="yuxuangmxie@gmail.com",
    install_requires=INSTALL_REQUIRES,
)