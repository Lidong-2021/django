def str_to_code(string):
    """
    字符串转编码
    """
    code = ''
    for i in string:
        code += 'u' + str(ord(i))
    return code


def code_to_str(code):
    """
    编码转字符串
    """
    str_ = ''
    list_ = code.split('u')[1:]
    for i in list_:
        str_ += chr(int(i))
    return str_


# code1 = str_to_code('jiso')
# print(code1)
# str_1 = code_to_str(code1)
# print(str_1)
