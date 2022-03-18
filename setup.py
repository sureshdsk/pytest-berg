import os

from setuptools import find_packages, setup

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
README = os.path.join(BASE_DIR, "README.md")

with open(README) as file:
    long_description = file.read()

setup(
    name="pytest-berg",
    version="1.0.0",
    description="Send desktop notification when tests are complete",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Suresh Kumar",
    author_email="sureshdsk@icloud.com",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Framework :: Pytest",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Testing",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],
    license="MIT",
    url="https://github.com/sureshdsk/pytest-berg",
    packages=find_packages("src"),
    package_dir={"": "src"},
    entry_points={"pytest11": ["berg = pytest_berg.plugin"]},
    install_requires=[
        "pytest",
        "chime==0.6.0",
        "win10toast==0.9; platform_system=='Windows'",
        "pync==2.0.3; platform_system=='Darwin'",
        "py-notifier==0.3.2",
    ],
)
