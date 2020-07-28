def split_string(string_to_cut):
    cut_string = ''

    for i in range(2, len(string_to_cut), 3):
        cut_string += string_to_cut[i]

    return cut_string
