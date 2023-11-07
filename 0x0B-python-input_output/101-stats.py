#!/usr/bin/python3
"""this function reads from the standard input and
adds the available metrics
"""


def print_stats(th_size, status_codes):
    """
    Prints all the available metrics
    """
    print("File size: {}".format(th_size))
    for key in sorted(status_codes):
        print("{}: {}".format(key, status_codes[key]))


if __name__ == "__main__":
    import sys

    th_size = 0
    status_codes = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    numb = 0

    try:
        for l in sys.stdin:
            if numb == 10:
                print_stats(th_size, status_codes)
                numb = 1
            else:
                numb += 1

            l = l.split()

            try:
                th_size += int(l[-1])
            except (IndexError, ValueError):
                pass

            try:
                if l[-2] in valid_codes:
                    if status_codes.get(l[-2], -1) == -1:
                        status_codes[l[-2]] = 1
                    else:
                        status_codes[l[-2]] += 1
            except IndexError:
                pass

        print_stats(th_size, status_codes)

    except KeyboardInterrupt:
        print_stats(th_size, status_codes)
        raise
