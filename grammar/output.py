from grammar import check_grammar
#gerar o output da gramatica
def generate_grammar_output():
    #formarta a gramatica
    result = check_grammar()
    if result is not None:
        print(f"G = (N, E, P, S), onde N = nao terminais, E = terminais, P = regras e S = regras")
        print(f"N = {result.nonTerminals}")
        print(f"E = {result.terminals}")
        print(f"P = {result.rules}")
        print(f"S = {result.firstSymbol}")
