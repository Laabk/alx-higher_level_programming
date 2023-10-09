#!/usr/bin/python3
def multiple_returns(sentence):
    leng_of_sen = len(sentence)
    if (leng_of_sen == 0):
        the_tuple = (leng_of_sen, None)
    else:
        the_tuple = (leng_of_sen, sentence[0])
    return (the_tuple)
