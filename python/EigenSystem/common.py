#!/usr/bin/python
# -*- coding: utf-8 -*-
import datetime
import numpy as np

def timestamp(header,string):
  ct = datetime.datetime.now()
  msg = "# [" + str(ct) + "] " + string + "\n"
  flog = open(header+'_python.log', 'a')
  flog.write(msg)
  flog.close()
