
from setuptools import setup, find_packages

setup(
    name="cropguardian",
    version="1.0.0",
    description="A library for agricultural management and analytics.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="your_email@example.com",
    url="https://github.com/yourusername/cropguardian",
    packages=find_packages(),
    install_requires=["matplotlib>=3.0"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License v2 (LGPLv2)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
