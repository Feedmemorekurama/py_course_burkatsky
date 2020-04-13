
#Implement a function that returns the minimal and the maximal value of a list.


def get_min_max(seq): 
    return (min(seq), max(seq))


#Example:
#test.assert_equals(get_min_max([1]), (1,1));
#test.assert_equals(get_min_max([1,2]), (1,2));
#test.assert_equals(get_min_max([2,1]), (1,2));