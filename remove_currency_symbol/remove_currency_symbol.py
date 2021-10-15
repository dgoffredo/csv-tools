#!/usr/bin/env python3


import csv
import locale
import sys


def remove_currency_symbol(text, symbol='$'):
    stripped = text.strip()
    if stripped.startswith(symbol):
        try:
            number = locale.atof(stripped[1:])
            return stripped[1:]
        except ValueError:
            pass

    return text


if __name__ == '__main__':
    reader = csv.reader(sys.stdin)
    writer = csv.writer(sys.stdout)

    for row in reader:
        writer.writerow([remove_currency_symbol(value) for value in row])
