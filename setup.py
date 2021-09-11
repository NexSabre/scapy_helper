from setuptools import find_packages, setup

with open("./README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="scapy_helper",
    description="Several features that should help you use Scapy",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Nex Sabre",
    author_email="nexsabre@protonmail.com",
    version="0.14.1",
    url="https://github.com/NexSabre/scapy_helper",
    packages=find_packages(),
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    license="MIT",
    install_requires=["tabulate~=0.8.7", "pyperclip==1.8.2"],
    entry_points={
        "console_scripts": [
            "hstrip = scapy_helper.utils.hstrip:hstrip",
            "hhstrip = scapy_helper.utils.hhstrip:hhstrip",
        ],
    },
)
