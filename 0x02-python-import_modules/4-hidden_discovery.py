#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    agm = dir(hidden_4)
    for items in range(len(agm)):
        if items[0:2] != '_':
            print(agm[items])
