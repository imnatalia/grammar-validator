import re

def check_rules(rules):
    padraoRegra = re.compile(r'^([A-Z])>([A-Za-z\$]+)$')
    isMatch = []
    
    for rule in rules:
        noWhiteSpace = rule.strip().replace(" ", "")
        isMatch = padraoRegra.match(noWhiteSpace)
        if not isMatch:
            return False
        
    return True