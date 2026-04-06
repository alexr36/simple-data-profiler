#!/usr/bin/env python3

from argparse import ArgumentParser
from pandas import read_csv

from ydata_profiling import ProfileReport


def generate_report(filename: str = 'data/dane.csv') -> None:
    '''
    Generate a profiling report for the given .csv file.

    Params:
        filename (str): Path to the .csv file to profile.
    
    Returns:
        None
    '''
    df = read_csv(filename)
    profile = ProfileReport(df, title=f'{filename} - Profiling Report', explorative=True)
    profile.to_file('report.html')


if __name__ == '__main__':
    parser = ArgumentParser(description='Simple data profiler for .csv files.')
    parser.add_argument('-f', '--file', help='Path to .csv file', default='data/dane.csv')
    args = parser.parse_args()
    generate_report(args.file)
