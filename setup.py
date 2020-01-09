import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="luri",
    version="0.0.1",
    author="iuri segtovich",
    author_email="iurisegtovich@gmail.com",
    description="lib iuri",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/iurisegtovich/luri",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
