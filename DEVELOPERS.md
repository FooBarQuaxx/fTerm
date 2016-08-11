![fTerm](logo.png)
[![homebrew](https://img.shields.io/badge/homebrew-0.0.2a3-yellow.svg?style=flat-square)]()
[![License (GPL version 3)](https://img.shields.io/badge/license-GNU%20GPL%20version%203-blue.svg?style=flat-square)](http://opensource.org/licenses/GPL-3.0)
[![Awesome: true](https://img.shields.io/badge/awesome%20-yes-brightgreen.svg?style=flat-square)]()

# Packages

## About
fTerm allows for the installation of files in the *main* folder.

## Requirements

Each file installed contains functions. fTerm automatically reads the number of arguments and docstrings of each function in each file installed. The name each fTerm command will be (lowercase) the name of the function defined in the file.

### (dict) synonyms
Synonyms is a dictionary containing alternate names for functions. The key/value pairs contain the alternate names mapping to the original names. For example, if you wanted to add "write" and "scribble" synonyms to the function "edit":

```
synonyms = {"scribble":"edit",
            "write":"edit",
            .
            .
            .
           }
```

**NOTE THAT** all functions in a package must have an entry as a value in *synonyms*. If you do not wish to add any synonyms for function *func*, you can simply add the entry `"func":"func"` to *synonyms*.

# Style
The fTerm project uses the PEP8 standard, through the [Pylint](https://www.pylint.org/) linter. However, in cases where PEP requests are extraneous or otherwise unreasonable, you may ignore them by adding, at the beginning of the file, after the docstring

```
# NOTE: {{why you ignore this error}}
# pylint: disable-msg={{id of error}}
```
