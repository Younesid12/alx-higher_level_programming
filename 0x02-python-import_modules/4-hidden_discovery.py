#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for mod in dir(hidden_4):
        if mod[1] != '_' and mod[0] != '_':
            print(mod)
