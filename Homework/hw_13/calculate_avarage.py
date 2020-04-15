#Write function avg which calculates average of numbers in given list.

#Python:

#Due to rounding issues please do not use statistics.mean or such.
#If the array is empty, return 0.

#array = [ 1, 2, 3 ]
#Test.assert_equals(find_average(array), 2)






def find_average(array):
    return sum(array)/len(array) if len(array) >0 else 0