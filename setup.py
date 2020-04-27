import os

from setuptools import setup, Extension
from Cython.Build import cythonize

# Get the current directory
here = os.path.abspath(os.path.dirname(__file__))
# Get the long description from the README
with open(os.path.join(here, "README.md"), 'r') as f:
    long_description = f.read()
# Load __version__ cleanly
with open(os.path.join(here, 'contains/version.py'), 'r') as f:
    exec(f.read())

setup(
    name="contains",
    version=__version__,
    ext_modules=cythonize("contains/triangle_hash.pyx"),
    description="Compiled point-in-mesh queries",
    long_description=long_description,
    url="https://github.com/mikedh/contains",
    author="Lars Mescheder",
    author_email="LarsMescheder@gmx.net",
    maintainer="Michael Dawson-Haggerty",
    maintainer_email="mikedh@kerfed.com",
    packages=["contains"],
    keywords="geometry",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers"],
    install_requires=["numpy"]
)
