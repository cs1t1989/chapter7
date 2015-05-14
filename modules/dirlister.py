# -*- coding: utf-8 -*-
"""
Created on Thu May 14 11:41:10 2015

@author: root
"""

import os

def run(**args):
    print "[*] In dirlister module."
    files= os.listdir(".")
    
    return str(files)