#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""This script is a wrapper for the alliance-tool-suite from
   http://www-soc.lip6.fr.

   This script requires that the alliance toolchain is already
   installed and the corresponding environment variables are set.
"""

import argparse
import sys
import StringBuilder

def input_file_empty():
    print("No input file defined!")

def get_vasy_command(parser_args):
    str_vasy_command = StringBuilder.StringBuilder()
    if parser_args.command == 'vasy':
        str_vasy_command.Append("vasy ")
        if (parser_args.i is None):
            input_file_empty()
            sys.exit(1)  
        if (parser_args.a is not None):
            str_vasy_command.Append("-a ")
        if (parser_args.p is not None):
            str_vasy_command.Append("-p ")
        if (parser_args.i is not None):
            str_vasy_command.Append(parser_args.i + " ")
        if (parser_args.o is not None):
            str_vasy_command.Append(parser_args.o)
        if (parser_args.o is None):
            str_vasy_command.Append(parser_args.i + "_vasy")
    return str_vasy_command

def get_boom_command(parser_args):
    str_boom_command = StringBuilder.StringBuilder()
    if parser_args.command == 'boom':
        str_boom_command.Append("boom ")
        if (parser_args.i is None):
            input_file_empty()
            sys.exit(1)
        if (parser_args.l is not None):
            str_boom_command.Append("-l " + str(parser_args.l) + " ")
        if (parser_args.d is not None):
            str_boom_command.Append("-d " + str(parser_args.d) + " ") 
        if (parser_args.i is not None):
            str_boom_command.Append(parser_args.i + " ")
    
    output = ""
    if (parser_args.o is not None):
        output = parser_args.o
    elif "_vasy" in parser_args.i:
        output = parser_args.i.replace("_vasy", "_boom")
    else:
        output = parser_args.i + "_boom"
    str_boom_command.Append(output)
    return str_boom_command

def get_boog_command(parser_args):
    str_boog_command = StringBuilder.StringBuilder()
    if parser_args.command == 'boog':
        str_boog_command.Append("boog ")
        if (parser_args.i is None):
            input_file_empty()
            sys.exit(1)
        if (parser_args.m is not None):
            str_boog_command.Append("-m " + str(parser_args.m) + " ")
        if (parser_args.i is not None):
            str_boog_command.Append(parser_args.i + " ")

    output = ""
    if (parser_args.o is not None):
        output = parser_args.o
    elif "_boom" in parser_args.i:
        output = parser_args.i.replace("_boom", "_boog")
    else:
        output = parser_args.i + "_boog"
    str_boog_command.Append(output)
    return str_boog_command

def get_loon_command(parser_args):
    str_loon_command = StringBuilder.StringBuilder()
    if parser_args.command == 'loon':
        str_loon_command.Append("loon ")
        if (parser_args.i is None):
            input_file_empty()
            sys.exit(1)
        if (parser_args.m is not None):
            str_loon_command.Append("-m " + str(parser_args.m) + " ")
        if (parser_args.x is not None):
            str_loon_command.Append("-x " + str(parser_args.x) + " ")
        if (parser_args.i is not None):
            str_loon_command.Append(parser_args.i + " ")

    output = ""
    if (parser_args.o is not None):
        output = parser_args.o
    elif "_boog" in parser_args.i:
        output = parser_args.i.replace("_boog", "_final")
    else:
        output = parser_args.i + "_final"
    str_loon_command.Append(output)
    return str_loon_command

def main():
    parser = argparse.ArgumentParser()

    sub_parsers = parser.add_subparsers(dest='command', help='sub-command help')

    parser_vasy = sub_parsers.add_parser('vasy', help='vasy analyze for the synthesis')
    parser_vasy.add_argument('-i', type=str, help='input-file in .vhdl-format')
    parser_vasy.add_argument('-a', type=str, help='output in alliance-format (.vbe)')
    parser_vasy.add_argument('-p', action='store_const', const=True, help='ports for power')
    parser_vasy.add_argument('-o', action='store_const', const=True, help='overrides output-file')
    parser_vasy.add_argument('-C', type=str, help='blocksize; produce carry-lookahead-adder')

    parser_boom = sub_parsers.add_parser('boom', help='boom optimize time and/or area')
    parser_boom.add_argument('-i', type=str, help='input-file in .vbe-format')
    parser_boom.add_argument('-l', type=int, nargs='?', const=0, help='optimizationexpense (0..3, default:0)')
    parser_boom.add_argument('-d', type=int, help='optimizationsgoal (0..100, 0=Area, 100=Speed)')
    parser_boom.add_argument('-o', type=str, help='output-file in vbe-format')

    parser_boog = sub_parsers.add_parser('boog', help='boog binding and optimization on gates')
    parser_boog.add_argument('-i', type=str, help='input-file in .vbe-format')
    parser_boog.add_argument('-m', type=int, help='optimizationgoal (0..4; 0=Area, 100=Speed)')
    parser_boog.add_argument('-o', type=str, help='output-file in vst-format')

    parser_loon = sub_parsers.add_parser('loon', help='loon logic optimization of nets')
    parser_loon.add_argument('-i', type=str, help='input-file in vst-format')
    parser_loon.add_argument('-m', type=int, help='optimizationgoal (0..4; 0=Area, 4=Speed)')
    parser_loon.add_argument('-x', type=int, help='[0|1] kind of .xsc-file 0=critical path; 1=signal')
    parser_loon.add_argument('-o', type=str, help='output-file in vst-format')



    args = parser.parse_args()
    #str_command = get_vasy_command(args)
    #str_command = get_boom_command(args) 
    #str_command = get_boog_command(args)
    str_command = get_loon_command(args)
    print(str_command)










if __name__ == "__main__":
    main()
