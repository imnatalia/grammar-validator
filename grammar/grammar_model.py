from dataclasses import dataclass

@dataclass
class GrammarComponents:
    terminals: list[str]
    nonTerminals: list[str]
    rules: list[str]
    firstSymbol: str