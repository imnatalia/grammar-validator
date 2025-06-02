from dataclasses import dataclass

@dataclass
class GrammarComponents:
    terminais: list
    naoTerminais: list
    regras: list
    raiz: chr