def string_function(pram1, pram2):
    first_string = []
    second_string = []

    for char in pram1:
        first_string.append(char)

    for char in pram2:
        second_string.append(char)

    last_letter_of_string1 = first_string[len(first_string) - 1]

    last_letter_of_string2 = second_string[len(second_string) - 1]

    first_string.remove(last_letter_of_string1)

    second_string.remove(last_letter_of_string2)

    final_string1 = ""
    for char in first_string:
        final_string1 += char

    final_string2 = final_string1 + last_letter_of_string2 + " "
    final_string3 = ""
    for char in second_string:
        final_string3 += char
    final_string = final_string2 + final_string3 + last_letter_of_string1
    return final_string

def string_functions(param):
    first_string = ""
    second_string = ""
    count = 0
    for char in param:
        count += 1
        if count <= 3:
            first_string += char
        else:
            second_string += char
        final_string = first_string + "ce" + second_string
    return final_string

def string_function1(param):
    caps = ""
    lower_case = ""
    for char in param:
        if char.isupper():
            caps += char
        else:
            lower_case += char
    final_string = caps + lower_case
    return final_string

def string_function2(param):
    UPPER_CASE = ["A","B","C", "D", "E", "F", "G", "H",
                  "I", "J", "K", "L", "M", "N", "O", "P",
                  "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

    LOWER_CASE = ["a", "b",	"c", "d", "e", "f",	"g", "h", "i",	"j",
                  "k", "l",	"m", "n", "o", "p", "q", "r", "s", "t",
                  "u", "v", "w", "x", "y", "z"]
    characters = []
    word = ""
    for char in param:
        if char not in UPPER_CASE and char not in LOWER_CASE:
            characters.append(char)
        else:
            word += char
    return word

def string_function3(param):
    

    return param