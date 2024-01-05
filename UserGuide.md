# RepeatAnalyzer Quickstart Guide

## Overview

The purpose of this guide is to allow you to set up and begin using the RepeatAnalyzer software package on a new computer, with either Windows, Mac OS X or Linux operating systems. This process involves installing free software from a third party source and thus requires an internet connection. A brief description of how to use the software follows, however this is not meant to be a complete source on use cases. For questions related to problems with installation or usage of this software, contact the dev team at <https://github.com/prosaicpudding/RepeatAnalyzer/discussions>

## Download

Source code is available at: <https://github.com/prosaicpudding/RepeatAnalyzer>. You can download the sourcecoe as a zip file by clicking the green "code" button and selecting "Download Zip". Alternatively, if you are familiar with git, you can clone the repository using:

`git clone git@github.com:prosaicpudding/RepeatAnalyzer.git`

For windows users, an executable file is available [here](https://github.com/prosaicpudding/RepeatAnalyzer/releases) If you are using the executable, you can skip the installation steps below. Note that we currently don't have a budget to sign the executable file, so you will need to ignore the windows defender security warning.

## Installation
Assuming for one reason or another you are downloading the program and running it from source code, ensure you have an internet connection before you begin.

1. Go to <https://www.python.org/downloads/>. Follow installation instructions there. Be sure to install a version that is at least 3.10.x
2. Next, we will install dependencies.
   - If you are on Mac OS, or Linux, you will likely need to install the latest versions of geos and proj using either brew (Mac OS) or apt (Linux).
   - For all operating systems, you will need to install poetry. `python -m pip install poetry`
