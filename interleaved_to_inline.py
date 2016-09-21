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

def canonicalize_chord(chord):
    chord = list(chord)
    chord[0] = chord[0].lower()
    if chord[0] in ITALIAN_CHORDS:
        chord[0] = ENGLISH_CHORDS[ITALIAN_CHORDS.index(chord[0])]
    return tuple(chord)

def apply_chords_to_text(chords, text):
    subst = []
    for match in CHORD_RE.finditer(chords):
        chord = canonicalize_chord(match.groups())
        pos = match.start()
        subst.append((chord, pos))
    subst.reverse()
    for chord, pos in subst:
        text = text[:pos] + "[" + "".join(chord) + "]" + text[pos:]
    return text

def main():
    sys.stdout = codecs.getwriter(locale.getpreferredencoding())(sys.stdout.detach())
    sys.stdin = codecs.getreader(locale.getpreferredencoding())(sys.stdin.detach())
    interleaved = [x.rstrip() for x in sys.stdin.readlines()]
    #for line in interleaved:
    #    print(categorize_line(line), line)
    print(apply_chords_to_text(interleaved[2], interleaved[3]))

if __name__ == '__main__':
    main()
