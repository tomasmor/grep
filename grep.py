import argparse
import subprocess

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

def run_on_ssh(_id, ip, credentials, mask):
    subprocess.call('ssh {0}@{1} "python find_files_for_mask.py {2} {3}"'.format(credentials[0], ip, mask, _id))

if __name__ == "__main__":
    args = parse_arguments()
    run_on_ssh(args.id, args.ip, get_credentials(args.ip), args.mask)
