"""Prints a list of models to a file."""


import glob
import os
import sys


if __name__ == '__main__':
    cwd = os.getcwd()
    os.chdir(sys.argv[1])
    files = glob.glob('**/*.mdl', recursive=True)
    os.chdir(cwd)
    with open(sys.argv[2], 'w') as fp:
        fp.write('\n'.join(files))
