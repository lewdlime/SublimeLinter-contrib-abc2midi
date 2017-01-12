# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by lsavide
# Copyright (c) 2017 lsavide
#
# License: MIT

"""This module exports the Abc2midi plugin class."""

from SublimeLinter.lint import Linter, util

class Abc2midi(Linter):
    """Provides an interface to abc2midi."""

    syntax = 'abc'
    cmd = 'abc2midi -v'
    executable = None
    version_args = '-ver'
    version_re = r'abc2midi (?P<version>\d+\.\d+(?:\.\d+)?) .*'
    version_requirement = '>= 2.0'
    regex = r'(?:^(?P<error>Error)|(?P<warning>Warning)) in line(?:-char)? (?P<line>\d+)-(?P<col>\d+)? : (?P<message>.+)'
    multiline = False
    line_col_base = (1, 1)
    tempfile_suffix = '-'
    error_stream = util.STREAM_BOTH
    selectors = {
      'abc': 'meta.tune.abc'
    }
    word_re = r'([-\w]+)'
    defaults = {
      '-t:': '',
      '-n:': '',
      '-CS:': '',
      '-quiet:': '',
      '-silent:': '',
      '-Q: +': '',
      '-NFNP:': '',
      '-NCOM:': '',
      '-NFER:': '',
      '-NGRA:': '',
      '-STFW:': '',
      '-HARP:': '',
      '-BF:': '',
      '-OCC:': '',
      '-TT:': '',
      '-CSM:': ""
    }
    inline_settings = None
    inline_overrides = None
    comment_re = r'(?:^r:.*)|(?:\s*%.*)'
