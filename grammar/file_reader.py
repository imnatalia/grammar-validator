def read_grammar_file():
    try:
        with open('./gramatica.txt', 'r') as file:
            lines = file.readlines() #retorna um vetor com todas as linhas
            if len(lines) == 0:
                return None
            return lines
    except:
        return IndexError