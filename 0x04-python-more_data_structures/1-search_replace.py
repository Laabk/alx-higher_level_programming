#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def find_search(the_element):
        return the_element if the_element != search else replace
    return list(map(find_search, my_list))
