#!us/user/bin/python3
def magic_string():
    magic_string.time = getattr(magic_string, 'time', 1) + 1
    return ", ".join(['BestSchool'] * magic_string.time)
