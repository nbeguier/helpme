#!/usr/bin/env python3
"""
Help me

MIT License
Copyright (c) 2020 Nicolas Béguier
Written by Nicolas BEGUIER (nicolas_beguier@hotmail.com)
"""

# Standard library imports
from argparse import ArgumentParser
import os
import sys

# Debug
# from pdb import set_trace as st

VERSION = '%(prog)s 1.1.0'
HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

def add_tips_file(tips_file, verbose):
    """
    Add tips file in the configuration
    """
    tips_file_abs = os.path.abspath(tips_file)
    if not os.path.exists(tips_file_abs):
        return
    config_path = '{}/config.txt'.format(
        os.path.dirname(os.path.realpath(__file__)))
    if os.path.exists(config_path):
        with open(config_path, 'r') as config_file:
            for line in config_file.readlines():
                if tips_file_abs+'\n' == line:
                    return
    with open(config_path, 'a') as config_file:
        if verbose:
            print('>> Adding: {}'.format(tips_file_abs))
        config_file.write(tips_file_abs+'\n')

def add_tips_files(command, verbose):
    """
    Add tips files in the configuration
    """
    if len(command) == 1:
        print('You should specify at least one tips file...')
        return
    for tips_file in command[1:]:
        add_tips_file(tips_file, verbose)

def load_tips_files(verbose):
    """
    Returns the list of stored tips files
    """
    tips_files = list()
    config_path = '{}/config.txt'.format(
        os.path.dirname(os.path.realpath(__file__)))
    if not os.path.exists(config_path):
        print('You should specify at least one tips file...')
        return tips_files
    with open(config_path, 'r') as config_file:
        for line in config_file.readlines():
            tips_file = line.split('\n')[0]
            if verbose:
                print('>> Loading: {}'.format(tips_file))
            tips_files.append(tips_file)
    return tips_files

def match_tags(command, tags_raw):
    """
    Returns True is the command match at least one tag
    """
    is_present = False
    if len(tags_raw.split()) <= 1:
        return is_present
    tags = tags_raw.split('\n')[0].split()[1:]
    for tag in tags:
        is_present = is_present or \
            tag.lower().startswith(command.lower())
    return is_present

def get_title(title_raw):
    """
    Extracts title from raw string
    """
    return title_raw.replace('\xa0', ' ').split('\n')[0].split('## ')[1]

def get_content(params, tips_file):
    """
    Get command info from tips_file
    """
    content = dict()
    content['command'] = params['command']
    line_1 = current_title = ''
    reading = False
    with open(tips_file, 'r') as tips_file_:
        for line in tips_file_.readlines():
            if line.startswith('@tags:') and match_tags(params['command'], line):
                current_title = get_title(line_1)
                content[current_title] = list()
                reading = True
            elif line.replace('\xa0', ' ').startswith('## '):
                reading = False
            elif reading:
                content[current_title].append(line)
            line_1 = line

    return content

def color_code(line):
    """
    Print the line like bash color
    """
    if line.replace('\xa0', ' ').startswith('$ '):
        prefix = HEADER+'$ '
        line = line[2:]
        command = line.split()[0]
        args = ''
        if len(line.split()) > 1:
            args = ' '.join(line.split()[1:])
        print(prefix+OKGREEN+command+' '+OKBLUE+args+ENDC)
    else:
        print(line)

def display_content(content):
    """
    Pretty display the content
    """
    if len(content.keys()) <= 1:
        return
    iscode = False
    for key in content:
        if key == 'command':
            continue
        print(BOLD+UNDERLINE+'## '+key+ENDC)
        for value in content[key]:
            if value.startswith('##'):
                print(BOLD+UNDERLINE+value[:-1]+ENDC)
                iscode = False
            elif value.startswith('@description: '):
                print(WARNING+value[:-1].replace('@description: ', '')+ENDC)
            elif value.startswith('```'):
                iscode = not iscode
            elif iscode and value.startswith('#'):
                print(BOLD+value[:-1]+ENDC)
            elif iscode:
                color_code(value[:-1])
            else:
                print(BOLD+value[:-1]+ENDC)
    return

def main(params):
    """
    Main function
    """
    tips_files = load_tips_files(params['verbose'])
    for tips_file in tips_files:
        if not os.path.exists(tips_file):
            continue
        content = get_content(params, tips_file)
        display_content(content)

if __name__ == '__main__':
    PARSER = ArgumentParser()

    PARSER.add_argument('--version', action='version', version=VERSION)
    PARSER.add_argument('--verbose', action='store_true',\
        help="Increase verbosity (=False)", default=False)
    PARSER.add_argument('command', type=str, help='Display this command help', nargs='+')
    ARGS = PARSER.parse_args()

    PARAMS = dict()
    PARAMS['command'] = ARGS.command[0]
    PARAMS['verbose'] = ARGS.verbose

    if ARGS.command[0] == 'add':
        add_tips_files(ARGS.command, ARGS.verbose)
        sys.exit(0)
    elif ARGS.command[0] == 'help':
        print('HELP')
        sys.exit(0)

    main(PARAMS)
