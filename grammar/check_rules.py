import re

#todo - verificacao para caracteres invalidos no meio da regra
#todo - verificacao de terminal gerando algo
def check_rules(rules):
    padraoRegra = re.compile(r'^([A-Z])>(.*)$')
    isMatch = []
    
    for rule in rules:
        noWhite = rule.replace(" ", "")
        isMatch = padraoRegra.match(noWhite)
        if not isMatch:
            return False
    return True