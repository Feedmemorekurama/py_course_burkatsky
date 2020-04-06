#Americans are odd people: in their buildings, the first floor is actually the ground floor and there is no 13th floor ('cause of superstition).

#Write a function that given an American floor (passed as an integer) returns the real floor.
#Moreover, your function should work for basement floors too: just return the same value as the passed one.

def get_real_floor(n):
    if n <= 0:
        return n
    elif n >=13:
        return n-2
    else:
        return n-1
    