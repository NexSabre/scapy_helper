from setuptools import setup, find_packages

setup(
    name="scapy_helper",
    description="Several features that should help you use Scapy",
    author="Nex Sabre",
    author_email="nexsabre@protonmail.com",
    version="0.2.2",
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
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    license='MIT',
    install_requires=["tabulate~=0.8.7"]
)
