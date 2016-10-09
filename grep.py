import argparse

from find_files_for_mask import find_all_need_strings

def get_credentials(ip):
    return ("login", "password")

def parse_arguments():
    parser = argparse.ArgumentParser("Add ip, file mask and id to find on server")
    parser.add_argument("mask", type=str)
    parser.add_argument("ip", type=str)
    parser.add_argument("id", type=int)

    args = parser.parse_args()
    return args

def run_on_ssh(id, ip, credentials, mask):
    ssh credentials[0]@ip "python ./grep.py mask id"


def __name__ == "__main__":
    args = parse_arguments()
    run_on_ssh(args.id, get_credentials(args.ip), args.mask)
