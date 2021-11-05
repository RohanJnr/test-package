import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sample",
    version="0.0.1",
    description="",
    long_description=long_description(),
    long_description_content_type="text/markdown",
    author="RohanJnr",
    author_email="rohanjnr44@gmail.com",
    url="https://github.com/RohanJnr/test-package",
    packages=setuptools.find_namespace_packages(),
    install_requires=['loguru = "^0.5.3"'],
    python_requires=">=3.8.0,<3.11",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)