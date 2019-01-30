def print_nested_structure(j, level=0):
    '''print_nested_structure
    Prints a list of all keys in a dictionary. The order and indentation shows any nested strucutre.
    
    Args:
        j (dict):
        level (int): Defaults to 0
    '''
    for k, v in j.items():
        print(' '*level, k)
        if isinstance(v, dict):
            print_nested_structure(v, level=level+1)
        elif (v is not None) & (type(v) != str):
            if isinstance(v[1], dict):
                print_nested_structure(v[0], level=level+1)
