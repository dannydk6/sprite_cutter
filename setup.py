import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sprite_cutter",
    version="0.0.1a",
    author="Daniel Alarcon",
    author_email="dfa238@nyu.edu",
    description="extract individual sprites from a png sprite sheet",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dannydk6/sprite_cutter",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
