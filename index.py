#!/usr/bin/python

import cgi
from src import Main

args = cgi.FieldStorage()
Main.run(args)