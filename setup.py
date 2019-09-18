import os
import runpy

from setuptools import setup, Extension

# Get the current directory
here = os.path.abspath(os.path.dirname(__file__))
# Get the long description from the README
with open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()
# Load __version__ cleanly
version_globals = runpy.run_path("contains/version.py")

setup(
    name="contains",
    version=version_globals["__version__"],
    ext_modules=[
        Extension("triangle_hash", ["contains/triangle_hash.pyx"], language="c++")
    ],
    description="Compiled point-in-mesh queries",
    long_description=long_description,
    url="https://github.com/mikedh/contains",
    author="",
    author_email="",
    keywords="geometry",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
    ],
)
