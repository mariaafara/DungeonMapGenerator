"""Python module to install maze_generator package."""
import os

from setuptools import find_packages, setup


def read(fname):
    """Read a file and return it as string."""
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


imports = ["tqdm", "matplotlib", "numpy"]

setup(
    name="maze_generator",
    version="0.0.1",
    author="Maria Afara",
    author_email="maria-afara5@hotmail.com",
    description="Package to generate a maze with 3 randomly initialized points.",
    packages=find_packages(),
    long_description=read("README.md"),
    install_requires=imports,
    scripts=[],
)
