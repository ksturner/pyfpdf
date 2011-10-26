
PYFPDF Fork
===========


DESCRIPTION
-----------

This is a fork of the PyFpdf project hosted on Google code at:
http://code.google.com/p/pyfpdf/

The main motivation for the fork was to create a setup.py so that the project
could be pip installed. Additionally, because the project was going to be pip
installed as part of a virtual environment, the project was reduced down to the
bare minimum (no examples/tutorials).

The fork was created 26oct2011 and may or may not be up to date with the
original project thereafter.


DIFFERENCES FROM ORIGINAL PROJECT
---------------------------------

This project deviates from the original and does *not* include:

 * attic/ - files were reference material for original PHP src
 * examples/ - example files that were not critical to install
 * tutorial/ - tutorial files that were again, not needed

This project does add the following:

 * setup.py - useful for `pip install ...`, among other things.


MINIMAL EXAMPLE
---------------

```python
from pyfpdf import FPDF

pdf=FPDF()
pdf.add_page()
pdf.set_font('Arial','B',16)
pdf.cell(40,10,'Hello World!')
pdf.output('tuto1.pdf','F')
```


FORK AUTHOR
-----------

 * Kevin Turner
 * kevin@ksturner.com
 * @ksturner
