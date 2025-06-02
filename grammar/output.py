from grammar import check_grammar
#gerar o output da gramatica
def generate_grammar_output():
    #formarta a gramatica
    resultado = check_grammar()
    print(f"G = (N, epson, P, S), onde N = nao terminais, epson = terminais, P = regras e S = regras")
    print(f"N = {resultado.naoTerminais}")
    print(f"epson = {resultado.terminais}")
    print(f"P = {resultado.regras}")
    print(f"S = {resultado.raiz}")
