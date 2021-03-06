#!/usr/bin/env python

import os
import argparse
from .DaysOfCode import DaysOfCode
from .DaysOfCode import DaysOfCodeException

__version__ = "0.2.0"

default_location = os.path.join(os.path.expanduser('~'), 'Documents')
default_day = 0


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
    group.add_argument('--display', '-d',
                       help='If a day number has been specified outputs the details, otherwise outputs all days.',
                       default=default_day
                       )
    group.add_argument('--edit', '-e',
                       help='Edit the specified day.',
                       )
    group.add_argument('--delete',
                       help='Delete challenge.',
                       action='store_true'
                       )
    parser.add_argument('--path', '-p',
                        help='The path where git repository is to be stored.',
                        default=default_location
                        )
    args = parser.parse_args()
    try:
        if args.start:
            doc = DaysOfCode(args.path)
            doc.start()
        elif args.restart:
            doc = DaysOfCode()
            doc.restart()
        elif args.newday:
            doc = DaysOfCode()
            doc.new_day()
        elif args.display:
            doc = DaysOfCode()
            doc.display_day(args.display)
        elif args.edit:
            doc = DaysOfCode()
            doc.edit_day(args.edit)
        elif args.delete:
            doc = DaysOfCode()
            doc.delete()
        else:
            parser.print_usage()
    except DaysOfCodeException as err:
        DaysOfCode.print_message(format(err))
