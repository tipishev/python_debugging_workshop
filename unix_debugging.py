#!/usr/bin/env python3

from time import sleep
from itertools import cycle
from urllib import request

urls = cycle(['http://n-gate.com',
              'http://example.com',
              'https://sportamore.se'])

# sudo strace -s 1024 -v -p $PID

if __name__ == '__main__':

    print('The script is running...\nBut what is it doing?')

    with open('README.md') as f:
        lines = cycle(f.readlines())

        with open('out.txt', 'w') as g:

            for idx, (line, url) in enumerate(zip(lines, urls)):
                g.write(f'{line}\n')
                sleep(5)
                request.urlopen(url).read()
