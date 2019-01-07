#!/usr/bin/env python

import os
import argparse
from .DaysOfCode import DaysOfCode

__version__ = "0.1.5"

default_location = os.path.join(os.path.expanduser('~'), 'Documents')


def main() -> None:
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--start', '-s',
                       help='Starts a new 100 Days of Code.',
                       action='store_true'
                       )
    group.add_argument('--restart', '-r',
                       help='Restarts 100 Days of Code. Warning, ALL progress is lost.',
                       action='store_true'
                       )
    group.add_argument('--newday', '-n',
                       help='Logs a new day.',
                       action='store_true'
                       )
    parser.add_argument('--path', '-p',
                        help='The path where git repository is to be stored.',
                        default=default_location
                        )
    args = parser.parse_args()
    doc = DaysOfCode(args.path)
    if args.start:
        doc.start()
    elif args.restart:
        doc.restart()
    elif args.newday:
        doc.new_day()
    else:
        parser.print_usage()
