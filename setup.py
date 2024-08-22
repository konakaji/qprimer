import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="qprimer",
    version="0.0.2",
    author="kohei nakaji",
    description="You can receive the message 'Hello!!!'",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/konakaji/qprimer",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
    ],
    python_requires='>=3.6',
)
