from setuptools import setup, find_packages
with open("README.md", encoding="utf-8") as f:
    long_desc = f.read()

setup(
    name="topsis-vansh-102303922",
    version="0.1.1",
    author="Vansh",
    description="Command line implementation of TOPSIS",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=["pandas", "numpy"],
    entry_points={
        "console_scripts": [
            "topsis=topsis.topsis:main"
        ]
    },
)
