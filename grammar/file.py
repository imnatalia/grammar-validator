import sys

def check_file_name(fileName):
    if fileName != "gramatica.txt":
        sys.exit("O arquivo deve ser obrigatoriamente gramatica.txt")

def read_grammar_file():
    try:
        fileName = sys.argv[1] #para selecionar especificamente o segundo argumento, que deve ser o arquivo
        check_file_name(fileName)
        with open(fileName, 'r') as file:
            lines = file.readlines()
            return check_file(lines)
    except FileNotFoundError:
        sys.exit("Erro ao ler o arquivo de texto")
    except Exception as e:
        sys.exit(f"Erro ao ler arquivo: {e}")

def check_file(lines):
    if len(lines) == 0:
        sys.exit("O arquivo esta vazio, por favor adicione alguma regra para verificacao")
    elif len(lines) > 1:
        sys.exit("O arquivo contem mais de uma linha, por favor adicione apenas uma regra para verificacao")
    return lines

