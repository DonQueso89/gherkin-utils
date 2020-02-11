#!/usr/bin/env python3
import argparse
import sys

import pandas as pd
from behave_pandas import dataframe_to_table
from collections import defaultdict
parser = argparse.ArgumentParser(
    usage="""
Convert parsed parameters from a feature file to a Gherkin table, optionally
adding some data to it from a json file.

Usage:
cat file.feature | grep -oh '<[a-z_]*>' | ~/this_script.py <datafile>

Parameters
----------
    datafile : str
        A json file containing a single list with objects describing the records
        to add to the table. Keys not present in the data, that are present in
        the table header will default to the string "None"

Returns
-------
    None
        result is written to stdout
"""
)


parser.add_argument("datafile", type=str, default=None)


def main():
    args = parser.parse_args()

    columns = set()
    for line in sys.stdin:
        line = line.strip()
        line = line.replace("<", "")
        line = line.replace(">", "")
        columns.add(line)

    df = pd.DataFrame(columns=columns)

    if args.datafile is not None:
        datadf = pd.read_json(args.datafile)
        df = df.append(datadf, ignore_index=True).fillna("None")

    print(dataframe_to_table(df[columns]))


main()
