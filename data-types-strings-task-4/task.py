def check_str(s: str):
    s1 = s.replace(" ", "")
    s2 = s1.replace("-", "")
    s3 = s2.replace(",", "")
    s4 = s3.replace("\'", "")
    new_string = s4[::-1]
    if s4.lower() == new_string.lower():
        return True
    else:
        return False




