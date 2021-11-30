# pbinfo_fetcher
Script written in Python that fetches problems from pbinfo.ro and puts the relevant sentences (requirements, explanations, input, output,...) as a comment in a C++ source file.
## Installation
This script requires the `lxml` module for it to work. You can install it using:
> `pip install lxml`

If you have `lxml` installed then you just need to download the **pbinfo.py** file from the repository (or just download the repository).
## Usage
To use this script you need to specify at least a *pbinfo.ro problem ID*.
> `./pbinfo.py 127 3945`

In this example, we have specified the script to download the problems with the IDs 127 and 3945. This will create 2 folders with the names `127` and `3945`, each folder containing a `main.cpp` file.
## Behaviour
The script will fetch the problems in the specified order and will exit when it fails to connect to pbinfo.ro or when it encounters an argument that is not valid to be a pbinfo.ro ID (positive integer number).  
However, if it encounters a valid problem that it can't access/doesn't exist (eg. 3, 4000), the script will output:  
`"The problem (insert problem ID here) does not exist!"`.
