#fTerm

![fTerm demo #2](demo.png)

[![homebrew](https://img.shields.io/badge/homebrew-1.0.1-yellow.svg?style=flat-square)]()
[![License (GPL version 3)](https://img.shields.io/badge/license-GNU%20GPL%20version%203-blue.svg?style=flat-square)](http://opensource.org/licenses/GPL-3.0)
[![Awesome: true](https://img.shields.io/badge/awesome%20-yes-brightgreen.svg?style=flat-square)]()

# About

fTerm is a terminal with english syntax and natural language processing.

# How-To

To run *command* with arguments *a1, a2,...*, simply run

```
f command a1, a2,...
```

The fTerm interpreter will then attempt to interpret *command*.
First it will check if it was defined as a synonym of another, defined, command, and then do a string-based (typo-preventing) search. It will then prompt you with:

```
[f-i] interpreted_command a1, a2...
```

If you enter anything (except just pressing the return key), the command will not be run.

## Examples

```
$ f list
[f-i] list⏎
a.txt
b.rst
c.mp4
$ f remove b.rst
[f-i] delete a⏎
$ f list
[f-i] list⏎
a.txt
c.mp4
```

```
$ f read a
[f-i] read a⏎
this is a test!
$ f read b
[f-i] read b⏎
this is also a test!
$ f swap a b
[f-i] swap a b⏎
[f] Swapped a and b
$ cat a
this is also a test!
$ cat b
this is a test!
```

# Commands

## list(*dirs)
List the files in a directory.

## addline(filename, line)
Append *line* to *filename*.

## delete(*files)
Delete a file or directory.

## edit(*files)
Edit a file.

## kill(*processes)
Kill the process with name *processname*.

## move(filename, pos)
Move the file or folder at *path1* to *path2*.

## read(*files)
Read a file.

## run(*files)
A universal run function.

## size(*files)
Return the size of a file in human-readable format.

## sort(directory, exp)
Takes a directory *directory* and a regular expression *exp*. Sorts each file into a
folder with name equal to the match of *exp* in its filename.

## swap(file1, file2)
A function that swaps the names of two files.

## compress(filename)
Compress a file.

## decompress(filename)
Decompress a file.

## decrypt(filename)
Decrypt a file.

## encrypt(filename)
Encrypt a file.

# Installing (Mac)

First, run

```
brew tap lschumm/tap
```
and then

```
brew install fterm
```

fTerm is now installed! Verify your installation by running:
```
$ f
[f-i] Please specify a command (e.g., f swap file1 file2)
```

# Extending
See (DEVELOPERS.md)[DEVELOPERS.md] for details.

# Contributing
The fTerm project uses [gitmagic.io](https://gitmagic.io/) for pull requests. See the [contributing.json](contributing.json) file for more information.


# Notes
- Install either the *zsh* or *fish* shell. Autocomplete is **awesome**.

# Authors

* **Liam Schumm** - *Lead Developer* - [@lschumm](https://github.com/lschumm)
* **Andy Merrill** - *Idea + Developer* - [@appleinventor](https://github.com/appleinventor)
* **Jack Merrill** - *Web Developer* - [@yoshifan509](https://github.com/yoshifan509)


#  License

This project is licensed under the GNU GPL License, version 3.0 - see the [LICENSE.md](LICENSE.md) file for details
