
PYFPDF Fork
===========


DESCRIPTION
-----------

This is a fork of the PyFPdf project hosted on Google code at:
http://code.google.com/p/pyfpdf/

The main motivation for the fork was to create a setup.py so that the project
could be pip installed. The fork was created 26oct2011 and may or may not be up
to date with the original project thereafter.

DIFFERENCES FROM ORIGINAL PROJECT
---------------------------------

This project deviates from the original and does *not* include:

 * attic/ - files were reference material for original PHP src
 * examples/ - example files that were not critical to install
 * invoice.csv - tutorial file? that was not necessary
 * tutorial/ - tutorial files that were again, not needed

This project does add the following:

 * setup.py - useful for `pip install ...`, among other things.


FORK AUTHOR
-----------

 * Kevin Turner
 * kevin@ksturner.com
 * @ksturner
