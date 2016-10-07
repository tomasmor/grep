import argparse

from find_string_in_file import find_string_in_file
from find_files_for_mask import find_files_for_mask


def parse_arguments():
    parser = argparse.ArgumentParser("Add ip, file mask and id to find on server")

    parser.add_argument("ip", type=str)
    parser.add_argument("mask", type=str)
    parser.add_argument("id", type=int)

    args = parser.parse_args()
    return args

grif __name__ == "__main__":
    args = parse_arguments()
    matches_files = find_files_for_mask(args.mask)
    for filename in matches_files:
        print find_string_in_file(filename, args.id)
