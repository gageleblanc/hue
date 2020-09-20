import setuptools

with open("readme.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='huecli',
    version='1.9.8',
    scripts=['hue'],
    author="Gage LeBlanc",
    author_email="gleblanc@symnet.io",
    description="A simple cli app for controlling hue lights",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gageleblanc/hue",
    packages=setuptools.find_packages(),
    install_requires=[
        'clilib>=1.6.1',
        'phue'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
)