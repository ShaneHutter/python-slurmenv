#!/usr/bin/env python3
"""This is a tool to convert a line seperated list of env variables
into lines of python for the enum
"""
if __name__ == '__main__':
    with open( "env_list" , "r" ) as filename:
        file_lines = filename.read().split( "\n" )
    ret = []
    code_string = "\t{} = environ.get( \"{}\" )"
    for line in file_lines:
        ret.append( code_string.format( line.lower() , line.upper() ) )
    print( "\n".join( ret ) )
