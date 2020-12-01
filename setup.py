from setuptools import setup, find_packages

setup(
    name="scapy_helper",
    description="Several features that should help you use Scapy",
    author="Nex Sabre",
    author_email="nexsabre@protonmail.com",
    version="0.2.0",
    url="https://github.com/NexSabre/scapy_helper",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        'License :: OSI Approved :: Apache Software License',
        "Operating System :: OS Independent",
    ],
    license='Apache License, Version 2.0',
    install_requires=["tabulate~=0.8.7"]
)
