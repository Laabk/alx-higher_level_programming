#!/usr/bin/python3
for the_cha in reversed(range(97, 123)):
    print("{:c}".format(the_cha if (the_cha % 2 == 0) else (the_cha - 32)), end='')
