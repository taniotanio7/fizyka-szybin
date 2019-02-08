"""Convert Excel spreadsheet into python code formatting"""


def convert_spreadsheet(multi_line_string, type=float):
    str_list = multi_line_string.split('\n')
    for i, item in enumerate(str_list):
        if type == float:
            str_list[i] = float(item.replace(',', '.'))
        else:
            str_list[i] = type(float(item.replace(',', '.')))
    print(str_list)
    return str_list
