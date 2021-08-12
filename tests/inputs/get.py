#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@gmail.com>
Date   : 2021-03-08
Purpose: Rock the Casbah
"""

import requests
import string
import re
from functools import partial
from bs4 import BeautifulSoup


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    out = open('drugs.txt', 'wt')
    tmpl = 'https://druginfo.nlm.nih.gov/drugportal/drug/names/{}'
    for letter in string.ascii_lowercase:
        print(letter)
        url = tmpl.format(letter)
        response = requests.get(url)
        if response.status_code == 200:
            p = BeautifulSoup(response.text, 'html.parser')
            for link in p.find_all(href=re.compile('/drugportal/name')):
                print(link.text, file=out)
        else:
            print(f'Error fetching "{url}": "{response.status_code}"',
                  file=sys.stderr)

    print('Done.')


# --------------------------------------------------
if __name__ == '__main__':
    main()
