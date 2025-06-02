def terminal_symbols(line):
    symbols = []
    for letter in line:
        if letter.islower() and letter not in symbols:
            symbols += letter
    if len(symbols) == 0:
        return None
    return symbols

def non_terminal_symbols(line):
    symbols = []
    for letter in line:
        if letter.isupper() and letter not in symbols:
            symbols += letter
    if len(symbols) == 0:
        return None
    return symbols