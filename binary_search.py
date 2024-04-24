# -*- coding: utf-8 -*-
"""
Binary Search Algorithm

Created on Tue Apr 23 00:20:55 2024

@author: paulo
"""
#------------------------------------------------------------------------------
# This function needs an ordered list as a parameter and an element of that 
# list as an argument. The function will search the list for the given 
# parameter and, if its found, it will return its index.
#
# If the argument is not found on the list, the function will return "none".
#------------------------------------------------------------------------------

def binary_src(list_src, element_src):
    
    list_min = 0
    list_max = len(list_src) - 1
    
    while list_min <= list_max: # *1
        list_med = (list_min + list_max) // 2 # "//": Floor division operator
        
        if list_src[list_med] > element_src:
            list_max = list_med - 1
        
        if list_src[list_med] < element_src:
            list_min = list_med + 1
        
        if list_src[list_med] == element_src:
            return list_med
        
    return None
        
#------------------------------------------------------------------------------
# *1: No mater the list size, in the worst case scenario, the function will be
# analizing a sublist with a lenght 1 in its last step. After the 2 extremes 
# passes, all elements will have been analized.
#------------------------------------------------------------------------------