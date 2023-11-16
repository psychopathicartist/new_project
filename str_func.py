def make_str_upper(input_str):
    '''Делает все буквы заглавными'''
    upper_str = input_str.upper()
    return upper_str


def make_first_and_second_upper(input_str):
    '''Делает первые две буквы заглавными'''
    str_upper = input_str.upper()
    first_and_second_upper_str = str_upper[:2] + input_str[2:]
    return first_and_second_upper_str
