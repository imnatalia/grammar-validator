from .file import read_grammar_file
from .symbols import terminal_symbols, non_terminal_symbols
from .check_rules import check_rules
from .grammar_model import GrammarComponents

#validador para verificar se ha simbolos
def validator(condition, msg):
    if condition == False:
        print(msg)
        return None

def check_grammar() -> GrammarComponents:
    startSymbol = ''
    hasTerminals = []
    hasNonTerminals = []
    rules = []
    lines = read_grammar_file()
    if len(lines) > 1:
        print("A regra contem mais de uma linha! Por favor, indique apenas uma regra por vez")
        return None

    for line in lines:
        #regra 1 - o primeiro caracter deve ser maiusculo, o qual sera a raiz
        if line[0].isupper():
            startSymbol = line[0]
        else:
            print("Sua regra nao esta bem formatada, o primeiro caracter da sua regra deve ser uma letra maiuscula")
            return None

        #regra 2 - o final da regra deve ter o caracter $
        if line[-1] != '$':
            print("Sua regra nao esta bem formatada, o ultimo caracter da sua regra deve ser $")
            return None
        
        #regra 3 - verifica se tem terminais
        hasTerminals, msg = terminal_symbols(line)
        validator(hasTerminals, msg)

        #regra 4 - verifica se tem nao terminais
        hasNonTerminals, msg = non_terminal_symbols(line)
        validator(hasNonTerminals, msg)

        #pegar cada regra
        rules = line.split(';')
        
        #regra 5 - ve se a regra esta bem formatada (apenas nao terminais gerando)
        if not check_rules(rules):
            print("Sua regra nao esta bem formatada, ela deve seguir o padrao <lado-esquerdo(letras maiusculas)> > <lado-direito(maiusculas e/ou minusculas)> - <lado-esquerdo> > $.")
            return None
        
    return GrammarComponents(hasTerminals, hasNonTerminals, rules, startSymbol)