MEDIANA = 101

def find_string_in_file(filename, pattern, mediana=MEDIANA):
    """
    returns first appearance of pattern in file and
    mediana strings before and after
    """
    chunk = []
    with open(filename, "rt") as opened_file:
        for line in opened_file:
            if len(chunk) == mediana:
                chunk.pop(0)
            chunk.append(line)
            if pattern in line:
                for i in range(1, mediana):
                    try:
                        next_line = opened_file.next()
                        chunk.append(next_line)
                    except StopIteration:
                        pass
                return chunk
            return []

if __name__ == "__main__":
    print find_string_in_file("find_string_in_file.py", "argparse")
