import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="data_analysis",
    version="0.0.1",
    author="Adam Arce",
    author_email="adam.arce@slu.edu",
    description="This is a sample of a data processing library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/seismicshaker/2018_agu_workshop.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
