""" lec_fileio.py

Companion codes for the lecture on reading and writing files
"""

import os
import toolkit_config as cfg

SRCFILE = os.path.join(cfg.DATADIR, 'qan_prc_2020.csv')
DSTFILE = os.path.join(cfg.DATADIR, 'new_file.txt')

# ----------------------------------------------------------------------------
#   Opening the `SRCFILE` and reading its contents
# ----------------------------------------------------------------------------
# This will open the file located at `SRCFILE` and return a handler (file
# object):
fobj = open(SRCFILE, mode='r')
# We can get the entire content of the file by calling the method `.read()`,
# without parameters:
cnts = fobj.read()

# The variable `cnts` will be a string containing the full contents of the
# file. This will print the first 20 characters:
print(cnts[:20])

# Output:
#  Date,Open,High,Low,C

# Close the file
fobj.close()
print(fobj.closed)  # --> True

# ----------------------------------------------------------------------------
#   Writing content to a file
# ----------------------------------------------------------------------------
# Auxiliary function to print the lines of a file
def print_lines(pth):
    """ Function to print the lines of a file
    Parameters
    ----------
    pth : str
        Location of the file
    Notes
    -----
    Each line in the file will be printed as
        line number: 'string with the line text'
    """
    with open(pth) as fobj:
        for i, line in enumerate(fobj):
            print(f"line {i}: {line.rstrip()}")


#  This will create the file located at `DSTFILE` and write some content to it
with open(DSTFILE, mode='w') as fobj:
    fobj.write('This is a line\n')
    fobj.write('This is a another line')

# Exiting the context manager will close the file
# We can then print its contents
print_lines(DSTFILE)