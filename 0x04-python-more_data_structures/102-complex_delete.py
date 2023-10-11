def complex_delete(a_dictionary, value):
    to_delkey = []
    for thekey in a_dictionary:
        if a_dictionary[thekey] == value:
            to_delkey.append(thekey)
    for thekey in to_delkey:
        del a_dictionary[thekey]
    return(a_dictionary)
