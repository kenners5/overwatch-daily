#!/usr/bin/env python
"""Render summary statistics comparing two dump files."""


import os
import sys

import json

def main():
    before_filename = os.path.expanduser(sys.argv[1])
    after_filename = os.path.expanduser(sys.argv[2])
    with open(before_filename) as handle:
        before = json.load(handle)
    with open(after_filename) as handle:
        after = json.load(handle)

    print before['us']['stats']['quickplay'].keys()
    print after['us']['stats']['quickplay'].keys()

if __name__ == "__main__":
    # Input checking outside of main because w/e
    if len(sys.argv) <= 2:
        print "Please specify before/after data files."
        print "{} (filename1) (filename2)".format(sys.argv[0])
        sys.exit(1)

    main()
