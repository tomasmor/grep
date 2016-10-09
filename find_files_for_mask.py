import os
import fnmatch

import argparse

from find_string_in_file import find_string_in_file

def parse_arguments():
    parser.add_argument("mask", type=str)
    parser.add_argument("id", type=int)

    args = parser.parse_args()
    return args


def find_files_for_mask(mask):
    """
    returns list of files on the machine with names matche mask
    """
    matches = []
    for root, dirnames, filenames in os.walk(r"/"): #on win change to smth like C:\
        for filename in fnmatch.filter(filenames, mask):
            matches.append(os.path.join(root, filename))
    return matches

def find_all_need_strings(mask, pattern):
    matches_files = find_files_for_mask(mask)
    for filename in matches_files:
        print find_string_in_file(filename, pattern)

if __name__ == "__main__":
    args = parse_arguments()
    find_all_need_strings(args.mask, args.id)
