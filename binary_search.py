# -*- coding: utf-8 -*-
"""
Binary Search Algorithm

Created on Tue Apr 23 00:20:55 2024

@author: paulo
"""

def binary_src(list_src, element_src):
    """
    Uses the binary search algorithm in a provided ordered list to find the 
    index of a provided element.

    Parameters
    ----------
    list_src : list
        The ordered list that will be used for the function.
    element_src : any
        The element that will be searched on the provided ordered list.

    Returns
    -------
    list_med : int
        If found, the function will return the element index.
    
    None :
        If not found, the function will return the None type

    """
    
    if type(list_src) != list: # *1
        raise TypeError("You must use an ordered list as a parameter for bynary_src!")
    
    list_min = 0
    list_max = len(list_src) - 1
    
    while list_min <= list_max: # *2
        list_med = (list_min + list_max) // 2 # "//": Floor division operator
        
        if list_src[list_med] > element_src: #*3
            list_max = list_med - 1
        
        if list_src[list_med] < element_src:
            list_min = list_med + 1
        
        if list_src[list_med] == element_src:
            return list_med
        
    return None
        
#------------------------------------------------------------------------------
# *1: This will check if the parameter passed to the function is, in fact, a 
# list. To check if the list is ordered, we would need a slower function: we
# will be relying on the user for this one.
#
# *2: No mater the list size, in the worst case scenario, the function will be
# analizing a sublist with a lenght 1 in its last step. After the 2 extremes 
# passes, all elements will have been analized.
#
# *3: If the middle element (index rounded down) is greater than the searched
# element, the second half of the list will be excluded and the pointer at the
# end of the list will be translated to the position before the checked 
# element. The simetric solution will be applied if the middle element is 
# smaller than the searched element.
#------------------------------------------------------------------------------