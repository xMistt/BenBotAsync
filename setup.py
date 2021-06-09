import setuptools

name = 'BenBotAsync'

with open("README.md", "r") as fh:
    long_description = fh.read()

with open(f'{name}/__init__.py', encoding="utf8") as f:
    version = f.read().split("__version__ = '")[1].split("'")[0]

setuptools.setup(
    name=name,
    version=version,
    author="xMistt",
    description="Asynchronous Python wrapper for BenBot API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/xMistt/BenBot",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'aiohttp',
    ],
)
