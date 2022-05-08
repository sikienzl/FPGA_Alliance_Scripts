#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" This script cleans up the
    workspace after a
    full synthese (vasy,
    boom, boog, loon) run.
"""

__author__ = "Siegfried Kienzle"
__email__ = "siegfried.kienzle@gmx.de"

import os
import sys
import getopt

# Extension of VHDL Behavioral Subset
VBE = ".vbe"
# Extension of VHDL Structural Subset
VST = ".vst"
# Extension for graphical schematic viewer
XSC = ".xsc"


def usage():
    print("usage: cleanup.py [-h] [-f]")
    print("")
    print("optional arguments:")
    print("-h, --help show this help message and exit")
    print(
        "-f, --force removes without asking all files with extensions " +
        VBE +
        ", " +
        VST +
        ", " +
        XSC +
        ".")


def remove(filename):
    os.remove(filename)


def delete_question(filename):
    delete = input("Should the file " + filename + " removed? (y/n)")
    return delete


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hf", ["help", "force"])
    except getopt.GetoptError as err:
        print(err)
        usage()
        sys.exit(2)

    force = False

    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-f", "--force"):
            force = True

    path = os.path.abspath(os.getcwd())

    files = []

    for filename in os.listdir(path):
        if filename.endswith(VBE) or filename.endswith(
                VST) or filename.endswith(XSC):
            files.append(filename)

    for candidate in files:
        if force:
            print(candidate + " will be deleted")
            remove(candidate)
        else:
            if delete_question(candidate) == ("y"):
                print(candidate + " will be deleted")
                remove(candidate)


if __name__ == "__main__":
    main()
