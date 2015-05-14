# -*- coding: utf-8 -*-
"""
Created on Thu May 14 11:45:58 2015

@author: root
"""

import os

def run(**args):
    print "[*] In environment module."
    return str(os.environ)
    