#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """ Creating a new list by applying the 
    replacement rule using lambda and map"""
    
    my_new_list = list(map(lambda x: replace if x == search else x, my_list))

    return (my_new_list)
