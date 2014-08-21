#!/usr/bin/python

import cProfile
import cgi
from src import Main

args = cgi.FieldStorage()
cProfile.run('Main.run(args)', sort='cumulative', filename='diagnostics/profiler.txt')