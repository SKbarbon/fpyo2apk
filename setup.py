from setuptools import setup, find_packages

setup(
    name='fpyo2apk',
    version='1.1.1',
    author='SKbarbon',
    description='A package tool that allow you to built a python Android apps with flet-pyodide dist.',
    long_description="https://github.com/SKbarbon/fpyo2apk",
    url='https://github.com/SKbarbon/fpyo2apk',
    install_requires=["briefcase==0.3.14"],
    include_package_data=True,
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
    ],
    include_dirs=["assets"],
    package_data={"assets": ["pyo2ipadist.zip"]},
)