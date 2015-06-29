#!/usr/bin/python

import sys

def reset_colour():
    return "\x1b[0m"
    
def set_colour(colour_number):
    return "\x1b[48;5;%im"%colour_number

colours=[1, 208, 220, 76, 27, 19, 171]
    
for (colour, line) in zip(colours, sys.stdin):
    print(set_colour(colour)+line.strip()+reset_colour())
