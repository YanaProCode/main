from typing import List

def split(data: str, sep=None, maxsplit=-1):
    if not data:
        return []
    result = []
    temp_string = ''
    count = 0
    sep_len = len(sep) if sep else 1

    for i in range(len(data)):
        if data[i:i+sep_len] != sep and (data[i] != ' ' or sep is not None):
            temp_string += data[i]
        elif data[i:i+sep_len] == sep or (sep is None and data[i] == ' ' and temp_string):
            result.append(temp_string)
            temp_string = ''
            count += 1
            if maxsplit != -1 and count == maxsplit:
                temp_string = data[i+sep_len:].lstrip()
                break
            if sep:
                i += sep_len - 1
    if maxsplit == 0 and sep is None:
        return [data.strip()]
    result.append(temp_string)

    return result


data = '    Hi     Python    world!    '
print(split(data))
print(split(',123,', sep=','))
print(split('Python    2     3', maxsplit=1))
print(split('    test     6    7', maxsplit=1))

if __name__ == '__main__':
    assert split('') == []
    assert split(',123,', sep=',') == ['', '123', '']
    assert split('test') == ['test']
    assert split('Python    2     3', maxsplit=1) == ['Python', '2     3']
    assert split('    test     6    7', maxsplit=1) == ['test', '6    7']
    assert split('    Hi     8    9', maxsplit=0) == ['Hi     8    9']
    assert split('    set   3     4') == ['set', '3', '4']
    assert split('set;:23', sep=';:', maxsplit=0) == ['set;:23']
    assert split('set;:;:23', sep=';:', maxsplit=2) == ['set', '', '23']