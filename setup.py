import setuptools

with open("readme.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='hue',
    version='1.9.6',
    scripts=['hue'],
    author="Gage LeBlanc",
    author_email="gleblanc@symnet.io",
    description="A simple cli app for controlling hue lights",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gageleblanc/hue",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
)