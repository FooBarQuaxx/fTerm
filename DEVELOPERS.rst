********************
Developing for fTerm
********************

========
Packages
========

About
-----
fTerm allows for the installation of files in the *main* folder.

Requirements
------------
Each file installed contains functions. fTerm automatically reads the number of arguments and docstrings of each function in each file installed. The name each fTerm command will be (lowercase) the name of the function defined in the file.

(dict) synonyms
^^^^^^^^^^^^^^^
Synonyms is a dictionary containing alternate names for functions. The key/value pairs contain the alternate names mapping to the original names. For example, if you wanted to add "write" and "scribble" synonyms to the function "edit":

.. code:: python

   synonyms = {"scribble":"edit",
               "write":"edit",
               .
               .
               .
              }

**NOTE THAT** all functions in a package must have an entry as a value in *synonyms*. If you do not wish to add any synonyms for function *func*, you can simply add the entry `"func":"func"` to *synonyms*.

functions
^^^^^^^^^
Functions in fTerm are defined as functions that take arguments (fTerm will automatically parse the number of arguments), and that return strings of BASH commands, seperated by semicolons (and ending with one) For example,

.. code:: python

   def swap(file1, file2):
       """A function that swaps the names of two files."""

       call = ""

       # make a temporary file
       temp = subprocess.Popen(["mktemp"], stdout=subprocess.PIPE).communicate()[0].replace("\n", "")

       # move 1 to temp
       call += "mv %s %s;" % (file1, temp)

       # move 2 to 1
       call += "mv %s %s;" % (file2, file1)

       # move temp to 1
       call += "mv %s %s;" % (temp, file2)

       return call


=====
Style
=====
The fTerm project uses the PEP8 standard, through the [Pylint](https://www.pylint.org/) linter. However, in cases where PEP requests are extraneous or otherwise unreasonable, you may ignore them by adding, at the beginning of the file, after the docstring

.. code: python

   # NOTE: {{why you ignore this error}}
   # pylint: disable-msg={{id of error}}


## Module docstrings
Docstrings, which must be at the beginning of all program files, should be of the following format:

.. code:: python

   [{{name of package}}] {{name of file}}

   {{explanation of what the file does}}


*e.g.*, for the fTerm core file *parser.py*,

.. code:: python

   """
   [fTerm] parser.py

   This module parses commands, interpreting them first with a synonym check (for
   any words that are synonymous with the word in question that are fTerm commands),
   and secondly with a difflib.get_close_matches check (in case of typos).
