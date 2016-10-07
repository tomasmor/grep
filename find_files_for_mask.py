import os
import fnmatch

def find_files_for_mask(mask):
    """
    returns list of files on the machine with names matche mask
    """
    matches = []
    for root, dirnames, filenames in os.walk(r"/"): #on win change to smth like C:\
        for filename in fnmatch.filter(filenames, mask):
            matches.append(os.path.join(root, filename))
    return matches


if __name__ == "__main__":
    find_files_for_mask("*.py")
