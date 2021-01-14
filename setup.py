import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="drf-cli",
    version="0.0.1",
    author="Shayan Karimi",
    author_email="shayankarimi0078@gmail.com",
    description="Django Rest Framework command-line tools",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shywn-mrk/drf-cli",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points= {
        'console_scripts': [
            'drf-cli = drf_cli.__main__:main'
        ]
    }
)
