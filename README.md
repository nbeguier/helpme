# Help me !

[![Build Status](https://travis-ci.org/nbeguier/helpme.svg?branch=master)](https://travis-ci.org/nbeguier/helpme) [![Python 3.4|3.8](https://img.shields.io/badge/python-3.4|3.8-green.svg)](https://www.python.org/) [![License](https://img.shields.io/github/license/nbeguier/helpme?color=blue)](https://github.com/nbeguier/helpme/blob/master/LICENSE)

Shortcut to display help about custom notes written in markdown

## Prerequisites

Create a markdown file.

  - Only `##` title are considered as title

  - Add `@tags` below a title to add tags

  - Add `@description` below a title to add colorful description

See tips_example.md for more information.

## Usage

```
$ ./helpme.py --help
usage: helpme.py [-h] [--version] [--verbose] command [command ...]

positional arguments:
  command     Display this command help

optional arguments:
  -h, --help  show this help message and exit
  --version   show program's version number and exit
  --verbose   Increase verbosity (=False)
```

## Add new tips

```
$ ./helpme.py --verbose add tips_example.md
>> Adding: /absolutepath/helpme/tips_example.md
```

## Example

```
$ ./helpme.py tool
## Tool A

This is text
$ this is code
and output

## Another tool called MIAMI

### Install
git clone miami
Then, remove the directory

rm miami.log
```

```
$ ./helpme.py miami
## Another tool called MIAMI

### Install
git clone miami
Then, remove the directory

rm miami.log
```

# License
Licensed under the [MIT License](https://github.com/nbeguier/helpme/blob/master/LICENSE).

# Copyright
Copyright 2020-2021 Nicolas Béguier; ([nbeguier](https://beguier.eu/nicolas/) - nicolas_beguier[at]hotmail[dot]com)
