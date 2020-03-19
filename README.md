# Help me !

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
