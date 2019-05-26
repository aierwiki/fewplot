# @Author: Tang Yubin <tangyubin>
# @Date:   2019-05-26T11:59:03+08:00
# @Email:  tang-yu-bin@qq.com
# @Last modified by:   tangyubin
# @Last modified time: 2019-05-26T12:48:50+08:00
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fewplot",
    version="0.0.2",
    author="Tang Yubin",
    author_email="tang-yu-bin@qq.com",
    description="a plot tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aierwiki/fewplot",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
