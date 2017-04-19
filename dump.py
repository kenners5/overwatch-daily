#!/usr/bin/env python
"""Dump player statistics to a data file."""

import os
import sys
import time

import json
import requests


def main():
    """ Dump player statistics to a data file."""
    user = sys.argv[1]
    battletag = user.replace("#", "-", 1)

    # owapi.net requires a custom user-agent header.
    # https://github.com/SunDwarf/OWAPI/blob/master/owapi/v3/v3_util.py#L16
    resp = requests.get("https://owapi.net/api/v3/u/{}/blob".format(battletag),
                        headers={'user-agent': 'unspecified'})
    if resp.status_code != 200:
        print resp.text
        sys.exit(1)

    data = resp.json()

    if not os.path.exists('data'):
        os.mkdir('data')

    datestr = time.strftime("%Y%m%d-%H%M%S")
    filename = os.path.join('data', '{}-{}.json'.format(datestr, battletag))

    with open(filename, 'w') as outfile:
        json.dump(data, outfile,
                  sort_keys=True,
                  indent=4,
                  separators=(',', ': '))

if __name__ == "__main__":
    # Input checking outside of main because w/e
    if len(sys.argv) <= 1:
        print "Please specify a battletag."
        print "{} USER#ID".format(sys.argv[0])
        sys.exit(1)

    main()
