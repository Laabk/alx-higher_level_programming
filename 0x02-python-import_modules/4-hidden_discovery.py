#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    items = dir(hidden_4)
    for ite in items:
        if ite[:2] != '_':
            print(ite)
