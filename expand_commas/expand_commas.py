#!/usr/bin/env python3


import csv
import sys


def expand_row(row, column_index=0):
    if column_index == len(row):
        yield None
        return
        
    for value in row[column_index]:
        suffixes = expand_row(row, column_index + 1)
        for suffix in suffixes:
            yield (value.strip(), suffix)


def chain_iter(chain):
    while chain is not None:
        value, chain = chain
        yield value


if __name__ == '__main__':
    reader = csv.reader(sys.stdin)
    writer = csv.writer(sys.stdout)
    for row in reader:
        parsed_row = [value.split(',') for value in row]
        for output_chain in expand_row(parsed_row):
            writer.writerow(chain_iter(output_chain))
