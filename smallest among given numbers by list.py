def smallest_of( list ):
    min = list[ 0 ]
    for x in list:
        if x < min:
            min = x
    return min
print(smallest_of([10,5,3,7,8,3,8]))
