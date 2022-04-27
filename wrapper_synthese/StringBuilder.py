#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""This class creates a
    StringBuilder.
    origin source can be found here:
    https://www.delftstack.com/de/howto/python/stringbuilder-in-python/
"""

from io import StringIO

class StringBuilder:
    _file_str = None

    def __init__(self):
        self._file_str = StringIO()

    def Append(self, str):
        self._file_str.write(str)

    def __str__(self):
        return self._file_str.getvalue()
