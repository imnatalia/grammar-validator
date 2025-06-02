#from grammar import GrammarComponents, read_grammar_file, terminal_symbols, non_terminal_symbols, check_rules
from .file_reader import read_grammar_file
from .symbols import terminal_symbols, non_terminal_symbols
from .check_rules import check_rules
from .grammar_model import GrammarComponents


def validator(condition):
    if condition == None:
        print("não há simbolos")
#todo - se tiver mais de uma linha deve retornar erro
#todo - retornar mensagens de erros especificos ex terminal nao pode gerar nao terminal
#reconhecer gramatica, por funcao
def check_grammar() -> GrammarComponents:
    #pega o arquivo
    raiz = ''
    terminais = []
    naoTerminais = []
    lines = read_grammar_file()
    #regras = []
    
    #para cada linha
    for line in lines:
        #regra 1 - a primeira parte da regra deve ser maiuscula, a qual sera a raiz
        if line[0].isupper():
            raiz = line[0]
        else:
            print("Sua regra nao esta bem formatada, o primeiro caracter da sua regra deve ser uma letra maiuscula")

        #regra final com $
        if line[-1] != '$':
            print("Sua regra nao esta bem formatada, o ultimo caracter da sua regra deve ser $")
        
        #regra 2 - ter terminais
        terminais = terminal_symbols(line)
        validator(terminais)

        #regra 3 - nao terminais
        naoTerminais = non_terminal_symbols(line)
        validator(naoTerminais)

        #regras
        #regras = line.split('-')
        
        #regra 4 - ver se a regra esta bem formatada
        if not check_rules(line):
            #regra certa
            print("Sua regra nao esta bem formatada.")

    return GrammarComponents(terminais, naoTerminais, line, raiz)