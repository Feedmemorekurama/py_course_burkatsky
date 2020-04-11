#Take an array and remove every second element out of that array. 
# Always keep the first element and start removing with the next element.
#Example:
#my_list = ['Keep', 'Remove', 'Keep', 'Remove', 'Keep', ...]
#one of the arrays will be empty, so you don't have to worry about that!

def remove_every_other(my_list):
    return my_list[::2]

my_list=remove_every_other(['Keep','Remove','Keep','Remove','Keep','Remove'])
print(my_list)