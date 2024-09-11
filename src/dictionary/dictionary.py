def my_dictionary(param):
    value_pair = {}
    spaces = []
    if isinstance(param, int):
        param = str(param)
    if isinstance(param, str):
        param = param.lower()
    for char in param:
        if char == " ":
            spaces.append(char)
        else:
            if char in value_pair.keys():
                value_pair[char] = value_pair[char]+1
            else:
                value_pair[char] = 1

    return value_pair

