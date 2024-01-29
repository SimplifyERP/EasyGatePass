from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in easygatepass/__init__.py
from easygatepass import __version__ as version

setup(
	name="easygatepass",
	version=version,
	description="Security system",
	author="VPS Business Solution",
	author_email="vivekchamp84@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
