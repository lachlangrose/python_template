import os
import codecs
from setuptools import setup, find_packages

def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()

def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")
	
package_root = os.path.abspath(os.path.dirname(__file__))

version = {}
with open(os.path.join(package_root, "version.py")) as fp:
    exec(fp.read(), version)
version = version["__version__"]

setup(
	name="MyLibrary",
	version=get_version("MyLibrary/__init__.py"),

	)
# bump1
#
