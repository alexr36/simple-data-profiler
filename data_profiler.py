#!/usr/bin/env python3

from argparse import ArgumentParser
from pandas import read_csv

from data_profiling import ProfileReport


def generate_report(filename: str, output: str) -> None:
    '''
    Generate a profiling report for the given .csv file.

    Params:
        filename (str): Path to the .csv file to profile.
        output (str): Path to the output HTML report.   
    Returns:
        None
    '''
    df = read_csv(filename)
    profile = ProfileReport(df, title=f'{filename} - Profiling Report', explorative=True)
    profile.to_file(output)


if __name__ == '__main__':
    parser = ArgumentParser(description='Simple data profiler for .csv files.')
    parser.add_argument('-f', '--file', help='Path to .csv file', default='data/dane.csv')
    parser.add_argument('-o', '--output', help='Path to output HTML report', default='reports/report.html')
    args = parser.parse_args()
    generate_report(args.file, args.output)