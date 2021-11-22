"""Package configuration."""
from setuptools import find_packages, setup

setup(
    name="1_1_de_assignment_parlindrome_int",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)