from setuptools import setup, find_packages

setup(
    name='fpyo2ipa',
    version='1.2',
    author='SKbarbon',
    description='A package tool that allow you to built a python iOS apps with flet UI.',
    long_description="https://github.com/SKbarbon/fpyo2ipa",
    url='https://github.com/SKbarbon/fpyo2ipa',
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