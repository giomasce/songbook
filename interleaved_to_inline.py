#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import codecs
import locale
import re

ITALIAN_CHORDS = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si']
ENGLISH_CHORDS = ['c', 'd', 'e', 'f', 'g', 'a', 'b']

CHORD_RE = re.compile(r"(\w*[^\d#bm ])(#|b|)(m|)(\d*)")

def categorize_line(line):
    if line == '':
        return 'BLANK'
    not_chords = CHORD_RE.sub('', line).strip()
    if not_chords == '':
        for match in CHORD_RE.finditer(line):
            if match.group(1).lower() not in ITALIAN_CHORDS + ENGLISH_CHORDS:
                return 'TEXT'
        return 'CHORDS'
    return 'TEXT'

def main():
    sys.stdout = codecs.getwriter(locale.getpreferredencoding())(sys.stdout.detach())
    sys.stdin = codecs.getreader(locale.getpreferredencoding())(sys.stdin.detach())
    interleaved = [x.strip() for x in sys.stdin.readlines()]
    for line in interleaved:
        print(categorize_line(line), line)

if __name__ == '__main__':
    main()
