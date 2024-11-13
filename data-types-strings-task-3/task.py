def replacer(s: str) -> str:
    conversion_table = str.maketrans({'"':"'", "'":'"'})
    return (s.translate(conversion_table))

