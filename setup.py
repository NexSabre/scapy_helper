from setuptools import setup, find_packages

setup(
    name="scapy_helper",
    description="Several features that should help you use Scapy",
    author="Nex Sabre",
    author_email="nexsabre@protonmail.com",
    version="0.1.7",
    url="https://github.com/NexSabre/scapy_helper",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["scapy==2.4.4", "tabulate==0.8.7"]
)
